import dis
import inspect

import ast
import linecache
from pprint import pprint
from sys import settrace

import pysnooper

from Scalpel.scalpel.cfg import CFGBuilder


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

    def getcode(*args, **kwargs):
        with pysnooper.snoop(depth=1):
            func(*args, **kwargs)
        # source_code = inspect.getsource(func)
        # parsed_funct = ast.parse(source_code)
        #
        # f = open('../output/ast.txt', 'w')
        #
        # f.writelines(ast.dump(parsed_funct, indent=4))
        # f.close()

        # dis.dis(func)
        # it = dis.get_instructions(func)
        # for i in it:
        #     print(i)

        # """ASTVisitor Subclassed using ast.NodeVisitor and overridden various visit_<node> methods and generic_visit
        # method """
        # from logless.visitor import ASTVisitor
        # ast_visitor = ASTVisitor()
        # print('\nvisit recursive\n')
        # ast_visitor.visit(parsed_funct)
        # pprint(f'\n\n\n\nFINAL RESULT LIST:\n')
        # pprint(ast_visitor.result_list)
        # print('\nEverything below this is App Output:')

        # cfg = CFGBuilder().build_from_src(src=source_code, name='logless')
        #
        # for item in cfg.__iter__():
        #     print(item)

        # for block in cfg:
        #     # print(dir(block))
        #     # print(block.__str__)
        #     print(block.get_source())
        #     print(block.func_calls)
        #     # print(block.statements)
        #     calls = block.get_calls()
        #     # print(dir(calls))
        #     # print(calls)

        return func(*args, **kwargs)

    # print(f'Arg1:: {func.arg1}')
    return getcode


def traceit(frame, event, arg):
    print(event)
    # if event == "line":
    #     lineno = frame.f_lineno
    #     filename = frame.f_globals["__file__"]
    #     # if (filename.endswith(".pyc") or
    #     #         filename.endswith(".pyo")):
    #     #     filename = filename[:-1]
    #     name = frame.f_globals["__name__"]
    #     line = linecache.getline(filename, lineno)
    #     print("%s:%s: %s" % (name, lineno, line.rstrip()))
    return traceit

# def traceit(frame, event, arg):
#     lineno = frame.f_lineno
#     filename = frame.f_globals["__file__"]
#     print("file %s line %d" % (filename, lineno))
#     return traceit
