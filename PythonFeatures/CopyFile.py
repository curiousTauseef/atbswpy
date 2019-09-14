from sys import argv

script, filenameone, filenametwo = argv
print("this program copies content of : %s to %s" % (filenameone, filenametwo))

print("file one has been opened in read mode by the program %s" % script)
file_one_open = open(filenameone)
file_one_read = file_one_open.read()

print("file two has been opened in write mode by the program %s" % script)
file_two_open = open(filenametwo, "w")
print("%s contents have been truncated" % (filenametwo))
file_two_open.truncate()
print("making changes ....")
file_two_write = file_two_open.write(file_one_read)

print(
    "contents of file  %s have been copied to the file %s" % (filenameone, filenametwo)
)
print("to read the content of both the files open another script")

file_one_open.close()
file_two_open.close()
