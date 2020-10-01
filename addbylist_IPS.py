n=int(input())
x=[]
y=[]
for i in range(n):
    x.append(int(input()))
for j in range(n):
    y.append(int(input()))
x.reverse()
y.reverse()
s=[]
d=0
for i in range(n):
    ss=int(x[i]+y[i])+d
    d=0
    m=ss%10
    if m>=0 and i<n-1:
        s.append(m)
        d=ss//10
    else:
        a=ss%10
        b=ss//10
        s.append(a)
        s.append(b)
s.reverse()
print(s)
