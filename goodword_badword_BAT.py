n=input()
count=0
l=len(n)
for i in range(l):
    for j in range(i+1,l):
        if n[i:i+1].upper()==n[j:j+1].upper():
            count=count+1
if count==0:
    print('Good Word')
else:
    print('Bad word')
            
