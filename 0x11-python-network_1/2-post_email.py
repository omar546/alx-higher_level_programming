#!/usr/bin/python3
"""testing POST requests of a server"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    load = {'email': email}
    load = urllib.parse.urlencode(load)
    load = load.encode('ascii')
    request = urllib.request.Request(url, load)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
