# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1   (5단계)

n = 9

# 단계의 갯수를 셀것 - done
# n을 1부터 99까지 변화하면서, 각각의  단계수를 출력할 것
# 그중 가장 큰 수를 찾을 것
# n=97: 118번만에 1로 도달
# n=73: 115번만에 1로 도달

maxvalue1 = -100
maxvalue2 = -100
maxvaluen1 = 0
maxvaluen2 = 0

for n in range(1,100000):
    # print(f'{n=}')
    ncount = 0
    i = n

    while i!= 1:
        if i % 2 == 1:
            i = 3 * i + 1
        else:
          i = i / 2
        ncount = ncount + 1

    print(f'{ncount}')
    if maxvalue1  < ncount:
        maxvalue2 = maxvalue1
        maxvalue1 = ncount
        maxvaluen2 = maxvaluen1
        maxvaluen1 = n
    elif maxvalue2 < ncount:
        maxvalue2 = ncount
        maxvaluen2 = n

print(f'{maxvalue1=}, {maxvaluen1=}')
print(f'{maxvalue2=}, {maxvaluen2=}')