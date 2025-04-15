import numpy as np
import statistics
import time
from collections import Counter

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

MAXNUM = 100

# 리스트 방식
start = time.time()
ncountl = []

for n in range(1, MAXNUM):
    ncount = collatz(n)
    ncountl.append((n, ncount))  # 튜플로 저장 (숫자, 단계 수)

# 정렬하여 빅 3 추출
top3_list = sorted(ncountl, key=lambda x: x[1], reverse=True)[:3]

print(f'[리스트 방식]')
steps_only = [s[1] for s in ncountl]
print(f'최대값={max(steps_only)}')
print(f'평균={statistics.mean(steps_only):.5f}')
print(f'중앙값={statistics.median(steps_only)}')
print(f'표준편차={statistics.stdev(steps_only):.5f}')
mode_val = Counter(steps_only).most_common(1)[0][0]
print(f'최빈값={mode_val}')
print(f'빅 3: {top3_list}')
end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다\n')

# numpy 방식
start = time.time()
ncounta = np.zeros(MAXNUM - 1, dtype=int)

for n in range(1, MAXNUM):
    ncounta[n - 1] = collatz(n)

print(f'[NumPy 방식]')
print(f'최대값={np.max(ncounta)}')
print(f'평균={np.mean(ncounta):.5f}')
print(f'중앙값={np.median(ncounta)}')
print(f'표준편차={np.std(ncounta):.5f}')
mode_val_np = np.bincount(ncounta).argmax()
print(f'최빈값={mode_val_np}')

# 빅 3 구하기: (숫자, 단계 수) 튜플 리스트 생성
top3_np = sorted([(i + 1, ncounta[i]) for i in range(len(ncounta))], key=lambda x: x[1], reverse=True)[:3]
print(f'빅 3: {top3_np}')
end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다')
