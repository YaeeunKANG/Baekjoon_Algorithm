'''01-02-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 1단계
    언어 - Python
'''



# 1001
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    temp =input().split()
    a = int(temp[0])
    b = int(temp[1])
    
    if a > 0 and b < 10:
        flag = 1

print(a-b)



# 10998
# 두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    temp =input().split()
    a = int(temp[0])
    b = int(temp[1])
    
    if a > 0 and b < 10:
        flag = 1

print(a*b)




# 1008
# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    temp =input().split()
    a = int(temp[0])
    b = int(temp[1])
    
    if a > 0 and b < 10:
        flag = 1

print(a/b)



# 10869
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    temp =input().split()
    a = int(temp[0])
    b = int(temp[1])
    
    if 1 <= a <= 10000 and 1 <= b <= 10000:
        flag = 1

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)



# 10430
# (A+B)%C는 ((A%C) + (B%C))%C와 같을까?
# (AxB)%C는 ((A%C) x (B%C))%C와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    temp =input().split()
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    
    if 2 <= a <= 10000 and 2 <= b <= 10000 and 2 <= c <= 10000:
        flag = 1

print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)



# 2588
# (세 자리 수) x (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#
#        4 7 2  - (1)
#      x 3 8 5  - (2)
#  -------------------
#      2 3 6 0  - (3)
#    3 7 7 6    - (4)
#  1 4 1 6      - (5)
#  -------------------
#  1 8 1 7 2 0  - (6)
#
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6) 위치에 들어갈 값을 구하는 프로그램을 작성하시오.

a = int(input())
b = int(input())
c = b%10
d = int(((b%100) - c)/10)
e = int((b - d*10 - c)/100)

print(a*c)
print(a*d)
print(a*e)
print(a*b)
