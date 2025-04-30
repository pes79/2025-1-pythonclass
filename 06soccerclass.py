class SoccerPlayer:
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print(f'선수 번호 교체: {self.back_number} => {new_number}')
        self.back_number = new_number

    def __str__(self):
        return f"저의 이름은 {self.name}, 위치는 {self.position}, 번호는 {self.back_number} 입니다. 화이팅"


def change_back_number(self, new_number):
    print(f'{self.back_number=}')  # self로 수정

    names = ["Messi", "Ramos", "Ronaldo", "Park", "Son"]
    positions = ["MF", "DF", "CF", "WF", "GK"]
    numbers = [10, 9, 8, 7, 1]

    players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]
    print(players)
    print(players[0])

    messi = SoccerPlayer(players[0][0], players[0][1], players[0][2])
    print(messi.name)

    player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
    print(player_objects[0])
    print(player_objects[0].name)

    for player in player_objects:
        print(player)

