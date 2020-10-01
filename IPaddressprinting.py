a=int(input())
b=int(input())
c=int(input())
d=int(input())
if d<=255:
    for i in range(0,5):
        d=d+1
        if d>255:
            d=-1
            continue
        print(a,b,c,d)
if c<=255:
    for i in range(0,5):
        c=c+1
        if c>255:
            c=-1
            continue
        print(a,b,c,d)
if b<=255:
    for i in range(0,5):
        b=b+1
        if b>255:
            b=-1
            continue
        print(a,b,c,d)
if a<=255:
    for i in range(0,5):
        a=a+1
        if a>255:
             a=-1
             continue
        print(a,b,c,d)
               
