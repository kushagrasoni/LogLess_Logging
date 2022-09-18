def get_patterns(line: str):
    # Algorithm for finding different possible patterns within a serverless app
    if line.find('=') > 0:
        return "Assignment"
    elif line.startswith('return'):
        return "Return"
