'''02-15-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 13단계
   언어 - Python'''



# 15652
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 
#        1부터 N까지 자연수 중에서 M개를 고른 수열
#        같은 수를 여러 번 골라도 된다.
#       고른 수열은 비내림차순이어야 한다.
#              - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []

def dfs(cnt):
    if(cnt == M):
        print(*arr)
        return
    
    for i in range(0, N):
        if(check_list[i]):
            continue
            
        arr.append(num_list[i])
        dfs(cnt + 1)
        check_list[i] = True
        arr.pop()
        
        for j in range(i + 1, N):
            check_list[j] = False
        
dfs(0)



# 9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 해결 못함

n = int(input())
s = [0 for i in range(16)]
result = 0
def isTrue(x):
    for i in range(1, x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x - i:
            return False
    return True
def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        for i in range(1, n + 1):
            s[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)
dfs(1)
print(result)