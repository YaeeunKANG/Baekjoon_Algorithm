'''02-16-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 13단계
   언어 - Python'''



# 2580
# 스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다.
# 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 
# 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.
# 나머지 빈 칸을 채우는 방식은 다음과 같다.
# 
#       각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
#       굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 
# 게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

import sys
r = sys.stdin.readline

# 가로 체크
def horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True

# 세로 체크
def vertical(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True

# 3x3 체크
def bythree(x, y, val):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx+i][ny+j]:
                return False
    return True


def DFS(index):
    if index == len(zeros):
        for row in sudoku:
            for n in row:
                print(n, end=" ")
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            nx = zeros[index][0]
            ny = zeros[index][1]

            # 세로, 가로, 3x3에 내가 대체하려고하는 숫자가 존재하는지 확인
            if horizontal(nx, i) and vertical(ny, i) and bythree(nx, ny, i):
                sudoku[nx][ny] = i
                DFS(index+1)
                sudoku[nx][ny] = 0


sudoku = [list(map(int, r().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
DFS(0)