import requests


r = requests.get(('https://api.github.com/user', auth=('Victor101020', 'awzrsnspA1')))

print(r.status_code)




