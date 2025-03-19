


from math import gamma #2025 03 19
#파이썬 수업, 조건문

score = int(input("점수를 입력하세요: "))
if score >= 60:
    grade = "합격"
    print(grade)
elif score > 50:
    grade = "임시합격"
    print(grade)
else:
    grade = "불합격"
    print(grade)





score = int(input("점수를 입력하세요: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(grade)

score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'  # 90 이상일 경우 A
elif score >= 80:
    grade = 'B'  # 80 이상일 경우 B
elif score >= 70:
    grade = 'C'  # 70 이상일 경우 C
elif score >= 60:
    grade = 'D'  # 60 이상일 경우 D
else:
    grade = 'F'  # 모든 조건에 만족하지 못할 경우 F

print(grade)

#money = True
#if money:
 #   print("택시를 타고 가라")
#else:
 #   print("걸어 가라")



