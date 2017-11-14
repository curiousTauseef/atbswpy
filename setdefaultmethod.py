#to avoid using 
#if key not in spam:
#	spam[key]=value
#we use setdefault method
#is working just like append in list but only for once.. as dictionaries are not appendable
spam={'color':'red','type':'cloth'}
if 'key' not in spam.keys():
	spam.setdefault('key','value')
print(spam)

