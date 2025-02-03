import turtle
import pandas
from states_class import StatesClass

screen = turtle.Screen()
screen.title("U.S Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
states = StatesClass()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

states.state_amount = 0
while states.state_amount < 50:
    answer_state = screen.textinput(f"{states.state_amount}/50 - Gues the State", "What is another state name?").title()
    print(answer_state)
    if answer_state in states_list:
        state_name_in_file = data[data.state == answer_state]
        print(state_name_in_file)
        states.state_name = state_name_in_file
        states.goto(state_name_in_file.x.item(), state_name_in_file.y.item())
        states.update_state_name(answer_state)
        states.state_amount += 1


turtle.mainloop()



