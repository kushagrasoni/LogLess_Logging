from trash.myDecorator_ref import my_wrapper


@my_wrapper("foo")
def foo(self):
    print(f"foo!")


@my_wrapper("bar")
def bar(self):
    print("bar!")
