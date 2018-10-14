import csv

file = open('example.csv')  # opening csv file
filereader = csv.reader(file)  # creating csv file reader object
outputfile = open('output.csv', 'w')  # opening output.csv in write mode
outputwriter = csv.writer(outputfile)  # creating csv file writer object
for row in filereader:  # looping through rows
    outputwriter.writerow(row)  # using writerow function of a writer object

file.close()  # closing opened files
outputfile.close()

# more about writerow()
'''
The writerow() method for Writer objects takes a list argument.
Each value in the list is placed in its own cell in the output CSV file. The
return value of writerow() is the number of characters written to the file
for that row (including newline characters).
'''
