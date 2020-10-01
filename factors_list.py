l=[]
a=[]
b=[]
c=[]
d=[]
for i in range(4):
    l.append(int(input()))
for i in range(1,l[0]+1):
    if l[0]%i==0:
        a.append(i)
for i in range(1,l[0]+1):
    if l[1]%i==0:
        b.append(i)
for i in range(1,l[0]+1):
    if l[2]%i==0:
        c.append(i)
for i in range(1,l[0]+1):
    if l[3]%i==0:
        d.append(i)
for i in d:
    for j in c:
        for k in b:
            for g in a:
                if i==j and j==k and k==g:
                    print(i)
for i in d:
    for j in c:
        for k in b:
            for g in a:
                if j!=k or j!=g and i!=k or i!=g :
                    print("Factors not Equal", i,j)
                

        
        
    
             
             
