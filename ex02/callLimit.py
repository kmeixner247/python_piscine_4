def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.

    Args:
        - limit(int): limit for how often the decorated function can be called

    Returns:
        - A function object that can be used as a decorator to limit the
        number of times a function can be called

    Raises:
        None
    """
    count = 0

    def callLimiter(function):
        """
        Returns a wrapper function that limits the number of times the
        decorated function can be called.

        Args:
            - function: The function to be decorated.

        Returns:
            A new function object that wraps the original function so it can
            only be called a limited number of times.

        Raises:
            None
        """
        def limit_function(*args: any, **kwds: any):
            """
            Wrapper function that limits the number of times the decorated
            function can be called

            Args:
                - *args: any positional arguments passed to the decorated function
                - **kwds: any keyword arguments passed to the decorated function

            Returns:
                None

            Raises:
                None
            """
            nonlocal count
            count += 1
            if (count > limit):
                print("Error:", function, "call too many times")
            else:
                function(*args, **kwds)
        return limit_function
    return callLimiter
