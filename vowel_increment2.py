a=input()
l=len(a)
for i in range(5):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        d=chr(ord(a[i])+5)
        if ord(d)>122:
            e=ord(d)-122
            f=97+e
            d=chr(f)
        print(d)
    else:
        if a[i]!='a' or a[i]!='e' or a[i]!='i' or a[i]!='o' or a[i]!='u':
            d=chr(ord(a[i])+4)
            if ord(d)>122:
                e=ord(d)-122
                f=97+e
                d=chr(f)
                if d=='a' or d=='e' or d=='i' or d=='o' or d=='u':
                    d=chr(ord(d)+1)
            print(d)
    
