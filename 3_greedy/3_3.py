n,m=map(int,input().split())
answer=0
for i in range(n):
    value=list(map(int,input().split()))
    minimum=min(value)
    answer=max(answer,minimum)
print(answer)
