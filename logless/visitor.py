import ast
from pprint import pprint

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

    def __init__(self):
        self.result_list = []
        self.node_depth = 0

    def recursive(func):
        """ decorator to make visitor work recursive """

        def wrapper(self, node):
            child_counter = 0

            func(self, node)
            self.node_depth = depth_ast(node)
            print(f'Depth of Node: {self.node_depth}\n')

            for child in ast.iter_child_nodes(node):
                self.visit(child)
                print(f'Current Child {child} Depth: {self.node_depth}')
                print(f'RESULT LIST FOR THE CHILD:\n')
                print(self.result_list)
                self.result_list = []
                self.node_depth -= 1

        return wrapper

    ####
    @recursive
    def visit_Module(self, node):
        """ visit a Module node and the visits recursively"""
        print(type(node).__name__)

    ####
    @recursive
    def visit_FunctionDef(self, node):
        """ visit a Function node and visits it recursively"""
        print(type(node).__name__, node.__dict__['args'], node.__dict__['body'])
        self.result_list.append((type(node).__name__, node.__dict__['args']))

    ####
    def visit_If(self, node):
        """ visit a If node and visits it recursively"""
        print(f'{type(node).__name__}\n\tTest: {node.test}\n\tBody: {node.body}\n\tORElse: {node.orelse}')
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_arguments(self, node):
        """ visit a Arguments node and visits it recursively"""
        print(type(node).__name__, node.__dict__['args'])
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_arg(self, node):
        """ visit a Arg node and visits it recursively"""
        print(type(node).__name__, node.__dict__['arg'])
        self.result_list.append((type(node).__name__, node.__dict__['arg']))

    ####
    def visit_Expr(self, node):
        """ visit a Assign node and visits it recursively"""
        print(type(node).__name__, node.value)
        self.result_list.append((type(node).__name__, node.value))
        self.generic_visit(node)

    ####
    def visit_Assign(self, node):
        """ visit a Assign node and visits it recursively"""
        print(
            f'{type(node).__name__}\n\tTotal Targets: {len(node.targets)}\n\tTargets: {node.targets}\n\tValue: {node.value}')
        self.result_list.append((type(node).__name__, f'Total Targets: {len(node.targets)}', f'Targets: {node.targets}', f'Value: {node.value}'))
        self.generic_visit(node)

    ####
    def visit_BinOp(self, node):
        """ visit a BinOp node and visits it recursively"""
        print(f'{type(node).__name__}\n\tLeft: {node.left}\n\tOperation: {node.op}\n\tRight: {node.right}')
        self.result_list.append((type(node).__name__,))
        self.generic_visit(node)

    ####
    def visit_Add(self, node):
        """ visit a BinOp node and visits it recursively"""
        print(f'{type(node).__name__}')
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_Call(self, node):
        """ visit a Call node and visits it recursively"""
        print(
            f'{type(node).__name__}\n\tFunction: {node.func}\n\tTotal Arguments: {len(node.args)}\n\tArguments: {node.args}\n\tKeywords: {node.keywords}')
        self.result_list.append((type(node).__name__, node.func, len(node.args), node.args))
        self.generic_visit(node)

    ####
    def visit_Attribute(self, node):
        """ visit a Assign node and visits it recursively"""
        print(f'{type(node).__name__}\n\tValue: {node.value}\n\tAttribute: {node.attr}\n\tContext: {node.ctx}')
        self.result_list.append((type(node).__name__, f'Value: {node.value}', f'Attribute: {node.attr}', f'Context: {node.ctx}'))
        self.generic_visit(node)

    ####
    def visit_AsyncFunctionDef(self, node):
        """ visit a Assign node and visits it recursively"""
        print(f'{type(node).__name__}\n\tAttribute: {node.__getattribute__}\n\tKeywords: {node.keywords}')
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_Lambda(self, node):
        """ visit a Lambda Function node """
        print(type(node).__name__)
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_Try(self, node):
        """ visit a Try node and visits it recursively"""
        print(type(node).__name__)
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_ExceptHandler(self, node):
        """ visit a Except node and visits it recursively"""
        print(type(node).__name__)
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_Num(self, node):
        """ visit a Num node and visits it recursively"""
        print(type(node).__name__, node.__dict__['value'])
        self.result_list.append(type(node).__name__)
        self.generic_visit(node)

    ####
    def visit_Str(self, node):
        """ visit a Str node and visits it recursively"""
        print(type(node).__name__, node.s)
        self.generic_visit(node)

    ####
    def visit_Constant(self, node):
        """ visit a Constant node and visits it recursively"""
        print(type(node).__name__, node.value)
        self.result_list.append((type(node).__name__, node.value))
        self.generic_visit(node)

    ####
    def visit_Name(self, node):
        """ visit a Name node and visits it recursively"""
        print(f'{type(node).__name__}\n\tId: {node.id}\n\tContext: {node.ctx}')
        self.result_list.append((type(node).__name__, node.id, node.ctx))
        self.generic_visit(node)


def generic_visit(self, node):
    ast.NodeVisitor.generic_visit(self, node)


def depth_ast(node):
    return 1 + max(map(depth_ast, ast.iter_child_nodes(node)),
                   default=0)
