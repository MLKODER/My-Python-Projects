d=input().rstrip()
dl=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
h=int(input())
m=int(input())
if h>=0 and h<24 and m>=0 and m<60 and d in dl:
    nh=h+5
    nm=m+30
    bf=nh
    if nh>=24 and m<60:
        bf=nh
        nh=nh-24
    elif nm>=60 and nh<24:
        nm=nm-60
        nh=nh+1
    elif nh>24 and nm>60:
        bf=nh
        nm=nm-60
        nh=nh-24
        nh=nh+1
    if nm==60:
        nh=nh+1
        nm=0
    if nh==24:
        nh=0
    elif nh==24 and nm==60:
        nh=0
        nm=0
        nh=nh+1
    for i in range(len(dl)):
        if d==dl[i]:
            di=i
    print(bf)
    if bf>=24 and di!=len(dl)-1:
        dc=dl[di+1]
    elif bf==0 and di!=len(dl)-1:
        dc=dl[di+1]
    elif di==len(dl)-1:
        dc=dl[0]
    else:
        dc=dl[di]
    print(dc)
    print(nh)
    print(nm)
else:
    print('Invalid input')
    
    
    

            
        
        
        
    
    
