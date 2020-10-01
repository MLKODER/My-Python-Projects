n=input()
h=n[0:2]
m=n[3:5]
s=n[6:8]
t=n[8:10]
if int(h)>0 and int(m)<60 and int(s)<60:
    if int(h)<=11 and t=='AM':
        print(h+':'+m+':'+s)
    elif int(h)==12 and t=='AM':
        print('00'+':'+m+':'+s)
    elif int(h)<=11 and t=="PM":
        print(str(int(h)+12)+":"+m+':'+s)
    elif int(h)==12 and t=="PM":
        print("24"+':'+m+':'+s)
