'''02-14-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 13단계
   언어 - Python'''



# 15650
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
#       1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#       고른 수열은 오름차순이어야 한다.

N, M = map(int, input().split())
visited = [False] * N
out, out_all = [], []

def solve(depth, N, M):
    if depth == M:
        out_str = ' '.join(map(str, sorted(out)))
        if out_str not in out_all:
            out_all.append(out_str)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()
solve(0, N, M)

for i in out_all:
    print(i)



# 15651
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 
#        1부터 N까지 자연수 중에서 M개를 고른 수열
#        같은 수를 여러 번 골라도 된다.

N, M = map(int, input().split())
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(i+1)
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)