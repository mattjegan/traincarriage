
import math

from BinaryOperator import BinaryOperator
from UnaryOperator import UnaryOperator

def add(x, y):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    y = y.evaluate() if hasattr(y, 'evaluate') else y
    return x + y

def sub(x, y):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    y = y.evaluate() if hasattr(y, 'evaluate') else y
    return x - y

def mul(x, y):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    y = y.evaluate() if hasattr(y, 'evaluate') else y
    return x * y

def div(x, y):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    y = y.evaluate() if hasattr(y, 'evaluate') else y
    return float(x) / float(y)

def noop(x):
    return x.evaluate() if hasattr(x, 'evaluate') else x

def floor(x):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    return math.floor(x)

def ceil(x):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    return math.ceil(x)

def abso(x):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    return abs(x)

cache = {}
def factorial(x):
    global cache
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    try:
        if x in cache:
            return cache[x]
        fac = math.factorial(x)
        cache[x] = fac
        return fac
    except ValueError:
        raise ZeroDivisionError

def exponent(x, y):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    y = y.evaluate() if hasattr(y, 'evaluate') else y
    return math.pow(x, y)

BINARY_OPS = [
    div,
    mul,
    add,
    sub,
    exponent,
]

CLAUSE_UNARY_OPS = [
    noop,
    floor,
    ceil,
    abso,
    #factorial
]

SINGLE_UNARY_OPS = [
    noop,
    factorial
]

SYMBOL_MAP = {
    div: '/',
    mul: '*',
    add: '+',
    sub: '-',
}