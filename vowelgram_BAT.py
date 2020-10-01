s=input()
def vowelgram(s):
    ca=0
    co=0
    ci=0
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
    if ca==1 and ci==1 and co==1 and cu==1 and ce==1:
        print('Vowelgram')
    else:
        print('Not vowelgram')
vowelgram(s)
