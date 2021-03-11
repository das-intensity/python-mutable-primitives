import unittest

from mutable_primitives import (
        Int,
        )


class TestInt(unittest.TestCase):
    def test_eq(self):
        assert Int(5) == Int(5)
        assert Int(5) == 5
        assert 5 == Int(5)

        assert Int(5) != 6
        assert 6 != Int(5)
