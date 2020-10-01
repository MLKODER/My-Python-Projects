h=int(input())
m=int(input())
s=int(input())
z=input()
if z=='PM':
    nh=12+1*h
else:
    if z=='AM':
        if h==12:
            nh=00
print(nh,':',m,':',s)
