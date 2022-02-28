import requests

r = requests.get("https://api.github.com/repos/dward2/ClassworkSpring2022/branches")

print(r)
print(type(r))
print("Status Code: {}".format(r.status_code))
#print("Text: {}".format(r.text)) # JSON encoded string

# If the request is not successful,
if r.status_code != 200:
    print("There was a problem")
    print(r.text)
    exit()

answer = r.json()

for branch in answer:
    print(branch["name"])

print("done")