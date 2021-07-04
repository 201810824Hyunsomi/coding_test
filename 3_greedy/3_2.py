n, m, k=map(int,input().split())
value=list(map(int,input().split()))
value.sort()
big=value[n-1]
big2=value[n-2]
sum=0
for i in range(1,m+1):
    if i%k==0:
        sum+=big2
        continue
    sum+=big
print(sum)
