#armstrong number
n=int(input("Enter a number to check:"))
len=len(str(n))
temp=n
sum=0
while temp!=0:
    temp=temp%10
    sum+=temp*len
    temp//=10
if sum==n:
    print("The given number id armstrong number")
