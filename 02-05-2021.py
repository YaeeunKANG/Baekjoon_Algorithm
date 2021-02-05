'''02-05-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 12단계
   언어 - Python'''

# 2751
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
N = int(input())
num = []

for _ in range(0, N):
    num.append(int(input()))

num.sort()
for i in range(0, N):
    print(num[i])

#################################################################################
## 시간초과 -> PyPy로 아래 코드 제출시 해결 / 아래 코드와 무엇이 다른지 잘 모르겠음##
#################################################################################

N = int(input()) 
nums = [] 

for i in range(N): 
    nums.append(int(input())) 

nums = sorted(nums) 
for i in range(N):
     print(nums[i])
'''


# 10989
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

N = int(input())
num = []

for _ in range(0, N):
    num.append(int(input()))

num = sorted(num)
for i in range(0, N):
    print(num[i])