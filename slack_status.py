#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

SETTINGS = {
    'SLACK_FIRST_NAME': None,
    'SLACK_LAST_NAME': None,
    'SLACK_API_TOKEN': None,
}

URL = 'https://slack.com/api/users.profile.set'


def load_settings():
    map(lambda k: SETTINGS.update({k: os.environ[k]}), SETTINGS.keys())


def parse_args():
    args = sys.argv[1:]  # ignore file name

    last_arg = args[-1]
    if last_arg.startswith(':') and last_arg.endswith(':'):
        emoji = last_arg.strip()
        args = [:-1]  # remove emoji from message
    else:
        emoji = None

    text = args and ' '.join(args)

    return text, emoji


def build_profile(text, emoji):
    profile = {
        'first_name': SETTINGS['SLACK_FIRST_NAME'],
        'last_name': SETTINGS['SLACK_LAST_NAME'],
        'status_text': text,
        'status_emoji': emoji,
    }
    return profile


def build_params(text, emoji):
    profile = build_profile(text, emoji)
    profile = json.dumps(profile)
    profile = urllib.quote(profile)

    token = SETTINGS['SLACK_API_TOKEN']

    params = 'token={token}&profile={profile}'
    params = params.format(token=token, profile=profile)

    return params


def build_headers():
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'cache-control': 'no-cache',
    }
    return headers


def make_request(url, params):
    headers = build_headers()
    response = request.request('POST', url, data=params, headers=headers)
    response = json.loads(response.text)
    return response


def update(text, emoji):
    params = build_params(text, emoji)
    response = make_request(URL, params)
    return bool(response.get('ok'))


def main():
    load_settings()


def main():
    load_settings()
    text, emoji = parse_args()
    update(text, emoji)


if __name__ == '__main__':
    main()

