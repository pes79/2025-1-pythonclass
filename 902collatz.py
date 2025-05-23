# 2025.4.2 파이썬 수업 프로젝트 두 번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자 중, 가장 많은 단계를 거쳐서 1로가는 수는 무엇 인가?, 가장 많은 단계는 몇 단계 인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3*n+1
# 예: 5 -> 16 ->8 ->4 ->2 ->1  (5단계)


#단계의 갯수를 셀 것
#n을 1부터 99까지 변화하면서, 각각의 단계 수를 출력할 것
#그 중 가장 큰 수를 찾을 것
# n=97: 118번만에 도착
# n= 73 115번만에 도착
# 세 번째로 큰 단계 수는 112번이고, 해당 n값은 54입니다.

maxvalue = 0
maxvaluen = 0
second_maxvalue = 0
second_maxvaluen = 0
third_maxvalue = 0
third_maxvaluen = 0

for n in range(1, 100):
    ncount = 0
    i = n
    while i != 1:
        if i % 2 == 1:
            i = 3 * i + 1
        else:
            i = i / 2
        ncount += 1

    if ncount > maxvalue:
        third_maxvalue = second_maxvalue
        third_maxvaluen = second_maxvaluen
        second_maxvalue = maxvalue
        second_maxvaluen = maxvaluen
        maxvalue = ncount
        maxvaluen = n
    elif ncount > second_maxvalue:
        third_maxvalue = second_maxvalue
        third_maxvaluen = second_maxvaluen
        second_maxvalue = ncount
        second_maxvaluen = n
    elif ncount > third_maxvalue:
        third_maxvalue = ncount
        third_maxvaluen = n

print(f'세 번째로 큰 단계 수는 {third_maxvalue}번이고, 해당 n값은 {third_maxvaluen}입니다.')


