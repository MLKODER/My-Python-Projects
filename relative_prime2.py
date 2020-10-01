m=int(input())
n=int(input())
c=int(0)
if m>n:
    for i in range(2,n):
        if m%i==0 and n%i==0:
            c=1
            #print('Not Coprime')
elif(m>n):
    for i in range(2,m):
        if(m%i==0 and n%i==0):
            c=1
            #print('Not Coprime')
if(c==0):
    if(m%1==0 and n%1==0):
        print('Coprime')
elif(c==1):
    print('Not coprime')
