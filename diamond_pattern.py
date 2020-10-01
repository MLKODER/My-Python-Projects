n=int(input())
p=n+1
a=n
d=1
f=0
if n>0 and n<=50:
    for j in range(n):
        print('*'*n+' '*(j+d)+'*'*n)
        n=n-1
        d=d+1
    m=d+1
    if a==5:
        for i in range(2,2*n+p):
            print('*'*i+' '*(m-f)+'*'*i)
            f=f+2
    elif a>5:
        o=a-5
        for i in range(2,2*n+p):
            print('*'*i+' '*(m-f+o)+'*'*i)
            f=f+2
    elif a<5:
        q=5-a
        for i in range(2,2*n+p):
            print('*'*i+' '*(m-f-q)+'*'*i)
            f=f+2
else:
    print('impossible')
            
            
        
