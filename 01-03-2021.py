''' 01-03-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 2단계
    언어 - Python'''



# 1330
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

temp = []
flag = 0

while(flag == 0):
    temp = input().split( )
    a = int(temp[0])
    b = int(temp[1])

    if -10000 <= a <= 10000 and -10000 <= b <= 10000:
        flag = 1

if a > b:
    print(">")

elif a < b:
    print("<")

else:
    print("==")



# 9498
# 시험 점수를 입력받아 90~100점은 A, 80~89점은 B, 70~79점은 C, 60~69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

flag = 0

while(flag == 0):
    score = int(input())
    if score >= 0 and score <= 100:
        flag = 1

if score >= 90:
    print("A")
elif score < 90 and score >= 80:
    print("B")
elif score < 80 and score >= 70:
    print("C")
elif score < 70 and score >= 60:
    print("D")
else:
    print("F")



# 2753
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

flag = 0
while (flag == 0):
    year = int(input())

    if 1 <= year <= 4000:
        flag = 1

if (year%4) == 0 and (year%100 != 0 or year%400 == 0):
    print(1)

else:
    print(0)



# 14681
# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다.
# "Quadrant n"은 "제 n사분면" 이라는 뜻이다.
# 예를 들어, 좌표가 (12, 5)인 점 A는 x 좌표와 y 좌표가 모두 양수이므로 제1사분면에 속한다.
# 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

flag = 0
while (flag == 0):
    x = int(input())
    y = int(input())

    if (-1000 <= x <= 1000 and x != 0) and ( -1000 <= y <= 1000 and y != 0):
        flag = 1

if ( x > 0 and y > 0 ):
    print(1)
elif ( x < 0 and y > 0 ):
    print(2)
elif ( x < 0 and y < 0 ):
    print(3)
else:
    print(4)



# 2884번
# 상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
# 상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
# 이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해주었다.
# 바로 "45분 일찍 알람 설정하기"이다.
# 이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 
# 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
# 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

temp = []
flag = 0
while (flag == 0):
    temp = input().split( )
    h = int(temp[0])
    m = int(temp[1])

    if (0 <= h <= 23 and 0<= m <= 59):
        flag = 1

if (m >= 45):
    print(h, m-45)
elif (h == 0 and m < 45):
    print(23, m+15)
else:
    print(h-1, m+15)
