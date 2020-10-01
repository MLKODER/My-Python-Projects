n=int(input())
l=[]
c=[]
for i in range(n+1):
    a=int(input())
    l.append(a)
m=int(input())
o=[]

for i in range(m+1):
    b=int(input())
    o.append(b)
if n>m:
    k=n-m
    for i in range(k):
        o.insert(0,0)
else:
    if m>n:
        d=m-n
        for i in range(d):
            o.insert(0,0)
#for i in range(10):
    #print(l[i])
#for i in range(10):
    #print(o[i])
for i in range(n):
    s=l[i]+o[i]
    c.append(s)

for i in range(len(c)):
    print(c[i])
    
    

    
