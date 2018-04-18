#this is same as greedy as well as non greedy matching
import re
ro=re.compile(r'(Ha){3,5}')  #is same as (Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)(Ha)
#greedy by default will print the largest matching string
mo=ro.search('hey man ! HaHaHaHaHaHaHaHaHaHaHaHaHaHaHa you look bad !')
print(mo.group())  #python regular expressions are greedy by default should return longest matching result

print('to return shortest possible match')

#? resturns the non greedy matching
ro2=re.compile(r'(Ha){2,5}?')
mo2=ro2.search('hey the result will be shortest possible match because of ? in pattern HaHaHaHaHaHaHaHaHa')
print(mo2.group())  #HaHa
