from yargy import Parser as YargyParser
from yargy.morph import MorphAnalyzer
from yargy.tokenizer import MorphTokenizer

def findINN(text):
    from .data.inn import INNORG
    parser = Parser(INNORG)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['num'] = i.num
        ret = ret + [z]
    if ret:
        return ret


def findDATECOAST(text):
    from .data.datecoast import DATECOASTCASE
    parser = Parser(DATECOASTCASE)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['day'] = i.day
        z['mounth'] = i.mouth
        z['year'] = i.year
        ret = ret + [z]
    if ret:
        return ret



def findDATECONT(text):
    from .data.datecont import DATECONT
    parser = Parser(DATECONT)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['day'] = i.day
        z['mounth'] = i.mouth
        z['year'] = i.year
        ret = ret + [z]
    if ret:
        return ret



def findNCOASTCASE(text):
    from .data.ncoast import NCOASTCASE
    parser = Parser(NCOASTCASE)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['first'] = i.first
        z['second'] = i.second
        z['third'] = i.third
        ret = ret + [z]
    if ret:
        return ret


def findNCONTRACT(text):
    from .data.ncont import NCONTRACT
    parser = Parser(NCONTRACT)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['num'] = i.num
        ret = ret + [z]
    if ret:
        return ret 
