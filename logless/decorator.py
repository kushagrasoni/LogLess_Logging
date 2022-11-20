import collections

from sys import settrace
from fpdf import FPDF


final_result = collections.OrderedDict()
frame_to_local_reprs = {}
func_name = None

#event
#event 
# event type 
#colour
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
    global func_name
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
    global final_result, frame_to_local_reprs
    if function_name == func_name:
        old_local_reprs = frame_to_local_reprs.get(frame, {})
        frame_to_local_reprs[frame] = final_result = get_local_reprs(frame)

        newish_string = ('Starting var:.. ' if event == 'call' else
                         'New var:....... ')
        for name, value_repr in final_result.items():
            if name not in old_local_reprs:
                log_event = LogEvent(event,f'{event}->{newish_string}{name} = {value_repr}')
                print(log_event)
            elif old_local_reprs[name] != value_repr:
                print(f'{event}->Modified var:.. {newish_string}{name} = {value_repr}')
        if event == 'return':
            frame_to_local_reprs.pop(frame, None)
            return_value_repr = arg
            print(f'{event}->Return value:.. {return_value_repr}')
        # print(SetColor(event,'blue'))
        return my_tracer
    return None


    # Event 
    # - name 
    # - type 
    # - text 
    # - colour 


class LogEvent():
    def __init__(self, event_type, event_text):
        self.event_type = event_type
        self.event_text = event_text
        self.type_color_map = {
            'line':'white',
            'call':'blue'
        }
        self.color_map = {'black' : "\u001b[30m",
                    'red' : "\u001b[31m",
                    'green' : "\u001b[32m",
                    'yellow' : "\u001b[33m",
                    'blue' : "\u001b[34m",
                    'magenta' : "\u001b[35m",
                    'cyan' : "\u001b[36m",
                    'white' : "\u001b[37m",
                    'none':''
        }

    def color_code(self):
        return self.color_map[self.type_color_map[self.event_type]]
    
    def __str__(self):
        return f'{self.color_code()}{self.event_text}'



class  SetColor():
    def __init__(self, text, color  = 'none'):
        self.text = text
        self.color = color
        self.color_map = {'black' : "\u001b[30m",
                    'red' : "\u001b[31m",
                    'green' : "\u001b[32m",
                    'yellow' : "\u001b[33m",
                    'blue' : "\u001b[34m",
                    'magenta' : "\u001b[35m",
                    'cyan' : "\u001b[36m",
                    'white' : "\u001b[37m",
                    'none':''
    }

    def color_code(self):
        return self.color_map[self.color]
    
    def __str__(self):
        return f'{self.color_code()}{self.text}'


    


def pdf_print():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 20)
    pdf.cell(200, 10, txt = "LogLess",ln = 1, align = 'C')
    pdf.output("logless.pdf")  


