import requests
import json

s = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/sgg15")
sd = json.loads(s.text)
id1 = sd["Donor"]
id2 = sd["Recipient"]

print(s.status_code)

b1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(id1))
b2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(id2))

print(b1.status_code)
print(b2.status_code)

if b1 == b2:
    match = "Yes"
else:
    match = "No"

out_data = {
    "Name" : "sgg15",
    "Match" : match
}

print("{} {}".format(b1.text,b2.text))
print(match)

r = requests.post("http://vcm-21170.vm.duke.edu:5002/match_check", json=out_data)

print(r.text)
print(s.status_code)
