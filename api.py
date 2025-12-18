import requests
response=requests.get(url="https://cataas.com/cat?json=true")
if response.status_code==200:
    print(f"ok{response.status_code}")
    data=response.json()
    print(data)
elif str(response.status_code).startswith("4"):
    print("false")
elif str(response.status_code).startswith("5"):
    print("no no")