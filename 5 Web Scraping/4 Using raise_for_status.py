import requests

result = requests.get("https://www.automatetheboringstuff.com/files/rj.txt")

print(result.status_code)  # 200 means everything is correct

# will print None as the result , because raise_for_status() works for halting the program if anything is incorrect or incomplete
print(str(result.raise_for_status()))

print("--------")

print(result.text[:150])
