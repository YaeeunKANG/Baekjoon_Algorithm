'''01-25-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 9단계
   언어 - Python'''



# 11653
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

v = int(input())
i = 2

while (v != 1):
    if (v%i == 0):
        v = v/i
        print(i)
    else:
        i = i+1



# 1929
# M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 블로그 참조

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)