from yargy import Parser, rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline


text ='''Поступ. в банк плат.		Списано со сч. плат.	
			
			
			
ПЛАТЕЖНОЕ ПОРУЧЕНИЕ № 	000139	12.09.2016				
						
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
				
				
	М.П.					
'''

Innnum = fact(
    'Innnum',
    ['num']
)

Namelegent = fact(
    'Namelegent',
    ['name']
)

INT = type('INT')

INN = morph_pipeline([
    'ИНН'
])

ORG = gram('ORG')


LEGENT = rule(
    ORG
)
    
INNLEGENT = rule(
    INN,
    INT,
    ORG
)    

parser = Parser(LEGENT)
match = parsec.match(text)
print(match)



