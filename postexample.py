import requests

out_data = {
   "name": "Sanika Gupte",
   "net_id": "sgg15",
   "e-mail": "sanika.gupte@duke.edu"
}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.text)

# To visualize all the students that have posted run http://vcm-21170.vm.duke.edu:5000/list in the webbrowser
# You can make get requests via your browser
