'''01-29-2021 Baekjoon Algorithm
단계별 문제 풀이 - 9단계
언어 - Python'''



# 4153
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

while True:
        a = list(map(int, input().split()))
        max_num = max(a)
        if sum(a) == 0:
                break
        a.remove(max_num)
        if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
                print('right')
        else:
                print('wrong')



# 3053
# 19세기 독일 수학자 헤르만 민코프스키는 비유클리드 기하학 중 택시 기하학을 고안했다.
# 택시 기하학에서 두 점 T1(x1,y1), T2(x2,y2) 사이의 거리는 다음과 같이 구할 수 있다.
#           D(T1,T2) = |x1-x2| + |y1-y2|
# 두 점 사이의 거리를 제외한 나머지 정의는 유클리드 기하학에서의 정의와 같다.
# 따라서 택시 기하학에서 원의 정의는 유클리드 기하학에서 원의 정의와 같다.
# 원: 평면 상의 어떤 점에서 거리가 일정한 점들의 집합
# 반지름 R이 주어졌을 때, 유클리드 기하학에서 원의 넓이와, 택시 기하학에서 원의 넓이를 구하는 프로그램을 작성하시오.

from math import pi

r = int(input())

euclid = r*r*pi 
taxi = r*r*2

print(round(euclid, 4))
print(round(taxi, 4))



# 1002
# 조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
# 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

temp = int(input())

for _ in range(temp):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    
    if ((x1 == x2) and (y1 == y2)):
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    if ((r1 > distance + r2) or (r2 > distance + r1) or (distance > r1 + r2)):
        print(0)
    elif ((r1 == distance + r2) or (r2 == distance + r1) or (r1 + r2 == distance)) :
        print(1)
    else:
        print(2)