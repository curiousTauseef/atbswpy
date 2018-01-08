import requests

result=requests.get('https://www.automatetheboringstuff.com/files/rj.txt')


print(result.status_code)

print(str(result.raise_for_status()))

print('--------')

print(result.text[:150])
