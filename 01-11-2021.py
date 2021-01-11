''' 01-11-2021 Baekjoon Algorithm
    단계별 문제 풀이 - 6단계
    언어 - Python '''

# 4673
# 셀프 넘버는 1949년도 인도 수학자 D.R.Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
# 예를 들어, d(75) = 75 + 7 + 5 = 87 이다.
# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ... 과 같은 무한 수열을 만들 수 있다.
# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다.
# 이런식으로 다음과 같은 수열을 만들 수 있다. 33, 39, 51, 57, 69, 84, ...
# n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다.
# 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개( 91과 100 )이 있다.
# 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

'''
def d(n):
    self_num = []
    for i in range(1, n):
        self_num.append(i)

    for i in range(1,n):
        temp = i
        while(0<temp<10000):
            if(0 < temp < 10):
                temp = temp + (temp%10)
                if(self_num.count(temp)!=0):
                    self_num.remove(temp)
            elif(10 <= temp < 100):
                temp = temp + (int(temp/10)) + (temp%10)
                if(self_num.count(temp)!=0):
                    self_num.remove(temp)
            elif(100 <= temp < 1000):
                temp = temp + (int(temp/100)) + (int(temp/10)%10) + (temp%10)
                if(self_num.count(temp)!=0):
                    self_num.remove(temp)
            elif(1000 <= temp < 10000):
                temp = temp + (int(temp/1000)) + (int(temp/100)%10) + (int(temp/10)%10) + (temp%10)
                if(self_num.count(temp)!=0):
                    self_num.remove(temp)
            elif(temp>=10000):
                break
    
    for i in range(0, len(self_num)):
        print(self_num[i])

d(10000)
'''

# 나의 오답 : 런타임에러 발생

def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x) 
    return int(n) + a
a= []
for i in range(1,10001):
    k = d(i)
    a.append(k)

for b in range(1, 10001):
    if b in a:
        pass
    else:
        print(b)

