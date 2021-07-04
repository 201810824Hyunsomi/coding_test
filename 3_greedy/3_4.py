n,k=map(int,input().split())
count=0
if n%k!=0:
    while(n%k!=0):
        n=n-1
        count=count+1
if n%k==0:
    if n/k!=1:
        n=n/k
        count=count+1
    count=count+1
print(count)
