birthdays={
'Mayank Singh':'8 July',
'Arush Garg':'3 November',
'Shaonika Saha':'15 august',
'Sakshi Sharma':'19 May',
'Aniket Singh':'18 May',
}
date=''
while True:

	name=input('enter a name to know their birth date [blank to quit] : ')

	if name=='':
		break
	else:
		if name in birthdays:
			print(birthdays[name]+' is the birth date of : '+name)
		else:
			print(name+' : Name not in Data Base')
			date=input('Please provide their Birth Date ')
			birthdays[name]=date
			print('Birthdays database is now Updated')

