import inspect


def logless(func):
    def getcode():
        func()
        print(inspect.getsource(func))

    return getcode

# def logless(func):
#     def getcode(*args, **kwargs):
#         func(*args, **kwargs)
#         print(inspect.getsource(func))
#
#     return getcode
