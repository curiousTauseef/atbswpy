n=int(input("Enter number of elements you wish to have in fibo seq."))
a=0
b=1
print(a)
print(b)
for i in range(1,n-1):
   a,b=b,a+b
   print(b)

