from turtle import Turtle
ALIGN = 'center'
FONT = ("Arial", 16, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 295)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.game_score}   High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)


    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.game_score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color('red')
    #     self.write(f'GAME OVER', align=ALIGN, font = FONT)


    def increase_score(self):
        self.game_score+=1
        self.clear()
        self.update_score()

