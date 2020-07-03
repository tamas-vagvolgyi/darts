class Player:

    wins = 0

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.info()

    def info(self):
        print("Player name: " + self.name + ", Remaining points: " + str(self.points))

    def get_points(self):
        print(self.points)

    def set_points(self, value):
        self.points = int(value)

    def reset(self, points):
        self.set_points(points)
        self.is_winner = False

    def is_winner(self):
        return(self.is_winner)

    def get_score(self):
        return(self.wins)

    def throw(self):
        pts_before_round = self.points
        throw = 0

        while throw < 3:
            # The value must start with s for single, d for double, t for treble and then the number, e.g.: s20, d16, t19
            value = input("Value thrown by " + self.name +": ").lower()
            if value == 'q':
                print("Bye!")
                exit()
            elif value == '0':
                throw += 1
                continue

            multiplier = value[0]
            multi = 0
            if multiplier == 's':
                multi = 1
            elif multiplier == 'd':
                multi = 2
            elif multiplier == 't':
                multi = 3
            else:
                print("Please give a valid value")
                continue

            number = int(value[1:])
            if number == 25:
                pass
            elif number <= 20:
                if number > 0:
                    pass
                else:
                    print("Please give a valid value")
                    continue
            else:
                print("Please give a valid value")
                continue

            value = number*multi
            if value > self.points:
                self.points = pts_before_round
                break
            else:
                self.points -= value
                if self.points == 1:
                    print(self.name + " threw too much...")
                    self.points = pts_before_round
                    break
                elif self.points == 0:
                    if multi == 2:
                        print(self.name + " is the winner!")
                        self.is_winner = True
                        self.wins += 1
                        break
                    else:
                        print(self.name + " didn't finish with a Double")
                        self.points = pts_before_round
                        break
            throw += 1

        self.info()

    is_winner = False

class Game:

    def __init__(self, points):
        numplayers = int(input("How many players will be playing?: "))
        self.points = points
        self.players = []
        for i in range(numplayers):
            playername = input("What's the name of the " + str(i+1) + ". player?: ")
            self.players.append(Player(playername, points))
        self.play()

    def play(self):
        for player in self.players:
            player.throw()
            if player.is_winner:
                self.score()
                self.play_again()
        self.play()

    def play_again(self):
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            for player in self.players:
                player.reset(self.points)
            self.play()
        else:
            print("Thank you for playing with us today!")
            exit()

    def score(self):
        for player in self.players:
            print(player.name + ": " + str(player.get_score()))

game = Game(101)
