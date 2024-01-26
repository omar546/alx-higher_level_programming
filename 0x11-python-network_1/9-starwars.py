#!/usr/bin/python3
"""posting data to swapi api"""
if __name__ == "__main__":
    import requests
    import sys
    url = "https://swapi.co/api/people/"
    search_url = url + "?search="
    if len(sys.argv) > 1:
        search_url += sys.argv[1]
    else:
        search_url = url
    response = requests.get(search_url)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            objy = response.json()
            if len(objy) == 0:
                print('No result')
                sys.exit()
            print('Number of results: {}'.format(objy.get('count')))
            ress = objy.get('results')
            for r in ress:
                print(r.get('name'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
