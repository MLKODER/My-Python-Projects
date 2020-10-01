from math import*
n=int(input())
s=[]
for i in range(n):
    s.append(input())

def sympali(s):
    l=len(s)
    f=[]
    b=[]
    count=0
    count1=0
    if l%2==0:
        mid=int(l/2)
        for i in range(mid):
            f.append(s[i])
        for i in range(mid,l):
            b.append(s[i])
        dupb=[]
        dupb=b.copy()
        b.reverse()
        for i in range(len(f)):
            if f[i].lower()==b[i].lower(): 
                count=count+1
        for i in range(len(f)):
            if f[i].lower()==dupb[i].lower():
                count1=count1+1
        if count==len(f) and count1!=len(f):
            print('Palindrome')
        if count1==len(f) and count!=len(f):
            print('Symmetric')
        if count==len(f) and count1==len(f):
            print('Both',count,count1)
        if count!=len(f) and count1!=len(f):
            print('No property')
    if l%2!=0:
        mid=l/2
        midm=floor(mid)
        for i in range(midm):
            f.append(s[i])
        for i in range(midm+1,l):
            b.append(s[i])
        dupb=[]
        dupb=b.copy()
        b.reverse()
        for i in range(len(f)):
            if f[i].lower()==b[i].lower(): 
                count=count+1
        for i in range(len(f)):
            if f[i].lower()==dupb[i].lower():
                count1=count1+1
        if count==len(f) and count1!=len(f):
            print('Palindrome')
        if count1==len(f) and count!=len(f):
            print('Symmetric')
        if count==len(f) and count1==len(f):
            print('Both')
        if count!=len(f) and count1!=len(f):
            print('No property')
        
for i in range(n):
    sympali(s[i])
    
        
        
            
      
