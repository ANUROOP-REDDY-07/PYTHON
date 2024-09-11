#calculator
a=int(input("enter a number"))
b=int(input("enter a number"))
print("sum =",a+b)
print("diff=",a-b)
print("product=",a*b)
print("division=",a/b)

# compound interest
import math
p=1000
t=12
r=8
c=(p*(1+(r/100)**t))-p
print("compound interest=",c)

#distance between 2 points
x1=int(input("enter absicca of first point"))
y1=int(input("enter ordinate of first point"))
x2=int(input("enter absicca of second point"))
y2=int(input("enter ordinate of second point"))
d=(((x2-x1)**2)+((y2-y1)**2))**0.5
print("distance between points=",d)

#printing details of a person
name=input("enter your name")
address=input("enter your address")
number=int(input("enter your number"))
print("name:"+ name)
print("address:"+ address)
print("number:",number)
