# 2025-1-파이썬 수업
이용희 교수님
- 목표:
- 1.머신러닝을 잘 하기 위해
- 2.객체지향개념을 연습하기 위해
- 3.ADP 실기시험을 위해
- 4.코딩테스트를 위해

## 깃허브와 파이참의 연동 실험
파이참의 파일메뉴 -> 버전관리에 있는 프로젝트 -> Github 선택
->원하는 repository 선택(2025-1 pythonclass) -> 원하는 디렉터리 선택
-> **복제 선택**

## 변수와 자료형
 - 정수 int
 - 실수 float
 - 문자형 str
 - 논리형 bool
## 리스트
한개의 변수에 여러 값을 할당 한다.
 - 인덱싱, 슬라이싱
 - 리스트의 연산 - 덧셈, 곱셈, append,insert,remove

## 조건문
 - if, else, elif

## 반복문
 - for
 - while


# 프로젝트 1 : 파이 값 구하기
파이 값을 구하고 그래프로 그림
![img.png](img.png)

```
p=1
pilist = []

for n in range(1,200):
    p = p * ((2 * n + 1) ** 2 - 1) / (2 * n + 1) ** 2
    #print(p*4,',')
    pilist.append(p*4)


import matplotlib.pyplot as plt
plt.plot (pilist)
plt.show()
```
![img_1.png](img_1.png)