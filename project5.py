#to generate fibonacci series
n=int(input("enter the number of terms:"))
a=0
b=1
print("fibonacci series as follows")
if n==0:
    print(a)
elif n==2:
    print(b)
else:
    print(a)
    print(b)
    i=0
    while i<=(n-2):
        c=a+b
        print(c)
        a=b
        b=c
        i+=1