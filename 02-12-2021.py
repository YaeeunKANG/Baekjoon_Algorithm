'''02-12-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 12단계
   언어 - Python'''



# 10814
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

member_num = int(input())
member_list = []

for _ in range(member_num):
    member_age, member_name = map(str, input().split())
    member_age = int(member_age)
    member_list.append((member_age, member_name))

#나이 숫자 정렬 > 가입순 정렬
member_list.sort(key = lambda member: (member[0]))

for member in member_list:
    print(member[0], member[1])