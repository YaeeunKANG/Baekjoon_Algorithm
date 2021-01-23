'''01-23-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 9단계
   언어 - Python'''



# 1978
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

N = int(input())
temp = list(input().split( ))
cnt = 0

for i in range(0, N):
    x = int(temp[i])
    num = 0
    for j in range(1, x):
        if (x == 0):
            break
        elif (x%j == 0):
            num += 1
    if (num <= 2 and num != 0):
        cnt += 1

print(cnt)


##############
#### 오답 ####
##############

import math
num_count = int(input())
num_list = list(map(int, input().split(' ')))
natural_num = list(range(2,1001))                       # 자연수 범위를 정한다.(소수는 1이상인 정수이기때문에 1은 뺀상태)
count = 0
 
if len(num_list) == num_count:
    for i in range(2, math.ceil(math.sqrt(1000))):      # p²≥100인 p의 배수(p를 제외한)까지만 지우면 된다.
        for j in natural_num:            
            if j / i == 1:                              # 자기 자신으로 나뉘는것은 제외
                pass           
            elif j % i == 0:                            # 그 이외에 나뉘는 수가 존재하면
                natural_num.remove(j)                   # 그 수는 정수 리스트에서 제거
for k in num_list:
    if k in natural_num:                                # num_list에 natural_num이랑 중복되는 수가 있다면 count +1
        count += 1
print(count)


#####################################
###에라토스테네스의 체를 이용한 코드###
#####################################