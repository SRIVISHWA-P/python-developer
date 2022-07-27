n=int(input("Enter a number to check:"))
def prime(n):
    for i in range(2,n):
        if n==2:
            print(n,"is a prime number")
        elif n%i==0:
            print(n,"is not a prime number")
            break
        else:
            print(n,"is a prime number")
            break
if n==0 or n==1 :
    print(n,"not a prime number")
else:
    prime(n)