n=int(input())
plan=list(input().split())
xlist=[-1,1,0,0]
ylist=[0,0,-1,1]
xstart=1
ystart=1
for pl in plan:
    if pl=="L":
        if xstart>=2:
            xstart+=xlist[0]
            ystart+=ylist[0]
    elif pl=="R":
        if xstart<=4:
            xstart+=xlist[1]
            ystart+=ylist[1]
    elif pl=="U":
        if ystart>=2:
            xstart+=xlist[2]
            ystart+=ylist[2]
    elif pl=="D":
        if ystart<=4:
            xstart+=xlist[3]
            ystart+=ylist[3]
    
print(ystart, xstart)
