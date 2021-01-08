''' 01-08-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 5단계
    언어 - Python '''


# 1546
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다.
# 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

'''
flag = 0
score = []
temp = []

while(flag == 0):
    n = int(input())
    if ( n < 1000):
        flag = 1

while(len(score) < n):
    temp = input().split( )
    for i in range(len(temp)):
        temp[i] = int(temp[i])
        if temp[i] == 0:
            count = count + 1
            if (count == 1):
                score.append(temp[i])
            elif count > 1:
                break
        elif (0 < temp[i] <= 100):
            score.append(temp[i])

max = score[0]
sum = 0

for i in range(0, len(score)):
    if score[i] > max:
        max = score[i]

for i in range(0, len(score)):
    score[i] = (score[i]/max)*100
    sum = sum + score[i]

print(sum/n)'''

# 런타임에러 발생

N = int(input())
M = list(map(int, input().split()))
M_max = max(M)

for i in range(N):
    M[i] = M[i]/M_max*100
avg = sum(M)/ N
print("%.2f" %avg)