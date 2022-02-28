import requests

out_data = {
    "user": "ria", "message": "hi friend"
}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)

print("Status Code: {}".format(r.status_code))

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Sanika+Kayana")

print(r.text)
