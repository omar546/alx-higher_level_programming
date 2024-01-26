#!/usr/bin/python3
"""testing status of web page"""
if __name__ == "__main__":
    import requests
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(print_str)
