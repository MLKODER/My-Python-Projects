l=[]
for i in range(3):
    l.append([])
for i in range(3):
    for j in range(3):
        l[i].append(j)

for i in range(3):
    for j in range(3):
        l[i][j]=int(input())
print(l)
if l[0][0]==l[0][1] and l[0][1]==l[0][2]:
    print('Winner Winner Chicken Dinner')
if l[1][0]==l[1][1] and l[1][1]==l[1][2]:
    print('Winner Winner Chicken Dinner')
if l[2][0]==l[2][1] and l[2][1]==l[2][2]:
    print('Winner Winner Chicken Dinner')
if l[0][0]==l[1][0] and l[1][0]==l[2][0]:
    print('Winner Winner Chicken Dinner')
if l[0][1]==l[1][1] and l[1][1]==l[2][1]:
    print('Winner Winner Chicken Dinner')
if l[0][2]==l[1][2] and l[1][2]==l[2][2]:
    print('Winner Winner Chicken Dinner')
if l[0][0]==l[1][1] and l[1][1]==l[2][2]:
    print('Winner Winner Chicken Dinner')
if l[2][0]==l[1][1] and l[1][1]==l[0][2]:
    print('Winner Winner Chicken Dinner')



