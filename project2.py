print("welcome to the simple interest calculator...........\b\b\b")
print("To calculate the simple interest first enter,")
p=int(input("Enter the principal amount deposited:"))
n=int(input("Enter the number of years:"))
r=int(input("Enter the rate of interest per annum:"))
si=p*n*r/100
print("The simple interest calculated was: Rs.",round(si))
