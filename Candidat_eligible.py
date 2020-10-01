a=input('First name ')
b=input('middle name ')
c=input('last name ')
d=input('Adhhar number ')
e=input('Mobile Number ')
print("Enter yout DOB ")
f=int(input('Date '))
g=int(input('Month '))
h=int(input('Year '))
if len(a)==0 or len(c)==0:
    print('Type your name')
if len(d)<12 or len(d)>12:
    print('Type valid adhaar no.')
if len(e)<10 or len(e)>10:
    print('Type valid mobile no.')
else:
    print('Eligible')
def DOB(f,g,h):
    if f>=4 and g>=9 and h>=2001:
        print('Your age is not eligible')

DOB(f,g,h)
