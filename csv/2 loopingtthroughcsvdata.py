import csv

file = open('example.csv')
filereader = csv.reader(file)
for row in filereader:
    print('Row#' + str(filereader.line_num) + str(row))
