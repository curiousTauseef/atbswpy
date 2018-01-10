# importing webbrowser module to open webpages by using .open() method
# importing requests module to download a webpage from internet using .get() method
# to check the status use object.status_code==requests.codes.ok , it returns boolean status
# another method to check the status is object.raise_for_status() method 
# it the object.status_code returns 200 it means everything went during download
# it is recommended to open a file in binary mode when downloading from requests module
	example=open('file.format','wb')
	for chunk in res.iter_content(pass bytes here):
		example.write(chunk)

# iter_content() method is used to iterate thorught the file byte by byte, it takes size in bytes as argument to create chunks 
of the file which needs to be written
# we can create BeautifulSoup object using bs4.BeautifulSoup(responseobject.text)

#Methods used for BeautifulSoup Objects

1.	Select Method can be used to select particular tags or classes or id's
		we can do so by
		soup.select('div') to select division elements
		soup.selelct('.className') to select a class name
		soup.select('.className > tag') this means the tags which are directly inside
				the particular class can be accessed.
		
