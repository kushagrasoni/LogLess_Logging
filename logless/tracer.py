import collections
import opcode
import traceback

from logless import utils
from logless.profile import Profile
from conf.config import INFO, ERROR
from logless.generator import Generator
from conf.config import MAXIMUM_VARIABLE_LEN
from logless.utils import get_local_result

class Tracer:
    def __init__(self, func_name, mode=None, file_type=None):
        self.final_result = collections.OrderedDict()
        self.frame_to_local_result = {}
        self.func_name = func_name
        self.mode = mode
        # clear temporary file used to store session logs
        with open("logless.txt","w") as f:
            f.write('')
        self.file_type = file_type

    # Trace function which returns itself
    def tracer(self, frame, event, arg=None):
        generator = Generator(self.mode, self.file_type)
        function_name = frame.f_code.co_name
        if function_name == self.func_name:
            old_local_reprs = self.frame_to_local_result.get(frame, {})
            self.frame_to_local_result[frame] = self.final_result = get_local_result(frame)

            assign_type = ('Starting Variable' if event == 'call' else
                           'Initializing Variable')
            for var_name, var_value in self.final_result.items():
                if var_name not in old_local_reprs:
                    profile = Profile(event, assign_type, var_name, var_value, INFO)
                    generator.add_profile(profile)

                elif old_local_reprs[var_name] != var_value:
                    assign_type = 'Updated Variable'
                    profile = Profile(event, assign_type, var_name, var_value, INFO)
                    generator.add_profile(profile)

            code_byte = frame.f_code.co_code[frame.f_lasti]
            if not isinstance(code_byte, int):
                code_byte = ord(code_byte)
            ended_by_exception = (
                    event == 'return'
                    and arg is None
                    and (opcode.opname[code_byte]
                         not in ('RETURN_VALUE', 'YIELD_VALUE'))
            )

            # Return in case of Call ending in exception
            if ended_by_exception:
                self.frame_to_local_result.pop(frame, None)
                return_value = None
                assign_type = f'Function "{self.func_name}" Ended with Exception'
                var_name = ''
                profile = Profile(event, assign_type, var_name, return_value, ERROR)
                generator.add_profile(profile)
            if event == 'return' and not ended_by_exception:
                self.frame_to_local_result.pop(frame, None)
                return_value = arg
                assign_type = f'Function "{self.func_name}" returns'
                var_name = ''
                profile = Profile(event, assign_type, var_name, return_value, INFO)
                generator.add_profile(profile)
            if event == 'exception':
                exception = '\n'.join(traceback.format_exception_only(*arg[:2])).strip()
                if MAXIMUM_VARIABLE_LEN:
                    exception = utils.truncate(exception, MAXIMUM_VARIABLE_LEN)
                assign_type = f'Exception Encountered'
                var_name = ''
                profile = Profile(event, assign_type, var_name, exception, ERROR)
                generator.add_profile(profile)
            if self.file_type == 'txt':
                generator.log()
            elif self.file_type == 'pdf':
                generator.print_to_pdf()
            else:
                generator.log()

            return self.tracer
        return None
