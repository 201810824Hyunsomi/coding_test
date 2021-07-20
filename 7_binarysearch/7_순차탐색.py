# 리스트에서 특정 원소가 있는지 체크하거나, 리스트 자료형에서 특정한 값을 가지는
# 원소를 세는 경우 사용된다.

def sequential_search(n, target, array):
    for i in range(n):
        if array[i]==target:
            return i+1

print("생성할 원소 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하세요")
input_data=input().split()
n=int(input_data[0])
target=input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한칸 합니다.")
array=input().split()

print(sequential_search(n,target,array))
