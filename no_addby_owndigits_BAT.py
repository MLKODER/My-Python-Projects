n=input()
l=len(n)
t=pow(10,l-1)
k=l-1
d=[]
r=int(n)
count=0
for i in range(l):
    e=int(r)//t
    r=int(n)%t
    k=k-1
    t=pow(10,k)
    d.append(e)
for i in range(len(d)):
    count=count+d[i]
print(d)
print(count)
    
