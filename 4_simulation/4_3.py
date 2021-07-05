data=input()
row=data[1]
col=data[0]
list=['a','b','c','d','e','f','g','h']
for i in range(len(list)):
    if col==list[i]:
        col=i+1
rstart=1
cstart=1
count=0
move=[(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
for mo in move:
    if(1<=rstart+mo[1] and rstart+mo[1]<=8 and 1<=cstart+mo[0] and cstart+mo[0]<=8):
        count+=1
print(count)
