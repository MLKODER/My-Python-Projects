from fractions import gcd
 
a= int(input())
b= int(input())
 
if gcd(a,b)==1:
     print("relatively prime")
else:
     print("relatively NOT prime")

