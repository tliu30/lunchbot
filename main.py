#!/usr/bin/env python
from datetime import date
import json
import logging
import random

from sparkpost import SparkPost

logger = logging.getLogger(__name__)

DEFAULT_OPTIONS_PATH = 'options.json'


def get_options(path):
    '''Read in options from a json file; should return a list'''
    with open(path, 'r') as f:
        return json.load(f)


def select_option(options):
    '''Use selection criteria to determine what today's choice is'''
    return random.choice(options)


def create_message(todays_choice):
    '''Draft a message'''
    return (
        '<p>Hi friends!</p>'
        '<p>Today we will be having {todays_choice}; hope you enjoy it!</p>'
        '<p>Peace out,<br>Lunch bot</p>'
    ).format(todays_choice=todays_choice)


def create_subject(todays_choice):
    return 'Lunch Bot {}'.format(date.today().isoformat())


if __name__ == '__main__':
    import settings
    sp = SparkPost(settings.SPARKPOST_API_KEY)

    options = get_options(DEFAULT_OPTIONS_PATH)
    todays_choice = select_option(options)
    message = create_message(todays_choice)
    subject = create_subject(todays_choice)

    response = sp.transmissions.send(
        use_sandbox=True,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipients=settings.DEFAULT_RECIPIENTS,
        subject=subject,
        html=message
    )

    logger.info(response)

