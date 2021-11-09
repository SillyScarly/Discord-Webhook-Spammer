import requests

url = "Insert webhook url here"


data = {
    "content": "message",
    "username": "Raid Bot"
}

while True:
    result = requests.post(url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
