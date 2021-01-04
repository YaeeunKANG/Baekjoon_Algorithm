''' 01-04-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 3단계
    언어 - Python '''



# 2739
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

flag = 0

while(flag == 0):
    dan = int(input())

    if ( 1 <= dan <= 9):
        flag = 1

for i in range (1, 10):
    print(dan, "*", i, "=", dan*i)


# 10950
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

n = int(input())

temp = []

for i in range (0, n):
    temp.append(input().split())
    print(int(temp[i][0]) + int(temp[i][1]))



# 8393
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

flag = 0
sum = 0

while (flag == 0):
    n = int(input())
    
    if ( 1 <= n <= 10000):
        flag = 1

for i in range(1, n+1):
    sum = sum + i

print(sum)



# 15552
# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# C++을 사용하고 있고... Java를 사용하고 있다면, ...
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우, .rstrip()을 추가로 해 주는 것이 좋다.
# 또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

import sys

t = int(sys.stdin.readline())

for i in range(0, t):
    a, b = map(int, sys.stdin.readline().split( ))
    while((a < 1 or a > 1000) or (b < 1 or b > 1000)) :
        a, b = map(int, sys.stdin.readline().split( ))
    print(a+b)



# 2741
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

flag = 0

while(flag==0):
    n = int(input())

    if(n <= 100000):
        flag = 1

for i in range(1, n+1):
    print(i)



# 2742
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

flag = 0

while(flag == 0):
    n = int(input())
    if (n <= 100000):
        flag = 1

j = n
for i in range (0, n):
    print(j)
    j = j-1