''' 01-05-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 3단계
    언어 - Python '''



# 11021
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

temp = []

t = int(input())

for i in range(0, t):
    temp = input().split( )
    a = int(temp[0])
    b = int(temp[1])
    print('Case #{0:d}: {1:d}'.format(i+1, a+b))



# 11022
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

temp = []

t = int(input())

for i in range(0, t):
    temp = input().split( )
    a = int(temp[0])
    b = int(temp[1])
    print('Case #{0:d}: {1:d} + {2:d} = {3:d}'.format(i+1, a, b, a+b))



# 2438
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

flag = 0

while(flag == 0):
    n = int(input())

    if (1 <= n <= 100):
        flag = 1

for i in range(1, n+1):
    for j in range(0, i):
        print("*", end = '')
    print("")



# 2439
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별을 출력하시오.

flag = 0

while(flag == 0):
    n = int(input())

    if (1 <= n <= 100):
        flag = 1

for i in range(1, n+1):
    for j in range(0, n-i):
        print(" ", end='')
    for k in range(0, i):
        print("*", end='')
    print("")



# 10871
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    temp = input().split( )
    n = int(temp[0])
    x = int(temp[1])

    if (1 <= n <= 10000 and 1 <= x <= 10000):
        flag = 1

temp = input().split( )

for i in range(0, n):
    a = int(temp[i])
    if a < x :
        print(a, end=' ')

