import random


class Coinflips:

    def __init__(self):
        self.__picks = []
        self.__correct = 0

    def play(self, guess):
        if guess != "heads" and guess != "tails":
            raise Warning
        choices = ["heads", "tails"]
        choice = random.choice(choices)

        self.__picks.append(choice)
        if guess == choice:
            self.__correct += 1
        return choice


    def winner(self):
        if self.__correct > len(self.__picks)//2:
            return True
        return False

    def __str__(self):
        res = ""
        for j,i in enumerate(self.__picks):
            res += i
            if j < len(self.__picks)-1:
                res += ","
        return res


t = Coinflips()
try:
    t.play("arms")
except Warning:
    print("invalid choice")
# Your play results may be different from this example due to randomness
print(t.play("heads"))
print(t.play("tails"))
print(t.play("heads"))
print(t)
print(t.winner())