def square(x: int | float) -> int | float:
    """Calculates the square of the provided argument

    Args:
        - x: number to be squared

    Returns:
        - the square value of x

    Raises:
        None
"""
    return x**2


def pow(x: int | float) -> int | float:
    """Calculates the provided argument to the power of itself

    Args:
        - x: number to be computed

    Returns:
        - x to the power of x

    Raises:
        None
"""
    return x**x


def outer(x: int | float, function) -> object:
    """Wrapper function that returns an inner function, which applies \
the provided function on the provided parameter x on every call of the \
returned function object.

    Args:
        - x(int | float): a number that serves as the input parameter for \
the provided function
        - function(function): a function to be applied on x

    Returns:
        A function object that applies function on x iteratively on every call\

    Raises:
        None
"""
    count = 0

    def inner() -> float:
        """Applies the provided function on the iteratd input value and \
returns the result

    Args:
        None

    Returns:
        The result of function(x).

    Raises:
        None
"""
        nonlocal x, count
        x = function(x)
        count += 1
        return x
    return inner
