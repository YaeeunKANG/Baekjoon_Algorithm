'''01-16-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 7단계
   언어 - Python'''



# 1152
# 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까?
# 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

temp = input().split( )
print(len(temp))



# 2908
# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다.
# 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다.
# 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수 를 말해보라고 했다.
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서 상수는 두 수 중 큰 수인 437을 큰 수라고 말할 것이다.
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

temp = input().split( )
sangsu_list1 = list(temp[0])
sangsu_list2 = list(temp[1])

sangsu_list1.reverse()
sangsu_list2.reverse()

sangsu_1 = "".join(sangsu_list1)
sangsu_2 = "".join(sangsu_list2)

sangsu_1 = int(sangsu_1)
sangsu_2 = int(sangsu_2)

if sangsu_1 > sangsu_2 :
    print(sangsu_1)
else:
    print(sangsu_2)



# 5622
# 상근이의 할머니는 오래된 다이얼 전화기를 사용한다.
# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나 누른 다음에 금속 핀이 있는 곳까지 시계방향으로 돌려야 한다.
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화번호를 각 숫자에 해당하는 문자로 외운다. 즉 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다.
# 예를 들어, UNUCIC는 868242와 같다.
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

word = list(input())
number = []

for i in range(0, len(word)):
    word[i] = ord(word[i])
    if 64 < word[i] <= 67:
        number.append(2)
    elif 67 < word[i] <= 70:
        number.append(3)
    elif 70 < word[i] <= 73:
        number.append(4)
    elif 73 < word[i] <= 76:
        number.append(5)
    elif 76 < word[i] <= 79:
        number.append(6)
    elif 79 < word[i] <= 83:
        number.append(7)
    elif 83 < word[i] <= 86:
        number.append(8)
    elif 86 < word[i] <= 90:
        number.append(9)
    elif 90 < word[i] <= 96:
        number.append(0)

time = 0

for i in range(0, len(number)):
    time += (number[i]+1)

print(time)