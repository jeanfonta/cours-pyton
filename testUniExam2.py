import unittest
from exam2 import programme

def verifieCodePostal():
    for i in programme():
        code = int(i[1])
        assert code >= 5000 and code <= 5100


def verifiePair():
    for i in programme():
        codeP = int(i[1])
        assert codeP % 2 == 0

verifiePair()