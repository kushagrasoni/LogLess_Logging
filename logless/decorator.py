import inspect

import ast


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
        parsed_funct = ast.parse(source_code)

        f = open('../output/ast.txt', 'w')

        f.writelines(ast.dump(parsed_funct, indent=4))
        f.close()

        """ASTVisitor Subclassed using ast.NodeVisitor and overridden various visit_<node> methods and generic_visit 
        method """
        from logless.visitor import ASTVisitor
        ast_visitor = ASTVisitor()
        print('\nvisit recursive\n')
        ast_visitor.visit(parsed_funct)

        print('\nEverything below this is App Output:')
        return func(*args, **kwargs)

    # print(f'Arg1:: {func.arg1}')
    return getcode

