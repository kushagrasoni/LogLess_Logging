import sqlite3
import ast
from dataclasses import dataclass
from xml.etree.ElementInclude import include


@dataclass
class CategoryAlias():
    name :str
    description : str
    ast_node_class : str

@dataclass
class NodeWrapper():
    ast : ast.AST
    category_alias : CategoryAlias


def get_category(ast_node):
    """
    This searches the logless.db "Category" table for various pre-defined code categories in the line of code,
    based on AST and returns them as their corresponding ALIAS. Next, these categories will be looked by the Pattern
    Finder method and will be mapped to the Patterns using "PatterMap" table from logless.db.

    :param ast_node: Input AST node from the parsed source code.
    :return: <CATEGORY ALIAS>
    """
    # Algorithm for finding different possible patterns within a serverless app code
    # This will need extensive pattern based algorithms to identify relevant code which
    # should be logged
    node_type_name = type(ast_node).__name__

    connection = sqlite3.connect('../db/logless.db')
    cursor = connection.cursor()
    row = cursor.execute(f"SELECT * FROM category where name = '{node_type_name}' limit 1;").fetchone()
    if row:
        category_alias = CategoryAlias(*row)
    else:
        category_alias = CategoryAlias(None, None, None)
    return NodeWrapper(ast_node, category_alias)
        

if __name__ == '__main__':
    # would be handled by other functions
    with open('../app2/sample_app2.py', 'r') as f:
        parsed_funct = ast.parse(f.read())
    i = 0
    for node in ast.walk(parsed_funct):
        node_wrapper = get_category(node)
        # print(f'For node {ast.dump(node_wrapper.ast)}, found category mapping {node_wrapper.category_alias}')
        if node_wrapper.category_alias.name:
            print(f'For node {i}, found category mapping {node_wrapper.category_alias}')
            i += 1