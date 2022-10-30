from logless import log


@log
def foo():
    arg1 = 1
    arg2 = 2
    a = arg1 + arg2
    var = 5
    b = a * var
    return a + b


print(foo())