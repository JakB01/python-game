import requests

url = 
req = requests.get(url)

data = req.json()
data_dict = data.items()
print(data.keys())
print(data["total_count"])
