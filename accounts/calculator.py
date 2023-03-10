def zero(op=None):
    if op:
        return op(0)
    return 0

def one(op=None):
    if op:
        return op(1)
    return 1

def two(op=None):
    if op:
        return op(2)
    return 2

def three(op=None):
    if op:
        return op(3)
    return 3

def four(op=None):
    if op:
        return op(4)
    return 4

def five(op=None):
    if op:
        return op(5)
    return 5

def six(op=None):
    if op:
        return op(6)
    return 6

def seven(op=None):
    if op:
        return op(7)
    return 7

def eight(op=None):
    if op:
        return op(8)
    return 8

def nine(op=None):
    if op:
        return op(9)
    return 9

def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y

def times(y):
    return lambda x: x * y

def divided_by(y):
    return lambda x: x // y