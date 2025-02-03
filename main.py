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
correct_states_list = []


while len(correct_states_list) < 50:
    answer_state = screen.textinput(f"{len(correct_states_list)}/50 - Gues the State", "What is another state name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        state_name_in_file = data[data.state == answer_state]
        states.state_name = state_name_in_file
        states.goto(state_name_in_file.x.item(), state_name_in_file.y.item())
        states.update_state_name(answer_state)
        correct_states_list.append(answer_state)


# creating a csv file with those states that were forgotten:
list_forgotten_states = []
for state in states_list:
    if state not in correct_states_list:
        list_forgotten_states.append(state)
states_lo_learn = {
    "learn" : list_forgotten_states
}
data = pandas.DataFrame(states_lo_learn)
data.to_csv("states-to-learn.csv")





