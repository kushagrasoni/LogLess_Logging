import logging
import datetime
import igraph


def handler(event, context):
    size = event.get('size')
    logging.info('Initialized "size" variable with %s', size)

    graph_generating_begin = datetime.datetime.now()
    logging.info('Initialized "graph_generating_begin" variable with %s', graph_generating_begin)

    graph = igraph.Graph.Barabasi(size, 10)
    logging.info('Initialized "graph" variable with %s', graph)

    graph_generating_end = datetime.datetime.now()
    logging.info('Initialized "graph_generating_end" variable with %s', graph_generating_end)

    process_begin = datetime.datetime.now()
    logging.info('Initialized "process_begin" variable with %s', process_begin)

    result = graph.pagerank()
    logging.info('Initialized "result" variable with %s', result)

    process_end = datetime.datetime.now()
    logging.info('Initialized "process_end" variable with %s', process_end)

    graph_generating_time = (graph_generating_end -
                             graph_generating_begin) / \
                            datetime.timedelta(microseconds=1)
    logging.info('Initialized "graph_generating_time" variable with %s', graph_generating_time)

    process_time = (process_end - process_begin) / \
                   datetime.timedelta(microseconds=1)
    logging.info('Initialized "process_time" variable with %s', process_time)

    return {
        'result': result[0],
        'measurement': {
            'graph_generating_time': graph_generating_time,
            'compute_time': process_time
        }
    }
