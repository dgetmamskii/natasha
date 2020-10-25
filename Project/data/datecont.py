from yargy import rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram, eq, type, in_
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline
from .data import NCONTRACT

INT = type('INT')
DOT = eq('.')
LEFT = eq('<')
RIGHT = rule(in_('>.'))

Datecont = fact(
    'Datecont',
    ['day','mounth','year']
)

OT = rule(eq('от'))

BEFOREDATE = or_(
    NCONTRACT,
    OT
)

DAY = rule(INT).interpretation(
    Datecont.day.custom(int)
)

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
).interpretation(
    Datecont.mounth
)

YEAR = rule(INT).interpretation(
    Datecont.year.custom(int)
)

#Правило для даты документа
DATECONT = rule(
    BEFOREDATE,
    LEFT.optional(),
    DAY,
    RIGHT.optional(),
    MOUNTH,
    DOT.optional(),
    YEAR
).interpretation(
    Datecont
)

