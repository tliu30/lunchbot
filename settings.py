import json

SECRETS_PATH = 'secrets.json'

with open(SECRETS_PATH, 'r') as f:
    SECRETS = json.load(f)

SLACK_WEBHOOK_URL = SECRETS['SLACK_WEBHOOK_URL']
