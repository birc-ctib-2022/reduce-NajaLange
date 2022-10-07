"""Reduce and accumulate module"""

from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')


def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    """
    assert len(x) >= 2
    val = f(x[0], x[1])
    for y in x[2:]:
        val = f(val, y)
    return val

#print(reduce(lambda x,y: x+y, [1, 2, 3]))
#print(reduce(lambda x,y: x*y, [1, 2, 4]))


def accumulate(f: Callable[[A], A], x: list[A]) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3])
    [1, 3, 6]
    """
    assert len(x) >= 2
    val = f(x[0], x[1])
    lst = [x[0], val]
    for y in x[2:]:
        val = f(val, y)
        lst.append(val)

    return lst

#print(accumulate(lambda x,y: x+y, [1, 2, 3]))
