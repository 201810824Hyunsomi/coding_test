n=int(input())
if n==5:
    print(0)
sun=n%5
count=0
while n!=1:
    if (n%5)==0:
        n=n//5
        count=count+1
    elif (n%5)==1:
        n=n-1
        count=count+1
    elif (n%5)==2 or (n%5)==4:
        n=n//2
        count=count+1
    else:
        n=n//3
        count=count+1

print(count)
    
