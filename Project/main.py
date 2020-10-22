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
import reader

def addinres(res, x, name):
    d = {}
    d[name] = x
    res = res + [d]


entity = ['ФИО', 'ИНН', '№ судебного приказа', '№ договора', 'Дата документа', 'Дата договора', 'Юрлица', 'Сумма']

inprog = []
inprog += [['ИНН', 'ФИО']]
inprog += ['docx']
inprog += ['example.docx']

res = []

segmenter = Segmenter()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
morph_vocab = MorphVocab()

names_extractor = NamesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)

text1 = 'Посол Израиля на Украине Йоэль Лион признался, что пришел в шок, узнав о решении властей Львовской области объявить 2019 год годом лидера запрещенной в России Организации украинских националистов (ОУН) Степана Бандеры...'

if inprog[1] == 'docx':
    text = readdocx(improg[2])
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)
    for span in doc.spans:
        span.normalize(morph_vocab)
    for ent in inprog[0]:
        if entity.count(ent) == 1:
            if ent == 'ФИО':
                for span in doc.spans:
                    if span.type == PER:
                        span.extract_fact(names_extractor)
                x = [_.fact.as_dict for _ in doc.spans if _.type == PER]
                if x:
                    addinres(res, x, 'ФИО')
            if ent == 'ИНН':
                matches = findINN(text)
                y = [_.fact for _ in matches]
                if y:
                    addinres(res, y, 'ИНН')
            if ent == '№ судебного приказа':
                matches = findNCOASTCASE(text)
                y = [_.fact for _ in matches]
                if y:
                    addinres(res, y, '№ судебного приказа')
            if ent == '№ договора':
                matches = findNCONTRACT(text)
                y = [_.fact for _ in matches]
                if y:
                    addinres(res, y, '№ договора')
            if ent == 'Дата документа':
                matches = findDATECOAST(text)
                y = [_.fact for _ in matches]
                if y:
                    addinres(res, y, 'Дата документа')
            if ent == 'Дата договора':
                matches = findDATECONT(text)
                y = [_.fact for _ in matches]
                if y:
                    addinres(res, y, 'Дата договора')
            if ent == 'Юрлица':
                y = []
                for span in doc.spans:
                    if span.type == ORG:
                        d = {}
                        d['name'] = span.text
                        y = y + [d]
                if y:
                    addinres(res, y, 'Юрлица')
            if ent == 'Сумма':
                matches = list(money_extractor(text1))
                y = [_.fact for _ in matches]
                if y:
                    addinres(res, y, 'Сумма')
print(res)

