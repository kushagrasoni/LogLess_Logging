import collections

from sys import settrace

# from fpdf import FPDF
from logless.generator import LogEvent, Generator

final_result = collections.OrderedDict()
frame_to_local_reprs = {}
func_name = None

# log_event = LogEvent()
generator = Generator()


# event
# event
# event type 
# colour
# text

def log(func):
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
        settrace(my_tracer)
        return func(*args, **kwargs)

    # print(f'Arg1:: {func.arg1}')
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
    function_name = frame.f_code.co_name
    global final_result, frame_to_local_reprs, log_event
    if function_name == func_name:
        old_local_reprs = frame_to_local_reprs.get(frame, {})
        frame_to_local_reprs[frame] = final_result = get_local_reprs(frame)

        assign_type = ('Starting var:.. ' if event == 'call' else
                       'New var:....... ')
        for var_name, var_value in final_result.items():
            if var_name not in old_local_reprs:
                # log_event.generate(event, f'{event}->{newish_string}{var_name} = {var_value}')
                # log_event = LogEvent(event,f'{event}->{newish_string}{var_name} = {var_value}')
                # print(f'{event}->{assign_type}{var_name} = {var_value}')
                generator.log(event, assign_type, var_name, var_value)

            elif old_local_reprs[var_name] != var_value:
                assign_type = 'Modified var:..'
                # print(f'{event}->Modified var:.. {assign_type}{var_name} = {var_value}')
                generator.log(event, assign_type, var_name, var_value)
        if event == 'return':
            frame_to_local_reprs.pop(frame, None)
            return_value = arg
            assign_type = 'Return value:..'
            var_name = 'return'
            # print(f'{event}-> {assign_type} {return_value}')
            generator.log(event, assign_type, var_name, return_value)
        # print(SetColor(event,'blue'))
        return my_tracer
    return None

    # Event
    # - name 
    # - type 
    # - text 
    # - colour 


def pdf_print():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 10, txt="LogLess", ln=1, align='C')
    pdf.output("logless.pdf")
