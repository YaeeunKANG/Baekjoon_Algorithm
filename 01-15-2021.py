'''01-15-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 7단계
   언어 - Python'''



# 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

'''
temp = input()
temp = list(temp)

alpha = []
count = []

for i in range(97, 123):
    alpha.append(chr(i))
    count.append(0)

for i in range(0, len(temp)):
    if temp[i] in alpha:
        index = alpha.index(temp[i])
        count[index] = count[index] + 1
    
    else:
        another = chr(ord(temp[i]) + 32)
        if another in alpha:
            index = alpha.index(another)
            count[index] = count[index] + 1

Max = count[0]
flag = 0

for i in (1, len(count)-1):
    if count[i] == Max:
        flag = 1
        temp2 = Max
    elif count[i] > Max:
        Max = count[i]

if (flag == 1) and (Max == temp2):
    print('?')
else:
    index = count.index(Max)
    print(chr(ord(alpha[index])-32))
'''

words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])