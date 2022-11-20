import functools, types

class MyDecoratorClass:
    __obj_dict__ = {}
    def __init__(self, method, name="unknown") -> None:
        functools.update_wrapper(self, method)
        self.method = method
        self.method_name = name
        return

    def __get__(self, obj, objtype) -> object:
        if obj in MyDecoratorClass.__obj_dict__.keys():
            # Return existing MyDecoratorClass() instance for
            # the given object-method_name combination, and make
            # sure it holds a bound method.
            if self.method_name in MyDecoratorClass.__obj_dict__[obj].keys():
                m = MyDecoratorClass.__obj_dict__[obj][self.method_name]
                return m
            else:
                # Create a new MyDecoratorClass() instance WITH a bound
                # method, and store it in the dictionary.
                m = type(self)(self.method.__get__(obj, objtype), self.method_name)
                MyDecoratorClass.__obj_dict__[obj][self.method_name] = m
                return m

        # Create a new MyDecoratorClass() instance WITH a bound
        # method, and store it in the dictionary.
        m = type(self)(self.method.__get__(obj, objtype), self.method_name)
        MyDecoratorClass.__obj_dict__[obj] = {}
        MyDecoratorClass.__obj_dict__[obj][self.method_name] = m
        return m

    def __call__(self, *args, **kwargs) -> object:
        return self.method(*args, **kwargs)


    def __del__(self):
        print(f"{id(self)} garbage collected!")


def my_wrapper(name="unknown"):
    def _my_wrapper_(method):
        return MyDecoratorClass(method, name)
    return _my_wrapper_
