#2025.3.26.2학년 1학기  파이썬수업
#순환문 (반복문)

for looper in [1, 2, 3, 5, 'end']:
    print(f'{looper}')


cities = ['서울','부산','인천','의정부','대전','강릉','논산','포항']
for city in cities:
    print(f'{city=}')

for i in range(3):
    print(i)

for i in range(1, 10, 2):
    print(i)

string = 'python'
for c in string:
    print(c)

i = 1
while i < 10:
    print(f'{i=}')
    i = i + 2;

    # 1부터 100까지의 홀수 합 구하기
sum = 0

for i in range(1, 101, 2):
    sum += i

print(f'{sum=}')


sum = 0

for i in range(2, 101, 2):
    sum += i

print(f'{sum=}')

#1부터 100까지 짝수의 합을 while문으로 구하기
sum = 0
i = 2

while i <= 100:
    sum += i
    i += 2

print(f'{sum=}')


