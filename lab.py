from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    
    PER,

    Doc
)

from ipymarkup import show_span_ascii_markup as show_markup

from yargy import Parser, rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram, eq, type, in_
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline



segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)


text ='''Поступ. в банк плат.		Списано со сч. плат.	
			
			
			
ПЛАТЕЖНОЕ ПОРУЧЕНИЕ № 	000139	09.12.2019				
						
		Дата		Вид платежа		
						
Сумма
прописью	Пять тысяч триста двенадцать рублей 00 копеек
ИНН 8812089467	КПП 671110011	Сумма	5312=
ООО «Колокольчик» //Россия, г.Москва, ул. Школьная, 18. //			
		Сч. №	40511637819274016748
			
Плательщик		
ОАО «Прайд-Банк» г.Москва		БИК	БИК ОАО «Прайд-Банк»-044657485
		Сч. №	
			
Банк плательщика		30104563780000007684
ГРКЦ ГУ Банка России, по Московской области г.Москва		БИК	046674859
		Сч. №	
			
Банк получателя		
ИНН 5647382956	КПП 887801001	Сч. №	40105674000000564839
Управление федерального казначейства по Московской области			
		Вид оп.	01	Срок плат.	
		Наз.пл.		Очер.плат.	3
			0		
Получатель	Код		Рез.поле	
				
17253674000047382949	12467000000	ТП	МС.09.2016	0	0	


Страховые взносы на обязательное пенсионное страхование
Назначение платежа
	Подписи		Отметки банка	

Дело № 2222-22222-22222
Делу № 222-1111-22222
				
	М.П.					
'''						
											
doc = Doc(text)

doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.tag_ner(ner_tagger)

INT = type('INT')
DOT = eq('.')
LEFT = eq('<')
RIGHT = rule(in_('>.'))
DASH = eq('-')

#Правило для номера ИНН
INNORG = rule(eq('ИНН'), INT)

text1 = 'ПЛАТЕЖНОЕ ПОРУЧЕНИЕ № 	000139	12.09.2016'

#Слова до номера документа
NCONTRWORD = morph_pipeline([
    'ПЛАТЕЖНОЕ ПОРУЧЕНИЕ №'
])  

#Правило для номера документа
NCONTRACT = rule(NCONTRWORD,INT)

OT = rule(eq('от'))

BEFOREDATE = or_(
    NCONTRACT,
    OT
)

DAY = rule(INT)
MOUNTH = or_(
    morph_pipeline([
        'январь',
        'февраль',
        'март',
        'апрель',
        'май',
        'июнь',
        'июль',
        'август',
        'сентябрь',
        'октябрь',
        'ноябрь',
        'декабрь'
    ]),
    rule(INT)
)

YEAR = rule(INT)

#Правило для даты документа
DATECONT = rule(
    BEFOREDATE,
    LEFT.optional(),
    DAY,
    RIGHT.optional(),
    MOUNTH,
    DOT.optional(),
    YEAR
)

FIRST = rule(INT)
SECOND = rule(INT)
THIRD = rule(INT)

#Правило для номера судебного дела
NCOASTCASE = rule(  morph_pipeline(['Дело']),eq('№'),FIRST,DASH,SECOND,DASH,THIRD)

parser = Parser(NCOASTCASE)
matches = list(parser.findall(text))
spans = [_.span for _ in matches ]
show_markup(text,spans)        



