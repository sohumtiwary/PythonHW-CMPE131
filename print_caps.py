from functools import wraps

def allcaps(fn):
    @wraps(fn)
    def inner():
        output = fn()  # target function takes no parameters
        if isinstance(output, str):
            return output.upper()
        return output
    return inner
