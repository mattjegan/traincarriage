
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

def factorial(x):
    x = x.evaluate() if hasattr(x, 'evaluate') else x
    try:
        return math.factorial(x)
    except ValueError:
        raise ZeroDivisionError

BINARY_OPS = [
    div,
    mul,
    add,
    sub,
]

CLAUSE_UNARY_OPS = [
    noop,
    floor,
    ceil,
    #factorial
]

SINGLE_UNARY_OPS = [
    noop,
    factorial,
]

SYMBOL_MAP = {
    div: '/',
    mul: '*',
    add: '+',
    sub: '-',
}