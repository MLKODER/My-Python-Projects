n=input() #97-122
for i in range(len(n)):
    p=chr(ord(n[i:i+1])+3)
    print(p, end='')
