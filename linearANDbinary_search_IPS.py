l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
s=int(int(input()))
o=int(input())
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=l[j]

if o==1:
    for i in range(n):
        if l[i]==s:
            print(i)
        else:
            print('Not found')
if o==2:
    count=0
    first=0
    last=len(l)-1
    while first<=last and count==0:
        midpoint=(first+last)//2
        if l[midpoint]==s:
            count=count+1
        else:
            if s<l[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    if count>0:
        print(midpoint)
    else:
        print('Not found')
