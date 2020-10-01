n=int(input())
l=[]
r=[]
count=0
count1=0
for i in range(n):
    l.append(input())
j=1
for i in range(n):
    for j in range(n):
        count1=0
        if l[i]==l[j]:
            count1=count1+1
    if count1==1:
        r.append(l[i])
s=input()
for i in range(len(r)):
    if s==r[i]:
        count=count+1
print(r)
if count>0:
    print('Found')
else:
    print('Not found')
