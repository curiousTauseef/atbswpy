import requests

# downloading a pdf file
file = requests.get("http://www.souravsengupta.com/cds2015/python/LPTHW.pdf")

try:
    # raise_for_status() method makes the program to halt if a bad download occurs, something like : the download link is invalid.
    file.raise_for_status()

    # making a file object
    saveFile = open("pdffile.pdf", "wb")

    # using requests object.iter_content() to create chunks of 100000 bytes by passing it as argument
    for chunk in file.iter_content(100000):

        # writing chunks of bytes into one file that in this case pdffile.pdf
        saveFile.write(chunk)

    saveFile.close()

except Exception as exc:

    print("There was an Exception %s" % (exc))
