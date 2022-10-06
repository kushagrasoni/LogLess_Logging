from logless.decorator import log_deco
import requests


@log_deco
def foo():
    arg1 = 1
    arg2 = 2
    a = arg1 + arg2
    var = 5
    b = a * var
    return a + b


print(foo())
