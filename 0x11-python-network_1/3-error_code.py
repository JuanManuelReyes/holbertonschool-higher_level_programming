#!/usr/bin/python3
""" 
Write a Python script that takes in a URL, sends
a request to the URL and displays the body of the
response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.reaed().decode()
            print(content)
    except error.URLError as error:
        print("Error code:", error.code)