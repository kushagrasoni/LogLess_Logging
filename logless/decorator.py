import collections

from sys import settrace
from logless.event import Event
from conf.config import INFO
from logless.generator import Generator
from logless.log_output import LogGenerator

final_result = collections.OrderedDict()
frame_to_local_reprs = {}
func_name = None

generator = Generator()


def log(func, output_format = 'terminal'):
    """
    This is the decorator which will be used by any function in the application code.
    This decorator is to bused in the following format:

    SYNTAX:
        @log\n
        def function(**args):
            do something\n
            return something

    :param func: The input is the function to which decorator is used upon
    :return: The output of the function (if any)
    """
    global func_name, log_event
    func_name = func.__name__

    def getcode(*args, **kwargs):
        print(args)
        settrace(my_tracer)
        return func(*args, **kwargs)
    return getcode


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


# local trace function which returns itself
def my_tracer(frame, event, arg=None):
    log_generator = LogGenerator()
    function_name = frame.f_code.co_name
    global final_result, frame_to_local_reprs, log_event
    if function_name == func_name:
        old_local_reprs = frame_to_local_reprs.get(frame, {})
        frame_to_local_reprs[frame] = final_result = get_local_reprs(frame)

        assign_type = ('Starting Variable' if event == 'call' else
                       'Initializing Variable')
        for var_name, var_value in final_result.items():
            if var_name not in old_local_reprs:
                e = Event(event, assign_type, var_name, var_value, INFO)
                log_generator.add_event(e)

            elif old_local_reprs[var_name] != var_value:
                assign_type = 'Updated Variable'
                e = Event(event, assign_type, var_name, var_value, INFO)
                log_generator.add_event(e)
        if event == 'return':
            frame_to_local_reprs.pop(frame, None)
            return_value = arg
            assign_type = f'Function {func_name} returns'
            var_name = ''
            e = Event(event, assign_type, var_name, var_value, INFO)
            log_generator.add_event(e)
        log_generator.print_to_terminal()
        #log_generator.print_to_txt()
        return my_tracer
    return None

