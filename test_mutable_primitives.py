import sys
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

        assert Int(6) + 5 == 11
        assert 5 + Int(6) == 11
        assert 5 - Int(6) == -1

        assert 5 - Int(6) == 5 - 6
        assert 5 * Int(6) == 5 * 6

        assert 18 / Int(5) == 18 / 5
        if sys.version_info[0] >= 3:
            assert 18 / Int(5) == 18 / 5
