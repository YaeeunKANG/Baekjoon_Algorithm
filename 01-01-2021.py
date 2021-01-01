'''01-01-2021 Baekjoon Algorithm
   단계별 문제 풀이 - 1단계
   언어 - Python'''



# 2557
# Hello World!를 출력하시오.

print("Hello World!")



# 10718
# ACM-ICPC 인터넷 예선, Regional, 그리고 World Finals까지 이미 2회씩 진출해버린 kriii는
# 미련을 버리지 못하고 왠지 모르게 올 해에도 파주 Worlds Fianls 준비 캠프에 참여했다.
#
# 대회를 뜰 줄 모르는 지박령 kriii를 위해서 격려의 문구를 출력해주자.

for i in range(0,2):
    print("강한친구 대한육군")



# 10171
# 아래 예죄와 같이 고양이를 출력하시오.
# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")



# 10172
# 아래 예제와 같이 개를 출력하시오.
# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|

print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`   |")
print("||_/=\\__|")



# 1000
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

temp = []
temp = input().split()
A = int(temp[0])
B = int(temp[1])
print(A+B)