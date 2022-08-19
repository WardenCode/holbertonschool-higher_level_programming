#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

if __name__ == '__main__':
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    response = post(URL, {'q': argv[1]})

    type_res = response.headers['content-type']

    if type_res == 'application/json':
        result = response.json()
        if result != {}:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
