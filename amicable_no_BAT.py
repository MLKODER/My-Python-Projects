n1=int(input())
n2=int(input())
n1l=[]
n2l=[]
s1=0
s2=0
for i in range(1,n1):
    if n1%i==0:
        n1l.append(i)
for i in range(1,n2):
    if n2%i==0:
        n2l.append(i)
for i in n1l:
    s1=s1+i
for i in n2l:
    s2=s2+i
if s1==n2 and s2==n1:
    print('Yes')
else:
    print('No')

