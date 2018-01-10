import bs4,requests

response=requests.get('https://www.geeksforgeeks.org/python-language-introduction/')

bObj=bs4.BeautifulSoup(response.text)

pelements=bObj.select('.entry-content > p')

print(type(pelements))

print(pelements[0].getText())
print(pelements[1].getText())
