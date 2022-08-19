#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""


if __name__ == '__main__':
    from requests import get

    response = get("https://intranet.hbtn.io/status")

    res = response.text

    print('\t- type: {}'.format(type(res)))
    print('\t- content: {}'.format(res))
