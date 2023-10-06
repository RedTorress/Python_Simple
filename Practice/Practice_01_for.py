# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}*{i}={dan * i}") # 전체주석 -> 컨트롤 /


# 문제2) 2단부터 9단까지 출력(중첩 for문)
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")

# 문제3) list a 의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
total = 0
for num in a:
    total += num # total = total + num
# a 길이 => len(a)
result = total / len(a)


#round(값, 자리수) : 자리수만큼 반올림
print(round(result, 2)) # 평균값 출력

# 문제4) list b 에서 최소값 찾기
b = [22, 1, 4, 7, 98]
n = len(b)
for i in range(n):
    for j in range(n-i-1):
        if(b[j]>b[j+1]):
             b[j],b[j+1] = b[j+1], b[j]
num_min = b[0]
print(num_min) # 1 출력
