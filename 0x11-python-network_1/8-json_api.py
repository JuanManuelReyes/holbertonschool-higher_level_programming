#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        q = str(argv[1])
    else:
        q = ""
    
    data = {'q': q}
    res = requests.post("http://0.0.0.0:5000/search_user", data)

    try:
        json = res.json()
        if(len(json)) == 0:
            print("No result")
        if(len(json) > 0):
            print("[{}] {}".format(json["id"], json["name"]))
    except ValueError as error:
        print("Not a valid JSON")