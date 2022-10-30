import ast

"""
    A node visitor base class that walks the abstract syntax tree and calls a
    visitor function for every node found.  This function may return a value
    which is forwarded by the `visit` method.

    This class is meant to be subclassed, with the subclass adding visitor
    methods.

    Per default the visitor functions for the nodes are ``'visit_'`` +
    class name of the node.  So a `TryFinally` node visit function would
    be `visit_TryFinally`.  This behavior can be changed by overriding
    the `visit` method.  If no visitor function exists for a node
    (return value `None`) the `generic_visit` visitor is used instead.

    Don't use the `NodeVisitor` if you want to apply changes to nodes during
    traversing.  For this a special visitor exists (`NodeTransformer`) that
    allows modifications.
    """


class ASTVisitor(ast.NodeVisitor):
    """ example recursive visitor """

    def recursive(func):
        """ decorator to make visitor work recursive """
        global parent_level, child_counter
        parent_level = 0

        def wrapper(self, node):
            global child_counter, parent_level
            child_counter = 0

            func(self, node)
            for child in ast.iter_child_nodes(node):
                self.visit(child)

        return wrapper

    @recursive
    def visit_FunctionDef(self, node):
        """ visit a Function node and visits it recursively"""
        print(type(node).__name__, node.__dict__['args'], node.__dict__['body'])

    @recursive
    def visit_arguments(self, node):
        """ visit a Arguments node and visits it recursively"""
        print(type(node).__name__, node.__dict__['args'])

    @recursive
    def visit_arg(self, node):
        """ visit a Arg node and visits it recursively"""
        print(type(node).__name__, node.__dict__['arg'])

    @recursive
    def visit_Expr(self, node):
        """ visit a Assign node and visits it recursively"""
        print(type(node).__name__, node.value)

    @recursive
    def visit_Assign(self, node):
        """ visit a Assign node and visits it recursively"""
        print(
            f'{type(node).__name__}\n\tTotal Targets: {len(node.targets)}\n\tTargets: {node.targets}\n\tValue: {node.value}')

    @recursive
    def visit_BinOp(self, node):
        """ visit a BinOp node and visits it recursively"""
        print(type(node).__name__)

    @recursive
    def visit_Call(self, node):
        """ visit a Call node and visits it recursively"""
        print(
            f'{type(node).__name__}\n\tFunction: {node.func}\n\tTotal Arguments: {len(node.args)}\n\tArguments: {node.args}\n\tKeywords: {node.keywords}')

    @recursive
    def visit_Attribute(self, node):
        """ visit a Assign node and visits it recursively"""
        print(f'{type(node).__name__}\n\tValue: {node.value}\n\tAttribute: {node.attr}\n\tContext: {node.ctx}')

    @recursive
    def visit_AsyncFunctionDef(self, node):
        """ visit a Assign node and visits it recursively"""
        print(f'{type(node).__name__}\n\tAttribute: {node.__getattribute__}\n\tKeywords: {node.keywords}')

    @recursive
    def visit_Lambda(self, node):
        """ visit a Function node """
        print(type(node).__name__)

    @recursive
    def visit_Module(self, node):
        """ visit a Module node and the visits recursively"""
        pass

    @recursive
    def visit_Try(self, node):
        """ visit a Try node and visits it recursively"""
        print(type(node).__name__)

    @recursive
    def visit_ExceptHandler(self, node):
        """ visit a Except node and visits it recursively"""
        print(type(node).__name__)

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
        """ visit a Name node and visits it recursively"""
        print(f'{type(node).__name__}\n\tId: {node.id}\n\tContext: {node.ctx}')

    def generic_visit(self, node):
        ast.NodeVisitor.generic_visit(self, node)

