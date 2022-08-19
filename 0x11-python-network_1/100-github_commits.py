#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”

You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/

Print all commits by: `<sha>: <author name>` (one by line)
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]

    URL = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)

    response = get(URL)
    json = response.json()

    for i in range(0, 10):
        sha = json[i].get('sha')
        author = json[i].get('commit').get('author').get('name')
        print("{:s}: {:s}".format(sha, author))
