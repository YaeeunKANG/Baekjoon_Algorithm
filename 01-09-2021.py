''' 01-09-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 5단계
    언어 - Python '''



# 8958번
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

n = int(input())
for i in range(n):
    num = input()
    score = 0
    count = 0
    for j in range(len(num)):
        if num[j] == 'O':
            count += 1
            score += count
        elif num[j] == 'X':
            score += 0
            count = 0
    print(score)



# 4344
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

n = int(input())
for i in range(n):
    score = list(map(int, input().split(' ')))
    average = sum(score[1:]) / score[0]
    count = 0
    for j in score[1:]:
        if j > average : 
            count += 1
            
    print(str("%.3f" %round((count/score[0])*100, 3))+"%")