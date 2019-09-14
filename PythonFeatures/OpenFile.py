# this line imports argv from sys module
from sys import argv

# this line will accept script , filename as two different arguments
script, filename = argv
# this line will open the file 'filename' in the program
file_open = open(filename)
# file_open has refrence to filename object
print("Reading your file : %s" % (filename))
# this line prints the content of the file in the standard output
print(">>", file_open.read())
