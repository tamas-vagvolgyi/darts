class Player:

    def_points = 501
    wins = 0

    def __init__(self, name, points = def_points):
        self.name = name
        self.points = points
        self.info()

    def info(self):
        print("Player name: " + self.name + ", Remaining points: " + str(self.points))

    def get_points(self):
        print(self.points)

    def set_points(self, value):
        self.points = int(value)

    def reset(self):
        self.set_points(501)
        self.is_winner = False

    def is_winner(self):
        return(self.is_winner)

    def get_score(self):
        return(self.wins)

    def throw(self):
        pts_before_round = self.points
        throws = 3

        for i in range(throws):

            # The value must start with s, d, t and then the number
            value = input("Value thrown by " + self.name +": ").lower()
            if value == 'q':
                print("Bye!")
                exit()
            elif value == '0':
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

            number = int(value[1:])
            if number <= 20:
                if number > 0:
                    pass
            else:
                print("Please give a valid value")

            value = number*multi

            if value > self.points:
                self.points = pts_before_round
            else:
                self.points -= value
                if self.points == 1:
                    self.points = pts_before_round
                    print(self.name + " threw too much...")
                    break
                elif self.points == 0:
                    print(self.name + " is the winner!")
                    self.is_winner = True
                    self.wins += 1
                    break

        self.info()

    is_winner = False

class Game:

    def __init__(self):
        numplayers = int(input("How many players will be playing?: "))
        self.players = []
        for i in range(numplayers):
            playername = input("What's the name of the " + str(i+1) + ". player?: ")
            self.players.append(Player(playername))
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
                player.reset()
            self.play()
        else:
            print("Thank you for playing with us today!")
            exit()

    def score(self):
        for player in self.players:
            print(player.name + ": " + str(player.get_score()))

game = Game()


"""
Todo:
- While loop
- Double exit
- Saving things to json
"""
