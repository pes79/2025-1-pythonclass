@ @-16

, 6 + 16, 9 @ @


def change_back_number(self, new_number):
    print(f'선수 번호 교체: {self.back_number} => {new_number}')
    self.back_number = new_number


def __str__(self):
    return f"저의 이름은 {self.name}, 위치는 {self.position}, 번호느 {self.back_number} 입니다. 화이팅"

    # SoccerPlayer 클래스가 jh 오브젝트를 생성함
    # 클래스의 생성함수 constructor가 실행됨


@ @-32

, 3 + 35, 33 @ @


def change_back_number(self, new_number):
    # 교체된 백넘버 확인
    print(f'{jh.back_number=}')

    names = ["Messi", "Ramos", "Ronaldo", "Park", "Son"]
    positions = ["MF", "DF", "CF", "WF", "GK"]
    numbers = [10, 9, 8, 7, 1]

    players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]
    print(players)
    print(players[0])

    # 첫번째 선수로 messi 생성
    messi = SoccerPlayer(players[0][0], players[0][1], players[0][2])
    print(messi.name)

    # 선수들의 리스트를 생성
    player_ojects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
    print(player_ojects[0])

    # 첫번째 선수의 이름
    print(player_ojects[0].name)

    # 모든 선수의 이름, 포지션, 번호 출력
    for player in player_ojects:
        print(player)

    # print(player_ojects[0])
    # print(player_ojects[1])
    # print(player_ojects[2])
    # print(player_ojects[3])
    # print(player_ojects[4])
