'''01-19-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 8단계
   언어 - Python'''



# 1193
# 무한히 큰 배열에 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> ... 과 같은 지그재그 순서로
# 차례대로 1번, 2번, 3번, 4번, 5번, ... 분수라고 하자. X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

x = int(input())

n = 1
while(x > n):
    x -= n
    n += 1

if line%2 == 0:
    a = x
    b = n - x + 1

else:
    a = n - x + 1
    b = x

print(a, '/', b, sep='')

# 런타임 오류 발생


# 구글 참고
input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  

gap = max_num - input_num 
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print(f'{top}/{under}')

# 알고리즘은 비슷하다고 생각되는데 왜 런타임 오류가 발생하는지 모르겠음
# 구글에도 나처럼 푼 사람 있던데...? ㅠㅠ