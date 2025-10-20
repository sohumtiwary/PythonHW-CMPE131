import time
from functools import wraps

def timestamp(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        current = time.ctime()  
        print(current)          
        return fn(*args, **kwargs)
    return inner
