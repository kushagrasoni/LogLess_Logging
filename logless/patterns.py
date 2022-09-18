def get_patterns(line: str):
    """
    This searches for various pre-defined patterns in the line of code and returns them as their corresponding ALIAS.
    The patterns and ALIAS will be defined as part of ALGORITHM which will determine what different types of CRUCIAL
    Serverless function needs to be logged in order perform proper logging.
    :param line: Input line of code from the parsed source code.
    :return: <PATTERN ALIAS>
    """
    # Algorithm for finding different possible patterns within a serverless app code
    # This will need extensive pattern based algorithms to identify relevant code which
    # should be logged
    if line.find('=') > 0:
        return "Assignment"
    elif line.startswith('return'):
        return "Return"
