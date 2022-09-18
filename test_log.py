from decorators.logless import logless


@logless
def foo():
    # do something with args
    a = 1 + 2
    print(a)


foo()
