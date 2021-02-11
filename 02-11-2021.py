'''02-11-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 12단계
   언어 - Python'''



# 1181
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

voca_list = []
for i in range(int(input())):              
    voca_list.append(input())               
 
set_voca_list = list(set(voca_list))       
sort_voca_list = []
 
for j in set_voca_list:
    sort_voca_list.append((len(j), j))     
 
sort_voca_list.sort()                      
 
for len_voca, voca in sort_voca_list:       
    print(voca)