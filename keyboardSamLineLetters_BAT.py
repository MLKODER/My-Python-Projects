w=input()
u=w.lower()
n=len(u)
count=0
count1=0
count2=0
for i in range(len(u)):
    if u[i:i+1]=='q' or u[i:i+1]=='w' or u[i:i+1]=='e' or u[i:i+1]=='r' or u[i:i+1]=='t' or u[i:i+1]=='y' or u[i:i+1]=='u' or u[i:i+1]=='i' or u[i:i+1]=='o' or u[i:i+1]=='p':
        count=count+1
    elif u[i:i+1]=='a' or u[i:i+1]=='s' or u[i:i+1]=='d' or u[i:i+1]=='f' or u[i:i+1]=='g' or u[i:i+1]=='h' or u[i:i+1]=='j' or u[i:i+1]=='k' or u[i:i+1]=='l':
        count1=count1+1
    elif u[i:i+1]=='z' or u[i:i+1]=='x' or u[i:i+1]=='c' or u[i:i+1]=='v' or u[i:i+1]=='b' or u[i:i+1]=='n' or u[i:i+1]=='m':
        count2=count2+1
if count==n or count1==n or count2==n:
    print('Yes')
else:
    print('No')
    
