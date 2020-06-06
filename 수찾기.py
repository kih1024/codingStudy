num = int(input())
arr = set(map(int, input().split(" ")))
# set을 이용할때는 값이 있는지 없는지 유무만 판단할때 쓴다. set은 중복이 없고 순서가 없어 있는지 없는지 유무를 판단할때는 무척 빠르다.
num2 = int(input())
pro = list(map(int,input().split(" ")))

for i in pro:
    if i in arr:
        print(1)
    else:
        print(0)