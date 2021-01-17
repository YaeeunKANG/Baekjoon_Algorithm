'''01-17-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 7단계
   언어 - Python'''



# 2941
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

temp = list(input())
alpha = []
count = 0

for i in range(0, len(temp)):
    index = i
    if temp[index] == '=' and i > 0:
        if temp[index-1] == 'c' or temp[index-1] == 's':
            alpha.append(temp[index-1]+temp[index])
            temp[index-1] = 0
            temp[index] = 0

        elif temp[index-1] == 'z' and (temp[index-2] != 'd'):
            alpha.append(temp[index-1]+temp[index])
            temp[index-1] = 0
            temp[index] = 0

        elif temp[index-1] == 'z' and (temp[index-2] == 'd') and i > 1:
            alpha.append(temp[index-2]+temp[index-1]+temp[index])
            temp[index-2] = 0
            temp[index-1] = 0
            temp[index] = 0
    
    elif temp[i] == '-' and i > 0:
        index = temp.index('-')
        if temp[index-1] == 'c' or temp[index-1] == 'd':
            alpha.append(temp[index-1]+temp[index])
            temp[index-1] = 0
            temp[index] = 0
    
    elif temp[i] == 'j' and i > 0:
        index = temp.index('j')
        if temp[index-1] == 'l' or temp[index-1] == 'n':
            alpha.append(temp[index-1]+temp[index])
            temp[index-1] = 0
            temp[index] = 0
        else:
            alpha.append(temp[index])
            temp[index] = 0

for i in range(0, len(temp)):
    if temp[i] != 0:
        alpha.append(temp[i])
        temp[i] = 0

print(len(alpha))



# 1316
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c,a,z,b가 모두 연속해서 나타나고, kin도 k,i,n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

'''n = int(input())

cnt = 0
for i in range(0, n):
    x = 0
    temp = list(input())
    for j in range(0, len(temp)-1):
        if temp[i] != temp[i+1]:
            cut = temp[i+1:]
            if temp[i] in cut:
                x += 1
        
        if x == 0:
            cnt += 1

print(cnt)'''
# 런타임 오류 발생

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)

# 구글 참조 // 기존의 코드에서 무엇이 런타임 에러를 발생시켰는지 잘 모르겠음 ㅠ