from yargy import rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram, eq, type, in_
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline

INT = type('INT')

#Слова до номера документа
NCONTRWORD = morph_pipeline([
    'ПЛАТЕЖНОЕ ПОРУЧЕНИЕ №'
]) 

Ncontract = fact(
    'Ncontract',
    ['num']
)

#Слова до номера документа
NCONTRWORD = morph_pipeline([
    'ПЛАТЕЖНОЕ ПОРУЧЕНИЕ №'
])

NUM = rule(INT).interpretation(
    Ncontract.num.custom(int)
)

#Правило для номера документа
NCONTRACT = rule(NCONTRWORD,NUM).interpretation(
    Ncontract
)

