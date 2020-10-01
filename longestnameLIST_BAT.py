n=[]
i= True
while i:
    m=input()
    if m!='Stop':
        n.append(m)
    elif m=='Stop':
        i=False
for i in range(len(n)):
    for j in range(0,len(n)-i-1):
        if len(n[j])>len(n[j+1]):
            temp=n[j]
            n[j]=n[j+1]
            n[j+1]=temp
print(n[len(n)-1])
    
    
      
