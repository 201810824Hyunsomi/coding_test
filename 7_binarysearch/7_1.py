n=int(input())
array1=list(map(int,input().split()))

m=int(input())
array2=list(map(int,input().split()))

array3=[]
for num in array2:
    count=0
    for num2 in array1:
        if num==num2:
            count=count+1
    if count==1:
        array3.append("yes")
    else:
        array3.append("no")
print(array3)
