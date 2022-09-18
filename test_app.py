from logless.decorator import log


@log
def foo(arg1, arg2):
    a = arg1 + arg2
    return a


print(foo(1, 2))
