from turtle import Screen, Turtle
import pandas as p
screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.title("Find US States")

states = p.read_csv("50_states.csv")
state_list = states["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    ans = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                           prompt="Enter the State Name ").title()
    if ans == 'Exit':
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        not_rem_data = p.DataFrame(missing_states)
        not_rem_data.to_csv("states_to_learn.csv")
        break
    if ans in state_list:
        guessed_states.append(ans)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == ans]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans)



