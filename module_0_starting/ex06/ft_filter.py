from typing import Optional, Callable, Iterable, Iterator


def ft_filter(func: Optional[Callable], data: Iterable) -> Iterator:
    """
    Apply bool functions to every element in Iterable.
    Function passed as parameter must have only 1 argument.

    Params: None/Function, Iterable (list, tuple, set...).

    Returns: Iterator of True elements.
    """
    if func is None:
        func = bool

    # return (item for item in data if func(item)) -> This solution is better
    # because avoid use of lists, but subject requires list comprehensions
    return (element for element in [item for item in data if func(item)])
