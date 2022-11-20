"""
Purpose

Shows how to implement an AWS Lambda function that handles input from direct
invocation.
"""
import sys

sys.path.append('..')
from logless import log

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

import pysnooper


@log
# @pysnooper.snoop(normalize=True)
def lambda_handler(event, context):
    """
    Accepts an action and a single number, performs the specified action on the number,
    and returns the result.

    :param event: The event dict that contains the parameters sent when the function
                  is invoked.
    :param context: The context in which the function is called.
    :return: The result of the action.
    """
    result = None
    action_event = event.get('action')

    try:
        number = event.get('number')

    except:
        number = 0
    if action_event == 'increment':
        # result = increase_by_1(number)
        result = number + 1
        # logger.info('Calculated result of %s', result)
    elif action_event == 'decrement':
        # result = decrease_by_1(number)
        result = number - 1
        logger.error("%s is not a valid action.", action_event)

    response = {'result': result}
    return response


def increase_by_1(value):
    return value + 1


def decrease_by_1(value):
    return value - 1
