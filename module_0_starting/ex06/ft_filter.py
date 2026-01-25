from collections.abc import Callable, Iterable, Iterator
from typing import Any


def ft_filter(func: Callable | None, data: Iterable[Any]) -> Iterator[Any]:
    """
    Filters elements in an iterable for which the function returns True.

    Args:
        func (Optional[Callable]): A function that takes one argument and
            returns a boolean. If None, the bool() function is used.
        data (Iterable): The iterable to filter.

    Returns:
        Iterator: An iterator over elements for which func returns True.
    """
    if func is None:
        func = bool

    # return (item for item in data if func(item)) -> This solution is better
    # because avoid use of lists, but subject requires list comprehensions
    return (element for element in [item for item in data if func(item)])
