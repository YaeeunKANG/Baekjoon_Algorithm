'''01-13-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 7단계
   언어 - Python'''

# 11720
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = int(input())
temp = []
temp = int(input())
num = []
j = 10

while(len(num) != n):
    num.append(int((temp%j)/j*10))
    temp = temp - (temp%j)
    j = j * 10

sum = 0
for i in range(0, len(num)):
    sum = sum + num[i]

print(sum)



# 10809
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

alpha = []
for i in range(97, 123):
    alpha.append(chr(i))

result = []

temp = input()
S = list(temp)

for i in range(0, len(alpha)):
    if (alpha[i] in S) == True:
        result.append(S.index(alpha[i]))
    else:
        result.append(-1)

for i in range(0, len(result)):
    print(result[i], end=" ")