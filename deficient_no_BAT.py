n=int(input())
l=[]
s=0
for i in range(2,n-1):
    if n%i==0:
        l.append(i)
for i in l:
    s=s+i
print(l)
print(s)
if s<n:
    print('Deficient')
else:
    print('Not deficient')
        
