n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def searchdfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y]=1
        searchdfs(x+1,y)
        searchdfs(x-1,y)
        searchdfs(x,y+1)
        searchdfs(x,y-1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if searchdfs(i,j) == True:
            result+=1

print(result)
