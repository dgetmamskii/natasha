from yargy import rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram, eq, type, in_
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline

INT = type('INT')

Innpegent = fact(
    'Innpegent',
    ['num']
)

INNNUM = rule(INT).interpretation(
    Innpegent.num.custom(int)
)

#Правило для номера ИНН
INNORG = rule(eq('ИНН'), INNNUM).interpretation(
    Innpegent
)





