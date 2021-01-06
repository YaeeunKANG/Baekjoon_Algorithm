''' 01-06-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 4단계
    언어 - Python '''


'''
# 10952
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
temp = []
flag = 0

while(flag == 0):
    temp = input().split(" ")
    a = int(temp[0])
    b = int(temp[1])

    if (0 < a < 10 and 0 < b < 10):
        print(a+b)
    
    elif (a == 0 and b == 0):
        flag = 1


# 10951
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    try:
        temp = input().split(" ")
        a = int(temp[0])
        b = int(temp[1])

        if ( 0 < a < 10 and 0 < b < 10):
            print(a+b)
    
    except:
        break


'''
# 1110
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# 26부터 시작한다. 2+6=8이다. 새로운 수는 68이다. 6+8=14이다. 새로운 수는 84이다. 8+4=12이다. 새로운 수는 42이다. 4+2=6이다. 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램의 작성하시오.

while(1):
    n = int(input())
    if (0 <= n <= 99):
        break

if (n < 10):
    a = 0
else:
    a = int(n/10)
b = n%10

count = 1
temp = int((a+b)%10)

x = b
y = temp

flag = 0

while(flag == 0):
    temp = (x+y)%10

    x = y
    y = temp

    if (x == a and y == b):
        flag = 1
    
    count = count + 1

if (a == 0 and b == 0):
    count = 1

print(count)
