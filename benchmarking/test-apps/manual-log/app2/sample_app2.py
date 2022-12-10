"""
Purpose

Shows how to implement an AWS Lambda function that handles input from direct
invocation.
"""
import logging


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
    logging.info('Initialized "results" variable with %s', result)

    action_event = event.get('action')
    logging.info('Initialized "action_event" variable with value = %s', action_event)

    try:
        number = event.get('number')
        logging.info('Assigned %s value to "number" variable.', number)

    except:
        number = 0
        logging.info('Assigned %s value to "number" variable.', number)

    if action_event == 'increment':
        result = increase_by_1(number)
        logging.info('Updated "results" variable with value = %s', result)

        # result = number + 1
        logging.info('Calculated result of %s', result)
    elif action_event == 'decrement':
        result = decrease_by_1(number)
        # result = number - 1
        logging.info('Updated "results" variable with value = %s', result)

    response = {'result': result}
    logging.info('Created "response" variable with value = %s', response)

    logging.info('Function returns value %s', response)
    return response


def increase_by_1(value):
    return value + 1


def decrease_by_1(value):
    return value - 1
