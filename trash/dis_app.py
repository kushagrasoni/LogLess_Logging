import dis

def foo():
    arg1 = 1
    arg2 = 2
    if arg1 > arg2:
        a = arg1 - arg2
    else:
        a = arg2 - arg1
    var = 5
    b = a * var
    return a + b




def get_assigned_name(frame):
    """ Checks the bytecode of *frame* to find the name of the variable
    a result is being assigned to and returns that name. Returns the full
    left operand of the assignment. Raises a `ValueError` if the variable
    name could not be retrieved from the bytecode (eg. if an unpack sequence
    is on the left side of the assignment).

        var = get_assigned_frame(sys._getframe())
        assert var == 'var'
    """

    SEARCHING, MATCHED = 1, 2
    state = SEARCHING
    result = ''
    for op in dis.get_instructions(frame.f_code):
        if state == SEARCHING and op.offset == frame.f_lasti:
            state = MATCHED
        elif state == MATCHED:
            if result:
                if op.opname == 'LOAD_ATTR':
                    result += op.argval + '.'
                elif op.opname == 'STORE_ATTR':
                    result += op.argval
                    break
                else:
                    raise ValueError('expected {LOAD_ATTR, STORE_ATTR}', op.opname)
            else:
                if op.opname in ('LOAD_NAME', 'LOAD_FAST'):
                    result += op.argval + '.'
                elif op.opname in ('STORE_NAME', 'STORE_FAST'):
                    result = op.argval
                    break
                else:
                    message = 'expected {LOAD_NAME, LOAD_FAST, STORE_NAME, STORE_FAST}'
                    raise ValueError(message, op.opname)

    if not result:
        raise RuntimeError('last frame instruction not found')
    return result
