''' Mutable Primitives '''
from types import FunctionType
import sys


EQUALITY_FUNCTIONS = [
        '__eq__',
        '__ne__',
        ]

MATH_FUNCTIONS = [
        ('add', '+'),
        ('sub', '-'),
        ('mul', '*'),
        # Division is handled differently in python2 and python3
        ]
if sys.version_info[0] < 3:
    MATH_FUNCTIONS.append(('div', '/'))
else:
    MATH_FUNCTIONS.extend([
        ('floordiv', '//'),
        ('truediv', '/'),
        ])


FORMATS = {
        '': 'return self.val {} other',
        'r': 'return other {} self.val',
        'i': 'self.val {}= other; return self',
        }


class Mutable(object): # pylint: disable=useless-object-inheritance
    ''' Base class for mutable primitives '''
    def __init__(self, val):
        self.val = val

    def get(self):
        ''' get raw value of mutable '''
        return self.val

    def set(self, val):
        ''' set raw value of mutable '''
        self.val = val

    def __eq__(self, other):
        return self.val == other

    def __ne__(self, other):
        return self.val != other

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.val)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.val)


class Bool(Mutable):
    ''' Mutable version of float '''


class MutableNumeric(Mutable):
    ''' Base class for mutable numeric primitives '''

    for fmt, basecode in FORMATS.items():
        for (basename, op) in MATH_FUNCTIONS:
            name = '__{}{}__'.format(fmt, basename)
            code = 'def {}(self, other): {}'.format(name, basecode.format(op))
            code = compile(code, "<string>", "exec")
            locals()[name] = FunctionType(code.co_consts[0], globals(), name)
            del code, name, op


class Int(MutableNumeric):
    ''' Mutable version of int '''

class Float(MutableNumeric):
    ''' Mutable version of float '''
