import csv

file = open('example.csv')
readerobj = csv.reader(file)
data = list(readerobj)
print(data)
