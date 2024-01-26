#!/usr/bin/python3
"""posting data to github api"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    url = "https://api.github.com/"
    user_url = url + "user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(user_url,
                            auth=HTTPBasicAuth(username,
                                               password))
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            objy = response.json()
            print(objy.get('id'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
    else:
        print(None)
