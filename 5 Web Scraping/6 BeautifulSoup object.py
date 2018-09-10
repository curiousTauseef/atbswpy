import requests
import bs4

response = requests.get('http://nostarch.com')

response.raise_for_status()

print(response.text[:800])

# creating a Beautiful Soup Object, other then response.text  a file object can also be taken as argument
# fileObject=open('example.txt')
# noStarchSoup=bs4.BeautifulSoup(fileObject) or directly noStarchSoup=bs4.BeautifulSoup(open('example.html'))

noStarchSoup = bs4.BeautifulSoup(response.text)

print(type(noStarchSoup))
