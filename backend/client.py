import requests
from flask import Flask, jsonify

url = 'http://127.0.0.1:5000/recommend'
myobj = {"Answers": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1,
                     2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 1, 0]}

x = requests.post(url, json=myobj)


print(x.text)