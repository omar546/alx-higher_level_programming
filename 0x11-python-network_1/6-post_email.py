#!/usr/bin/python3
"""posting data to web server"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    load = {'email': email}
    response = requests.post(url, data=load)
    print(response.text)
