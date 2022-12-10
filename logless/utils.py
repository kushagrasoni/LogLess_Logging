import collections


def get_local_result(frame):
    code = frame.f_code
    vars_order = (code.co_varnames + code.co_cellvars + code.co_freevars +
                  tuple(frame.f_locals.keys()))

    result_items = [(key, value)
                    for key, value in frame.f_locals.items()]

    result_items.sort(key=lambda key_value: vars_order.index(key_value[0]))

    result = collections.OrderedDict(result_items)

    return result


def truncate(string, maximum_length):
    if (maximum_length is None) or (len(string) <= maximum_length):
        return string
    else:
        left = (maximum_length - 3) // 2
        right = maximum_length - 3 - left
        return u'{}...{}'.format(string[:left], string[-right:])
