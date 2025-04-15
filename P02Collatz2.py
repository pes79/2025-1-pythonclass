import numpy as np
import statistics
import time
from collections import Counter

# collatz 함수 직접 정의
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
    ncountl.append(ncount)

print(f'[리스트 방식]')
print(f'최대값={max(ncountl)}')
print(f'평균={statistics.mean(ncountl):.5f}')
print(f'중앙값={statistics.median(ncountl)}')
print(f'표준편차={statistics.stdev(ncountl):.5f}')
mode_val = Counter(ncountl).most_common(1)[0][0]
print(f'최빈값={mode_val}')
end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다\n')

# numpy 방식
start = time.time()
ncounta = np.zeros(MAXNUM - 1, dtype=int)

for n in range(1, MAXNUM):
    ncount = collatz(n)
    ncounta[n - 1] = ncount

print(f'[NumPy 방식]')
print(f'최대값={np.max(ncounta)}')
print(f'평균={np.mean(ncounta):.5f}')
print(f'중앙값={np.median(ncounta)}')
print(f'표준편차={np.std(ncounta):.5f}')
mode_val_np = np.bincount(ncounta).argmax()
print(f'최빈값={mode_val_np}')
end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다')
