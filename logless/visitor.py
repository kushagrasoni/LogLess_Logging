import ast

global parent_level, child_counter


class RecursiveVisitor(ast.NodeVisitor):
    """ example recursive visitor """

    def recursive(func):
        """ decorator to make visitor work recursive """
        global parent_level, child_counter
        parent_level = 0

        def wrapper(self, node):
            global child_counter, parent_level
            # print(f'Parent Level : {parent_level}')
            child_counter = 0

            func(self, node)
            print("PARENT NODE: ", parent_level, type(node).__name__)
            for child in ast.iter_child_nodes(node):
                # print(f'\tChild Counter : {child_counter}')
                print("CHILD NODE", child)
                self.visit(child)

            print("\n\n")
            parent_level += 1

        return wrapper

    @recursive
    def visit_Assign(self, node):
        """ visit a Assign node and visits it recursively"""
        print(type(node).__name__, node.value)

    @recursive
    def visit_BinOp(self, node):
        """ visit a BinOp node and visits it recursively"""
        print(type(node).__name__)

    @recursive
    def visit_Call(self, node):
        """ visit a Call node and visits it recursively"""
        print(type(node).__name__)

    @recursive
    def visit_Lambda(self, node):
        """ visit a Function node """
        print(type(node).__name__)

    @recursive
    def visit_FunctionDef(self, node):
        """ visit a Function node and visits it recursively"""
        print(type(node).__name__)

    @recursive
    def visit_Module(self, node):
        """ visit a Module node and the visits recursively"""
        pass

    @recursive
    def visit_arguments(self, node):
        """ visit a Arguments node and visits it recursively"""
        print(type(node).__name__)

    @recursive
    def visit_arg(self, node):
        """ visit a Arg node and visits it recursively"""
        print(type(node).__name__, node.__dict__['arg'])

    @recursive
    def visit_Num(self, node):
        global child_counter
        child_counter += 1
        """ visit a Num node and visits it recursively"""
        print(type(node).__name__, node.__dict__['value'])

    @recursive
    def visit_Str(self, node):
        """ visit a Str node and visits it recursively"""
        print(type(node).__name__, node.s)

    @recursive
    def visit_Constant(self, node):
        """ visit a Str node and visits it recursively"""
        print(type(node).__name__, node.value)

    @recursive
    def visit_Name(self, node):
        """ visit a Str node and visits it recursively"""
        print(type(node).__name__, node.id)

    def generic_visit(self, node):
        ast.NodeVisitor.generic_visit(self, node)


class SimpleVisitor(ast.NodeVisitor):
    """ simple visitor for comparison """

    def recursive(func):
        """ decorator to make visitor work recursive """

        def wrapper(self, node):
            func(self, node)
            for child in ast.iter_child_nodes(node):
                self.visit(child)

        return wrapper

    def visit_Assign(self, node):
        """ visit a Assign node """
        print(type(node).__name__)

    def visit_BinOp(self, node):
        """ visit a BinOp node """
        print(type(node).__name__)

    def visit_Call(self, node):
        """ visit a Call node """
        print(type(node).__name__)

    def visit_Lambda(self, node):
        """ visit a Function node """
        print(type(node).__name__)

    def visit_FunctionDef(self, node):
        """ visit a Function node """
        print(type(node).__name__)

    @recursive
    def visit_Module(self, node):
        """ visit a Module node and the visits recursively, otherwise you
        wouldn't see anything here"""
        pass

    def generic_visit(self, node):
        pass
