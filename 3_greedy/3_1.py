n=int(input())
num=0
list=[500,100,50,10]
for li in list:
    num+=int(n/li)
    n=n%li
print(num)
