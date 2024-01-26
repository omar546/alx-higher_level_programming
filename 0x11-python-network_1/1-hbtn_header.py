#!/usr/bin/python3
"""testing status of web page"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        metaData = response.info()
        for header in metaData._headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
