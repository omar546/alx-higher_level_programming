#!/usr/bin/python3
"""testing status of web page"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    metaData = response.headers
    print(metaData.get('X-Request-Id'))
