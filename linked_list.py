import collections.abc
import enum

class seq(collections.abc.Iterable):

    __slots__ = ()

    def __new__(self, iterable):
        out = Nil
        for elem in iterable:
            out = cons(elem, out)
        return out

class NilType(seq):

    def __new__(cls):
        try:
            return cls._instance
        except AttributeError:
            cls._instance = object.__new__(cls)
            return cls._instance

    def __init__(self):
        return

    def __bool__(self):
        return False

    def __len__(self):
        return 0

    def __iter__(self):
        yield

    def __getitem__(self, index):
        raise IndexError('seq index out of range')

    def __eq__(self, other):
        return self is other

    def __repr__(self):
        return "Nil"

Nil = NilType()

class cons(seq):

    __slots__ = ('_head', '_tail')

    def __new__(cls, head, tail):
        if not isinstance(tail, seq):
            raise TypeError("tail must be an instance of linked list")
        self = object.__new__(cls)
        self._head = head
        self._tail = tail
        return self

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail
    
    def __len__(self):
        try:
            return self._len
        except AttributeError:
            self._len = sum(1 for _ in self)
            return self._len

    def __iter__(self):
        while self is not Nil:
            yield self.head
            self = self.tail

    def __getitem__(self, index):
        for current_index, elem in enumerate(self):
            if index == current_index:
                return elem
        raise IndexError('seq index out of range')

    def __eq__(self, other):
        return isinstance(other, seq) and \
               len(self) == len(other) and \
               all(x==y for x,y in zip(self, other))

    def __repr__(self):
        return 'seq([' + ", ".join(map(str, self)) + '])' 

if __name__ == '__main__':
    x = cons(1, Nil)
