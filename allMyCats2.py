catName=[]
while True:
        print('cat '+str(len(catName)+1))
        name=input()
        if name=='':
                break
        catName=catName+[name]
for name in catName:
        print(name)
