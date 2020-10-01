n=input()
p=[]
s=len(n)
k=s-1
no=int(n)
noo=no
a=pow(10,s-1)
for i in range(s):
    m=int(no/a)
    if noo%m==0:
        p.append(m)
    no=no%a
    k=k-1
    a=pow(10,k)
if len(p)==0:
    print('No factors')
p.reverse()
for i in range(len(p)):
    print(p[i])


    
    
    
