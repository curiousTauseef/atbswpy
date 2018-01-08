#all the results in findall() method are appended into a tuple, tuples are immutable in nature
import re
ro=re.compile(r'\d{3}-\d{3}-\d{4}')
mo=ro.findall('all the numbers are 123-456-8795 145-666-7894 123-456-9898')
print(mo)
print('length of mo is :'+ str(len(mo)))


print('grouping and then using findall method')

ro2=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2=ro2.findall('all the numbers are 123-456-8795 145-666-7894 123-456-9898')
print(mo2) #mo2 and mo are tuples
