''' 01-06-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 5단계
    언어 - Python '''


'''
# 10818
# N개의 정수가 주어진다. 이 때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

flag = 0

while(flag == 0):
    n = int(input())
    if (1 <= n <= 1000000):
        flag = 1

temp = [n]

while(1):
    temp = input().split( )
    for i in range(0, n):
        temp[i] = int(temp[i])
    break

maximum = temp[0]
minimum = temp[0]

for i in range(0, n):
    if (temp[i] > maximum):
        maximum = temp[i]
    elif (temp[i] < minimum):
        minimum = temp[i]

print(minimum, maximum)



# 2562
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

temp = []

while(len(temp)!=9):
    a = int(input())
    if 0 < a < 100:
        temp.append(a)

maximum = temp[0]
index = 0
for i in range(0, 9):
    if (temp[i] > maximum):
        maximum = temp[i]
        index = i

print(maximum)
print(index+1)



# 2577
# 세 개의 자연수 A, B, C가 주어질 때 AxBxC를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427이라면
# A x B x C = 150 x 266 x 427 = 17037300이 되고,
# 계산한 결과 17037300에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

number = []
count = []

for i in range(0, 10):
    number.append(i)
    count.append(0)

flag = 0
while(flag == 0):
    A = int(input())
    B = int(input())
    C = int(input())

    if (100 <= A < 1000, 100 <= B < 1000, 100 <= C < 1000):
        flag = 1

result = A*B*C
ABC = list(str(result))

for i in range(len(ABC)):
    ABC[i] = int(ABC[i])
    for j in range(len(number)):
        if (ABC[i] == number[j]):
            count[j] = count[j] + 1

for i in range(len(count)):
    print(count[i])
'''


# 3052
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지이다.
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

num = []
remain = []
count = 0

while(len(num) != 10):
    temp = int(input())
    if ( 0 <= temp <= 1000):
        num.append(temp)
        remain.append(temp%42)

remain = set(remain)
print(remain)
print(len(remain))