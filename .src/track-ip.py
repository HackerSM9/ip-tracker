import requests

y = '\033[0;33m'
t = '\033[1;36m'
e = '\033[0m'
ip = input(t+"Enter IP to Trace it >>> ")
url = "https://api.ipdata.co/v1/{0}/?api-key=be0f755b93290b4c100445d77533d291763a417c75524e95e07819ad".format(ip)

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

print(y+response.text+e)
