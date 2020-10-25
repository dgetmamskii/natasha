from natasha import (
    Segmenter,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    MorphVocab,
    PER,
    ORG,
    NamesExtractor,
    MoneyExtractor,
    
    Doc
)

import myextractors

status = 1
res = {}

segmenter = Segmenter()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
morph_vocab = MorphVocab()

names_extractor = NamesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)

text = 'Посол Израиля на Украине Йоэль Лион признался, что пришел в шок, узнав о решении властей Львовской области объявить 2019 год годом лидера запрещенной в России Организации украинских националистов (ОУН) Степана Бандеры...'

docType = 'coast'

doc = Doc(text)
doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)
doc.tag_ner(ner_tagger)

for span in doc.spans:
    span.normalize(morph_vocab)

#для судебного приказа    
if docType == 'coast':
    #фио
    for span in doc.spans:
        if span.type == PER:
            span.extract_fact(names_extractor)
    x = [_.fact.as_dict for _ in doc.spans if _.type == PER]
    if x:
        res['ФИО'] = x
    else:
        status = 0
    #инн
    y = findINN(text)
    if y:
        res['ИНН'] = y
    else:
        status = 0
    #номер судебного приказа 
    y = findNCOASTCASE(text)
    if y:
        res['номер судебного приказа'] = y
    else:
        status = 0
    #дата с п
    y = findDATECOAST(text)
    if y:
        res['дата судебного приказа'] = y
    else:
        status = 0
    #организации
    y = []
    for span in doc.spans:
        if span.type == ORG:
            d = {}
            d['name'] = span.text
            y = y + [d]
    if y:
        res['организации'] = y
    else:
        status = 0

#для письма      
if docType == 'mail':
    #фио
    for span in doc.spans:
                if span.type == PER:
                    span.extract_fact(names_extractor)
    x = [_.fact.as_dict for _ in doc.spans if _.type == PER]
    if x:
        res['ФИО'] = x
    else:
        status = 0
    #инн
    y = findINN(text)
    if y:
        res['ИНН'] = y
    else:
        status = 0
    #номер дог
    y = findNCONTRACT(text)
    if y:
        res['номер договора'] = y
    else:
        status = 0
    #дата дог
    y = findDATECONT(text)
    if y:
        res['дата договора'] = y
    else:
        status = 0

#для платежного поручения        
if docType == 'order':
    #фио
    for span in doc.spans:
        if span.type == PER:
            span.extract_fact(names_extractor)
    x = [_.fact.as_dict for _ in doc.spans if _.type == PER]
    if x:
        res['ФИО'] = x
    else:
        status = 0
    #инн
    y = findINN(text)
    if y:
        res['ИНН'] = y
    else:
        status = 0
    #организации
    y = []
    for span in doc.spans:
        if span.type == ORG:
            d = {}
            d['name'] = span.text
            y = y + [d]
    if y:
        res['организации'] = y
    else:
        status = 0
    #номер дог
    y = findNCONTRACT(text)
    if y:
        res['номер договора'] = y
    else:
        status = 0
    #дата дог
    y = findNCONTRACT(text)
    if y:
        res['номер договора'] = y
    else:
        status = 0
    #сумма
    matches = list(money_extractor(text))
    y = [_.fact for _ in matches]
    ret = []
    for i in y:
        z = {}
        z['amount'] = i.amount
        z['currency'] = i.currency
        ret = ret + [z]
    if ret:
        res['сумма'] = ret 
    else:
        status = 0

returning = {}
        
if status == 1:
    returning['status'] = 'успех'
else:
    returning['status'] = 'не успех'
    
returning['entities'] = ret

print(res)

