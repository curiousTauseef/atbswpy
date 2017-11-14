classItems={'pen':15,'pencil':5,'ruler':1,'sharpener':1}
#second argument return the value specied if key not present
print('pens : '+str(classItems.get('pen',0))+' pencils : '+str(classItems.get('pencil',0))+' ruler : '+str(classItems.get('ruler',0)))
