import collections
from sys import settrace

final_result = collections.OrderedDict()
frame_to_local_reprs = {}

def foo():
    arg1 = 5
    arg2 = 2
    if arg1 > arg2:
        a = arg1 - arg2
        c = arg1/arg2
    else:
        a = arg2 - arg1
    var = 5
    b = a * var
    return a + b


# local trace function which returns itself
def my_tracer(frame, event, arg=None):
    function_name = frame.f_code.co_name
    global final_result, frame_to_local_reprs
    if function_name == 'foo':
        old_local_reprs = frame_to_local_reprs.get(frame, {})
        frame_to_local_reprs[frame] = final_result = get_local_reprs(frame)

        newish_string = ('Starting var:.. ' if event == 'call' else
                         'New var:....... ')
        for name, value_repr in final_result.items():
            if name not in old_local_reprs:
                print(f'{event}->{newish_string}{name} = {value_repr}')
            elif old_local_reprs[name] != value_repr:
                print(f'{event}->Modified var:.. {newish_string}{name} = {value_repr}')
        if event == 'return':
            frame_to_local_reprs.pop(frame, None)
            return_value_repr = arg
            print(f'{event}->Return value:.. {return_value_repr}')

        return my_tracer
    return None

    # print(dir(frame))
    # extracts frame code
    # code = frame.f_code

    # print(code.co_consts)
    # dis.disco(code)
    # print(dir(code))
    # print(code)
    # extracts calling function name
    # func_name = code.co_name

    # extracts the line number
    # line_no = frame.f_lineno

    # print(f"A {event} encountered in  {func_name}() at line number {line_no} ")


import sys
import linecache


def get_local_reprs(frame, watch=(), custom_repr=(), max_length=None, normalize=False):
    code = frame.f_code
    vars_order = (code.co_varnames + code.co_cellvars + code.co_freevars +
                  tuple(frame.f_locals.keys()))
    # print(vars_order)
    result_items = [(key, value)
                    for key, value in frame.f_locals.items()]
    # print(result_items)
    result_items.sort(key=lambda key_value: vars_order.index(key_value[0]))
    # result_items.sort()
    result = collections.OrderedDict(result_items)

    for variable in watch:
        result.update(sorted(variable.items(frame, normalize)))
    return result


settrace(my_tracer)

foo()
# # print(f'Output: {foo()}')

# for item in final_result.items():
#     print(item)


# cfg = CFGBuilder().build_from_src(src=inspect.getsource(foo))


# dis.dis(foo)

# Frame
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'f_back', 'f_builtins', 'f_code', 'f_globals', 'f_lasti', 'f_lineno', 'f_locals', 'f_trace', 'f_trace_lines', 'f_trace_opcodes']

# Code
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_posonlyargcount', 'co_stacksize', 'co_varnames', 'replace']


# def traceit(frame, event, arg):
#     print(event)
#     if event == "line":
#         lineno = frame.f_lineno
#         filename = frame.f_globals["__file__"]
#         if (filename.endswith(".pyc") or
#                 filename.endswith(".pyo")):
#             filename = filename[:-1]
#         name = frame.f_globals["__name__"]
#         line = linecache.getline(filename, lineno)
#         print("%s:%s: %s" % (name, lineno, line.rstrip()))
#     return traceit

# def traceit(frame, event, arg):
#     lineno = frame.f_lineno
#     filename = frame.f_globals["__file__"]
#     print("file %s line %d" % (filename, lineno))
#     return traceit

# settrace(traceit)