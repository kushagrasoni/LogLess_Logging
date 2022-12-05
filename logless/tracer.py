import collections
from logless.event import Event
from conf.config import INFO
from logless.log_output import LogGenerator


class Tracer:
    def __init__(self, func_name, mode=None):
        self.final_result = collections.OrderedDict()
        self.frame_to_local_result = {}
        self.func_name = func_name
        self.mode = mode
        # generator = Generator()

    @staticmethod
    def get_local_result(frame):
        code = frame.f_code
        vars_order = (code.co_varnames + code.co_cellvars + code.co_freevars +
                      tuple(frame.f_locals.keys()))

        result_items = [(key, value)
                        for key, value in frame.f_locals.items()]

        result_items.sort(key=lambda key_value: vars_order.index(key_value[0]))

        result = collections.OrderedDict(result_items)

        return result

    # local trace function which returns itself
    def tracer(self, frame, event, arg=None):
        log_generator = LogGenerator(self.mode)
        function_name = frame.f_code.co_name
        if function_name == self.func_name:
            old_local_reprs = self.frame_to_local_result.get(frame, {})
            self.frame_to_local_result[frame] = self.final_result = self.get_local_result(frame)

            assign_type = ('Starting Variable' if event == 'call' else
                           'Initializing Variable')
            for var_name, var_value in self.final_result.items():
                if var_name not in old_local_reprs:
                    e = Event(event, assign_type, var_name, var_value, INFO)
                    log_generator.add_event(e)

                elif old_local_reprs[var_name] != var_value:
                    assign_type = 'Updated Variable'
                    e = Event(event, assign_type, var_name, var_value, INFO)
                    log_generator.add_event(e)
            if event == 'return':
                self.frame_to_local_result.pop(frame, None)
                return_value = arg
                assign_type = f'Function "{self.func_name}" returns'
                var_name = ''
                e = Event(event, assign_type, var_name, return_value, INFO)
                log_generator.add_event(e)
            log_generator.print_to_terminal()

            return self.tracer
        return None
