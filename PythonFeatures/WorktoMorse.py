
message=input('enter a string to convert it to morse code : ')
message=message.lower()
morsedict={
'a':'.-',
'b':'-...',
'c':'-.-.',
'd':'-..',
'e':'.',
'f':'..-.',
'g':'--.',
'h':'....',
'i':'..',
'j':'.---',
'k':'-.-',
'l':'.-..',
'm':'--',
'n':'-.',
'o':'---',
'p':'.--.',
'q':'--.-',
'r':'.-.',
's':'...',
't':'-',
'u':'..-',
'v':'...-',
'w':'.--',
'x':'-..-',
'y':'-.--',
'z':'--..',
0:'-----',
1:'.----',
2:'..---',
3:'...--',
4:'....-',
5:'.....',
6:'-....',
7:'--...',
8:'---..',
9:'----.',
'.':'.-.-.-',
',':'--..--',
'?':'..--..',
' ':' '
}
messagelist=list(message)

#print(messagelist)

morselist=[]

for letter in messagelist:
	morselist.append(morsedict[letter])
morsestring=' / '.join(morselist)
print('your message \" '+message+' \" in morse is : '+morsestring)
