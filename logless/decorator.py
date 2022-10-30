import inspect


from logless.lister import Lister
from logless.logger import logger
from logless.node_visitor import NodeVisitor
from logless.patterns import get_patterns
from logless.create import get_log
from logless.categorizer import *
import ast

from logless.visitor import RecursiveVisitor, SimpleVisitor


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
        func(*args, **kwargs)
        source_code = inspect.getsource(func)
        # print(f'Func Attributes:\n {dir(func)}')
        # print(f'Func Globals:\n {func.__globals__}')
        parsed_funct = ast.parse(source_code)

        f = open('../output/ast.txt', 'w')

        # print(func_ast)
        f.writelines(ast.dump(parsed_funct, indent=4))
        f.close()

        print("Args:")
        # for item in args:
        #     print(f'\t{type(item)}')
        #     print(f'\t{item}')

        print("kwargs:")
        # for item in kwargs:
        #     print(f'\t{item}')

        ######### METHOD 1
        # print("PARENT NODE: ", type(parsed_funct).__name__)
        # for child in ast.iter_child_nodes(parsed_funct):
        #     print("CHILD NODE", child)

        # Lister().visit(parsed_funct)

        ######### METHOD 2
        recursive_visitor = RecursiveVisitor()
        print('\nvisit recursive\n')
        recursive_visitor.visit(parsed_funct)

        # print('\nvisit simple\n')
        # simple_visitor = SimpleVisitor()
        # simple_visitor.visit(parsed_funct)

        ######### METHOD 3
        # import symtable
        # from io import StringIO
        # from tokenize import generate_tokens, untokenize, INDENT
        # source_code = _dedent(source_code)
        # SymbolTable = symtable.symtable(source_code, 'string', 'exec')
        # v = NodeVisitor(SymbolTable)
        # v.visit(parsed_funct)
        # _dedent borrowed from the myhdl package (www.myhdl.org)
        # def _dedent(s):
        #     """Dedent python code string."""
        #
        #     result = [t[:2] for t in generate_tokens(StringIO(s).readline)]
        #     # set initial indent to 0 if any
        #     if result[0][0] == INDENT:
        #         result[0] = (INDENT, '')
        #     return untokenize(result)

        # lines = source_code.split('\n')
        # for index in range(1, len(lines) - 1):
        #     assign = func_ast.body
        #     # print(assign)
        #     # print(f'Line:: {lines[index]}... Variable {assign.targets[0].id}.... Value {assign.value.n}')
        #     line = lines[index].strip()  # needs alog for determining the indentation for various logics
        #
        #     # Filtering out the unwanted lines like Comments and decorators of Function declarations
        #     if line and (line[0] not in ['#', '@']) and not line.startswith('def'):
        #         pattern = get_patterns(line)
        #         log_statement = get_log(pattern)
        #         # logger.info(log_statement + str(type(line)))
        #         print(line)

        print('\nEverything below this is App Output:')
        return func(*args, **kwargs)

    # print(f'Arg1:: {func.arg1}')
    return getcode

