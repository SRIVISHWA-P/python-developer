#armstrong number
n=int(input("Enter a number to check:"))
lenn=len(str(n))
temp=n
sum=0
while temp!=0:
    temp=temp%10
    sum+=temp*lenn
    temp//=10
if sum==n:
    print("The given number is armstrong number")
else:
    print("no")
