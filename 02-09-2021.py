'''02-09-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 12단계
   언어 - Python'''



# 1427
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

N = int(input())

i = list(map(int, str(N)))
i.sort(reverse=True)
for _ in i :
    print(_, end="")



# 11650
# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

N = int(input())
array = []

for _ in range(N):
    x, y = map(int,input().split())
    array.append((x,y))

array.sort()   
array.sort(key= lambda x : x[0])

for i in array :
    print(*i)