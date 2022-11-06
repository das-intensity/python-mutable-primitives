import sys
from types import FunctionType
import unittest

from mutable_primitives import (
        Int,
        Float,
        Bool,
        Str
        )

DEFAULTS = {
        # Intentionally put zero-values last to ensure others are used for equality comparisons
        "int": [5, 7, 0],
        "bool": [True, False],
        "float": [3.431, 8.543, 0.0],
        "str": ["a","z","asdf"]
        }


class TestBasic(unittest.TestCase):
    typ = None
    name = None

    def test_eq(self):
        # Both mutables
        assert self.typ(DEFAULTS[self.name][0]) == self.typ(DEFAULTS[self.name][0])
        assert self.typ(DEFAULTS[self.name][0]) != self.typ(DEFAULTS[self.name][1])

        # mutable lvalue, primitive rvalue
        assert self.typ(DEFAULTS[self.name][0]) == DEFAULTS[self.name][0]
        assert self.typ(DEFAULTS[self.name][0]) != DEFAULTS[self.name][1]

        # primitive lvalue, mutable rvalue
        assert DEFAULTS[self.name][0] == self.typ(DEFAULTS[self.name][0])
        assert DEFAULTS[self.name][0] != self.typ(DEFAULTS[self.name][1])

    def test_truthiness(self):
        # check boolean evaluation
        for val in DEFAULTS[self.name]:
            if val:
                assert self.typ(val), "{} evaluates True, but {} evaluates False".format(val, self.typ(val))
            else:
                assert not self.typ(val), "{} evaluates False, but {} evaluates True".format(val, self.typ(val))

    def test_set_get(self):
        obj = self.typ(DEFAULTS[self.name][0])
        assert obj.val == DEFAULTS[self.name][0]
        assert obj.get() == DEFAULTS[self.name][0]

        obj.set(DEFAULTS[self.name][1])
        assert obj.val == DEFAULTS[self.name][1]
        assert obj.get() == DEFAULTS[self.name][1]

    def test_stringify(self):
        obj = self.typ(DEFAULTS[self.name][0])
        assert str(obj) == '{}({})'.format(obj.__class__.__name__, DEFAULTS[self.name][0])
        assert repr(obj) == '{}({})'.format(obj.__class__.__name__, DEFAULTS[self.name][0])

class TestNumerics(unittest.TestCase):
    typ = None
    name = None

    funcs = [
            ('add', '+'),
            ('sub', '-'),
            ('mul', '*'),
            ('div', '+'),
            ]

    if sys.version_info[0] < 3:
        funcs.append(('div', '/'))
    else:
        funcs.extend([
            ('floordiv', '//'),
            ('truediv', '/'),
            ])

    for (basename, op) in funcs:
        name = "test_{}".format(basename)
        code = '''
def {}(self):
    mut_a = self.typ(DEFAULTS[self.name][0])
    mut_b = self.typ(DEFAULTS[self.name][1])
    prim_a = DEFAULTS[self.name][0]
    prim_b = DEFAULTS[self.name][1]

    assert mut_a {op} mut_b == prim_a {op} prim_b
    assert mut_b {op} mut_a == prim_b {op} prim_a

    assert mut_a {op} prim_b == prim_a {op} prim_b
    assert prim_b {op} mut_a == prim_b {op} prim_a

    mut_a {op}= mut_b
    assert mut_a.get() == prim_a {op} prim_b
        '''.format(name, op=op)
        code = compile(code, "<string>", "exec")
        locals()[name] = FunctionType(code.co_consts[0], globals(), name)
        del code, name, op

types = [
        ("bool", Bool),
        ("str", Str),
        ]

num_types = [
        ("int", Int),
        ("float", Float),
        ]

types += num_types


for typ in types:
    name = "Test{}Basic".format(typ[0])
    attrs = {'__test__': True, "name": typ[0], "typ": typ[1]}
    globals()[name] = type(name, (TestBasic,), attrs)
del typ
del globals()["TestBasic"]

for typ in num_types:
    name = "Test{}Numerics".format(typ[0])
    attrs = {'__test__': True, "name": typ[0], "typ": typ[1]}
    globals()[name] = type(name, (TestNumerics,), attrs)
del typ
del globals()["TestNumerics"]
