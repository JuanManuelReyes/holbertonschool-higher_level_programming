#!/usr/bin/python3
"""
Write a Python script that fetches
https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
