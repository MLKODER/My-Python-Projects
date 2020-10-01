f=int(input())
h=int(input())
d=int(input())
n=int(input())
D=[]
L=[]
p=[]
nl=[]
for i in range(n):
    D.append(int(input()))
    L.append(int(input()))
for i in range(len(D)):
    if D[i]==d:
        p.append(i)
        nl.append(L[i])

    
