#!/usr/bin/python3
"""posting data to web server"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
