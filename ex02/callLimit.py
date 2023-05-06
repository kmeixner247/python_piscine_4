def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            """lol"""
            nonlocal count
            count += 1
            if (count > limit):
                print("Error:", function, "call too many times")
            else:
                function()
            return 
        return limit_function
    return callLimiter