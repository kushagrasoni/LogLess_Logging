import sqlite3


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

    connection = sqlite3.connect('../db/logless.db')
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM category").fetchall()
    print(rows)
    return rows
