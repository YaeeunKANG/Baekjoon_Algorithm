''' 01-10-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 6단계
    언어 - Python '''

# 15596
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
# 작성해야 하는 함수는 다음과 같다.
# def solve(a: list) -> int
#    a : 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0<=a[i]<=1,000,000, 1<=n<=3,000,000)
#    리턴값 : a에 포함되어 있는 정수 n개의 합(정수)

'''
1차 시도

flag = 0
while(flag==0):
    n = int(input())
    if(1<=n<=3,000,000):
        flag = 1
        
a = []
temp = []

i = 0
while(len(a) < n):
    temp = input().split( )
    for i in range(0, len(temp)):
        if (0<= int(temp) <= 1,000,000):
            a.append(int(temp[i]))
        else:
            temp.delete(temp[i])
            
def solve(a):
    ans = 0
    for i in range(0, len(a)):
        ans = ans + a[i]
    return ans
'''
'''
2차 시도
b = input().split( )

def solve(a):
    ans = 0
    for i in range(0, len(a)):
        ans = ans + int(a[i])
    return ans

print(solve(b))
'''

# 위의 코드 두 개 모두 Visual Studio Code 에서는 정상 작동하나 acmicpc 채점기에서는 EOFError, 즉 런타임 에러 발생

def solve(a):
    return sum(a)



