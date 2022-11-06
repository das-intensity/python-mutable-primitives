''' Str - A mutable str class '''
from mutable_primitives.base import Mutable


class Str(Mutable):
    ''' Str - A mutable str class '''
    base = str

    def __init__(self, val):
        super(Str, self).__init__(val, self.base)  # pylint: disable=super-with-arguments
        self.val = val

    def get(self):
        ''' get raw (primitive value '''
        return self.val

    def set(self, val):
        ''' set raw (primitive) value '''
        assert isinstance(val, self.base)
        self.val = val

    def __eq__(self, other):
        return self.val == other

    def __ne__(self, other):
        return self.val != other

    def __bool__(self):
        ''' boolean test for python3 '''
        if self.val:
            return True
        return False

    def __add__(self, other):
        return self.val + other

    def __mul__(self, other):
        return self.val * other

    def __iadd__(self, other):
        self.val += other
        return self

    def __imul__(self, other):
        self.val *= other
        return self

    def __radd__(self, other):
        return other + self.val

    def __rmul__(self, other):
        return other * self.val
