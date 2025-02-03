from turtle import Turtle

class StatesClass(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.state_name = ''
        self.state_amount = 0
        self.state_x_position = 0
        self.state_y_position = 0
        self.pencolor("black")
        self.goto(self.state_x_position, self.state_y_position)

    def update_state_name(self, name):
        self.write(name, align="center", font=("Arial", 10, "bold"))

