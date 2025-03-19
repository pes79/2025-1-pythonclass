#2025.3.18
#파이썬 리스트 : 한개의 변수에 여러 값을 할당
from operator import index

#인덱싱
colors = ['red', 'blue','green']
print(colors) #리스트 전체 출력
print(colors[1]) #리스트 0,1 두번째 원소
print(colors[-1]) #리스트 마지막 원소 출력
print(len(colors)) #리스트의 길이 출력

#슬라이싱
cities = ['서울','부산','인천','의정부','대전','강릉','논산','포항']
print(cities[0:5]) #cities [0:n] 0~n-1까지 표시
print(cities[:7])#0,1,2,3,4,5,6
print(cities[:-1])#0부터 -2
print(cities[3:])#뒤에를 안쓰면 끝까지
print(cities[:]) #전부 표시
print(cities[-4:])#뒤에서 4번째 부터 표시
print(cities[:7:2])# 처음 부터 6번째 원소 까지 한 칸 씩 건너 뜀
print(cities[::3]) #처음부터 끝까지 3칸씩 건너뜀
print(cities[::-1])#처음부터 끝까지 but 방향은 반대
print(cities[4::-2])
print(len(cities))

# 리스트의 추가
#colors = ['red', 'blue','green']
#colors.append('white')
#print(colors[:])
#colors.extend(['black','purple'])
#print(colors[index:1,object:'orange'])
#print(colors[:])
#colors.remove('purple')
#print(colors[:])
#colors[1] = 'sky'
#print(colors[:])

# 패킹, 언패킹
#c1,c2,c3,_ ,_,_= colors
#print(c1,c2,c3)


#퀴즈

first = ["egg","salad","bread","soup","canafe"]
second = ["fish","lamb","pork","beef","chicken"]
third = ["apple","banana","orange","grape","mango"]

order = [first,second,third]
john = [order[0][:-2],second[1::3],third[0]]   #john = [soup,[lamb,chicken],apple]
del john[2]  #john = [soup,[lamb,chicken]]
john.extend([order[2][0:1]]) #john = [soup,[lamb,chicken,apple]
print(john)

# 다차원 리스트

colors = ['red','blue','green']
cities = ['서울','부산','인천','의정부','대전','강릉','논산','포항']
combi = [colors, cities]
print(combi[1][2]) #인천
#print(combi[2][3]) #에러 발생
bigcombi = [combi,[0,2,7]]
print(bigcombi)
print(len(bigcombi))
print(bigcombi[0][1][2]) #인천
print(bigcombi[1][1]) #2







