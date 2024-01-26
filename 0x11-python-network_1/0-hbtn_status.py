#!/usr/bin/python3
"""testing status of web page"""
if __name__ == "__main__":
    import urllib.request
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        bytes = response.read()
        content = bytes.decode('utf-8')
        dis_str = '''Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}'''.format(type(bytes), bytes, content)
        print(dis_str)
