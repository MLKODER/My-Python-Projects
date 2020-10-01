n=int(input())
l=[]
m=[]
s=0
sm=0
for i in range(n):
    a=int(input())
    l.append(a)
    for j in range(n):
        b=int(input())
        m.append(b)
        break
for i in range(n):
    s=s+int(l[i])
for i in range(n):
    sm=sm+int(m[i])

c=int(sm/1000)
s=s+c
d=int(sm%1000)
print(s)
print(d)
