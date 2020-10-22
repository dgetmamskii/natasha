from yargy import rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram, eq, type, in_
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline

INT = type('INT')
DASH = eq('-')

Ncoastcase = fact(
    'Ncoastcase',
    ['first','second','third']
)

FIRST = rule(INT).interpretation(
    Ncoastcase.first.custom(int)
)
SECOND = rule(INT).interpretation(
    Ncoastcase.second.custom(int)
)
THIRD = rule(INT).interpretation(
    Ncoastcase.third.custom(int)
)

#Правило для номера судебного дела
NCOASTCASE = rule(  morph_pipeline(['Дело']),eq('№'),FIRST,DASH,SECOND,DASH,THIRD).interpretation(
    Ncoastcase
)
