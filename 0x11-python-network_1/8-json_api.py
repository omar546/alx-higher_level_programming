#!/usr/bin/python3
"""posting data to web server"""
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        qu = sys.argv[1]
    else:
        qu = ""
    query = {'q': qu}
    response = requests.post(url, data=query)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            objy = response.json()
            if len(objy) == 0:
                print('No result')
                sys.exit()
            idy = objy.get('id')
            namey = objy.get('name')
            print("[{}] {}".format(idy, namey))
        except ValueError as invalid_json:
            print('Not a valid JSON')
