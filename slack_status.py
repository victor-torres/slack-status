#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

SETTINGS = {
    'SLACK_FIRST_NAME': None,
    'SLACK_LAST_NAME': None,
    'SLACK_API_TOKEN': None,
}

def load_settings():
    map(lambda k: SETTINGS.update({k: os.environ[k]}), SETTINGS.keys())


def main():
    load_settings()
    


if __name__ == '__main__':
    main()

