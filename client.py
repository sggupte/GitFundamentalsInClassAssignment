from interface import check_HDL
from flask import Flask, request
import requests
import json

r = requests.get("http://127.0.0.1:5000/")

print(r.status_code)
print(r.text)

r = requests.get("http://127.0.0.1:5000/info")
print(r.status_code)
print(r.text)

out_data = {"name": "David", "hdl_result": 65}
r = requests.post("http://127.0.0.1:5000//hdl_check", json=out_data)
print(r.status_code)
print(r.text)

out_data = {"a": 3, "b": 5}
r = requests.post("http://127.0.0.1:5000/add", json=out_data)
print(r.status_code)
print(r.text)
a = r.json()
print(a[0])

r = requests.get("http://127.0.0.1:5000/add/3/5")
print(r.status_code)
print(r.text)
