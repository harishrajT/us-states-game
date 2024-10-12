import turtle
from asyncio import all_tasks

import pandas


#setup screen
screen = turtle.Screen()
screen.title("U.S.States Game")

#set up image background
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

#import from csv file
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


guessed_states = []

while len(guessed_states) < 50:
    #getting input from user
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 Guess the other state",
                                    prompt="What's the other state?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states] # missed states by user
        # convert missed states to csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_Learn.csv")
        break

    if answer_state in states_list:  #check if it is in the csv file
        guessed_states.append(answer_state)
        t = turtle.Turtle()  #setup text box
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  #get coordinate of regarding state
        t.goto(int(state_data.x), int(state_data.y)) #move text box
        t.write(answer_state)


#end of code
