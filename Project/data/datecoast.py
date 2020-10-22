from yargy import rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram, eq, type, in_
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline

INT = type('INT')
DOT = eq('.')
LEFT = eq('<')
RIGHT = rule(in_('>.'))


Datecoastcase = fact(
    'Datecoastcase',
    ['day','mounth','year']
)

OT = rule(eq('от'))

BEFOREDATE = or_(
    OT
)

DAY = rule(INT).interpretation(
    Datecoastcase.day.custom(int)
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
    Datecoastcase.mounth
)

YEAR = rule(INT).interpretation(
    Datecoastcase.year.custom(int)
)
DATECOASTCASE = rule(
    BEFOREDATE,
    LEFT.optional(),
    DAY,
    RIGHT.optional(),
    MOUNTH,
    DOT.optional(),
    YEAR
).interpretation(
    Datecoastcase
)

