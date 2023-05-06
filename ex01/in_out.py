def square(x: int | float) -> int | float:
    """square"""
    return x**2


def pow(x: int | float) -> int | float:
    """pow"""
    return x**x


def outer(x: int | float, function) -> object:
    """outer"""
    count = x
    def inner() -> float:
        """inner"""
        nonlocal count
        count = function(count)
        return count
    return inner