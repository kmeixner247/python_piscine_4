def mean(args):
    """Returns the mean value of the number set. Calculated by dividing the \
total sum of all numbers by the number of elements.

    Args:
        - args(list): The list of numbers to compute.

    Returns:
        - the computed mean value as a number

    Raises:
        None

    Example:
        mean([1, 5, 12]) = (1 + 5 + 12) / 3 = 6
"""
    return sum(args) / len(args)


def median(args):
    """Returns the median value of the number set. The median is defined as the
middle value of the ordered elements. If the number of elements is even, the \
median is the mean value of the two middle values.

    Args:
        - args(list): The list of numbers to compute.

    Returns:
        - the median value as a number

    Raises:
        None

    Examples:
        median([1, 5, 12]) = 5
        median([5, 2, 9, 18]) = median([2, 5, 9, 18]) = mean(5, 9) = 7
"""
    lst = sorted(args)
    if (len(lst)) % 2 == 1:
        return lst[int(len(lst)/2)]
    else:
        return (lst[int(len(lst)/2)] + lst[int(len(lst)/2-1)])/2


def quartile(args):
    """Returns the lower (25%) and upper (75%) quartiles of the number set. \
The quartiles are defined as the mean value of the lower or upper half of the \
sorted number set. If the number of elements is odd, the middle element is \
part of both halves.

    Args:
        - args(list): The list of numbers to compute.

    Returns:
        - the lower and upper quartiles as numbers in a list

    Raises:
        None

    Examples:
        quartile([1, 5, 12]) = [mean([1, 5]), mean(5, 12)] = [3.0, 8.5]
        quartile([5, 2, 9, 18]) = [mean([2, 5]), mean([9, 18])] = [3.5, 13.5]
"""
    lst = sorted(args)
    mid = len(lst) // 2
    if len(lst) % 2 == 1:
        return [mean(lst[:mid+1]), mean(lst[mid:])]
    else:
        return [mean(lst[:mid]), mean(lst[mid:])]


def std(args):
    """Returns the standard deviation of the data set. The standard deviation \
is defined as the average distance of all values to the mean. This is \
calculated as the square root of the sum of the squared distance to the mean \
of all elements divided by the number of elements.

    Args:
        - args(list): The list of numbers to compute.

    Returns:
        - the calculated standard deviation as a number

    Raises:
        None

    Example:
        - std([1, 5, 12]):
            - mean([1, 5, 12]) = 6
            - (1 - 6)**2 + (5 - 6)**2 + (12 - 6)**2 = 25 + 1 + 36 = 62
            - 62 / 3 = 20.667
            - 20.667 ** 0.5 = 4.643
"""
    m = mean(args)
    return (sum((n-m)**2 for n in args) / len(args)) ** 0.5


def var(args):
    """Returns the variance of the data set. The variance is defined as the \
squared average distance of all values to the mean. This is calculated as the \
sum of the squared distance to the mean of all elements divided by the number \
of elements.

    Args:
        - args(list): The list of numbers to compute.

    Returns:
        - the calculated variance as a number

    Raises:
        None

    Example:
        - std([1, 4, 12]):
            - mean([1, 5, 12]) = 6
            - (1 - 6)**2 + (5 - 6)**2 + (12 - 6)**2 = 25 + 1 + 36 = 62
            - 62 / 3 = 20.667
"""
    m = mean(args)
    return (sum((n-m)**2 for n in args) / len(args))


def ft_statistics(*args: int | float, **kwargs: str) -> None:
    """Prints statistics about the provided set of numbers based on the \
provided keywords.

    Args:
        - *args(int | float): list of numbers to be analyzed
        - **kwargs(str): list of keywords to specify which statistics to print
        - Supported keywords:
            - 'mean': The mean value of the number set
            - 'median': The median value of the number set
            - 'quartile': The lower (25%) and upper (75%) quartiles of the \
number set
            - 'std': The standard deviation of the number set
            - 'var': the variance of the data set

    Returns:
        None
"""
    funcs = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
    }
    for n in kwargs:
        try:
            keyword = funcs.get(kwargs[n])
            if keyword is not None:
                print(f"{kwargs[n]} : {keyword(args)}")
        except Exception as msg:
            print(f"ft_statistics: {type(msg).__name__}: {msg}")
