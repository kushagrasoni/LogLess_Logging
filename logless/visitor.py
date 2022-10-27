import ast

global parent_level, child_counter


class RecursiveVisitor(ast.NodeVisitor):
    """ example recursive visitor """

    def recursive(func):
        """ decorator to make visitor work recursive """
        global parent_level, child_counter

        def wrapper(self, node):
            global child_counter, parent_level
            # print(f'Parent Level : {parent_level}')
            child_counter = 0
            parent_level = 0
            func(self, node)
            for child in ast.iter_child_nodes(node):
                # print(f'\tChild Counter : {child_counter}')
                self.visit(child)
                parent_level += 1
            print("\n\n")

        return wrapper

    @recursive
    def visit_Assign(self, node):
        """ visit a Assign node and visits it recursively"""
        global child_counter
        child_counter += 1
        print(parent_level, child_counter, type(node).__name__, node.value)

    @recursive
    def visit_BinOp(self, node):
        global child_counter
        child_counter += 1
        """ visit a BinOp node and visits it recursively"""
        print(parent_level, child_counter, type(node).__name__)

    @recursive
    def visit_Call(self, node):
        global child_counter
        child_counter += 1
        """ visit a Call node and visits it recursively"""
        print(parent_level, child_counter, type(node).__name__)

    @recursive
    def visit_Lambda(self, node):
        global child_counter
        child_counter += 1
        """ visit a Function node """
        print(parent_level, child_counter, type(node).__name__)

    @recursive
    def visit_FunctionDef(self, node):
        global child_counter
        child_counter += 1
        """ visit a Function node and visits it recursively"""
        print(parent_level, child_counter, type(node).__name__)

    @recursive
    def visit_Module(self, node):
        global child_counter
        child_counter += 1
        """ visit a Module node and the visits recursively"""
        pass

    @recursive
    def visit_Num(self, node):
        global child_counter
        child_counter += 1
        """ visit a Num node and visits it recursively"""
        print(parent_level, child_counter, type(node).__name__, node.__dict__['value'])

    @recursive
    def visit_Str(self, node):
        global child_counter
        child_counter += 1
        """ visit a Str node and visits it recursively"""
        print(parent_level, child_counter, type(node).__name__, node.s)

    @recursive
    def visit_Constant(self, node):
        global child_counter
        child_counter += 1
        """ visit a Str node and visits it recursively"""
        print(parent_level, child_counter, type(node).__name__, node.value)

    @recursive
    def visit_Name(self, node):
        global child_counter
        child_counter += 1
        """ visit a Str node and visits it recursively"""
        print(parent_level, child_counter, type(node).__name__, node.id)

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
        print(parent_level, child_counter, type(node).__name__)

    def visit_BinOp(self, node):
        """ visit a BinOp node """
        print(parent_level, child_counter, type(node).__name__)

    def visit_Call(self, node):
        """ visit a Call node """
        print(parent_level, child_counter, type(node).__name__)

    def visit_Lambda(self, node):
        """ visit a Function node """
        print(parent_level, child_counter, type(node).__name__)

    def visit_FunctionDef(self, node):
        """ visit a Function node """
        print(parent_level, child_counter, type(node).__name__)

    @recursive
    def visit_Module(self, node):
        """ visit a Module node and the visits recursively, otherwise you
        wouldn't see anything here"""
        pass

    def generic_visit(self, node):
        pass
