#we are using sub() method to replace the matched text with our custom text
import re
#\w only mathes the first letter of the next word, whereas \w+ matches the complete next word
ro=re.compile(r'H\w+')
#in the line below every word starting with capital H will be replaced by Carter
#if \w is used in replacement of \w+ , Hill will be replaced by Carterill instead  of Carter
#with \w+ we are replacing 
mo=ro.sub('Carter','Agent Hill belongs to S.H.I.E.L.D, Agent Hill is Awesome')
print(mo)
