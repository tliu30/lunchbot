#!/usr/bin/env python
from datetime import date
import json
import logging
import os
import random
import requests

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
        'Hi friends! '
        'Today we will be having {todays_choice}; hope you enjoy it!'
        '\nPeace out,\n\tLunch bot'
    ).format(todays_choice=todays_choice)


def create_subject(todays_choice):
    return 'Lunch Bot {}'.format(date.today().isoformat())


if __name__ == '__main__':
    import settings
    webhook_url = settings.SLACK_WEBHOOK_URL

    options = get_options(DEFAULT_OPTIONS_PATH)
    todays_choice = select_option(options)
    message = create_message(todays_choice)

    response =  requests.post(webhook_url, data=json.dumps({'text': message}), headers={'Content-Type': 'application/json'})

    logger.info(response.status_code)

