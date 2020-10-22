from yargy import Parser as YargyParser
from yargy.morph import MorphAnalyzer
from yargy.tokenizer import MorphTokenizer

def findINN(text):
    from .data.inn import INNORG
    parser = Parser(INNLEGENT)
    matches = list(parser.findall(text))
    if matches:
        return matches


def findDATECOAST(text):
    from .data.datecoast import DATECOASTCASE
    parser = Parser(DATECOASTCASE)
    matches = list(parser.findall(text))
    if matches:
        return matches



def findDATECONT(text):
    from .data.datecont import DATECONT
    parser = Parser(DATECONT)
    matches = list(parser.findall(text))
    if matches:
        return matches



def findNCOASTCASE(text):
    from .data.ncoast import NCOASTCASE
    parser = Parser(NCOASTCASE)
    matches = list(parser.findall(text))
    if matches:
        return matches


def findNCONTRACT(text):
    from .data.ncont import NCONTRACT
    parser = Parser(NCONTRACT)
    matches = list(parser.findall(text))
    if matches:
        return matches
        

