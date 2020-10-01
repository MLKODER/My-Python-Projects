z=input()
n=z.lower()
count=0
count1=0
l=len(n)
if ord(n[0:1])>=97 and ord(n[0:1])<=122 or ord(n[0:1])>=65 and ord(n[0:1])<=90:
    if l>=8:
        for i in range(l):
            if ord(n[i:i+1])>=32 and ord(n[i:i+1])<=47 or ord(n[i:i+1])>=58 and ord(n[i:i+1])<=64 or ord(n[i:i+1])>=91 and ord(n[i:i+1])<=96 or ord(n[i:i+1])>=123 and ord(n[i:i+1])<=126:
                count=count+1
        for j in range(l):
            if ord(n[j:j+1])>=43 and ord(n[j:j+1])<=52:
                count1=count1+1                   
print(count,count1)
if count>0 and count1>0:
    print('Valid')
else:
    print('Invalid')
