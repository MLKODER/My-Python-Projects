s=input()
ca=0
ci=0
co=0
cu=0
ce=0
for i in range(len(s)):
    if s[i]=='a':
        ca=ca+1
    if s[i]=='i':
        ci=ci+1
    if s[i]=='o':
        co=co+1
    if s[i]=='u':
        cu=cu+1
    if s[i]=='e':
        ce=ce+1
if ca>0 and ci>0 and co>0 and cu>0 and ce>0:
    print('Vowgram')
else:
    print("Not vowgram")
    
        
