# this code works effectively for links which presents text file

import requests  # importing requests module to download stuff from internet

# creating a result object
# using get function to download
# if it succeeds in downloading then the complete webpage will be saved in the result as a response object
result = requests.get('')

# checking download status
# using object.status_code==requests.codes.ok to find status in boolean
print(str(result.status_code == requests.codes.ok))

print('-------------')
print('-------------')
print('-------------')

print('Length : '+str(len(result.text)))

print(result.text[:1500])
