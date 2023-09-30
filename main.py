import pandas
import turtle
from answer import Answer
import time

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)
screen.update()

# def get_mouse_click_coor(x,y):
#   print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv('./50_states.csv')
all_states = data.state.to_list()
guessed_states = []
while(len(guessed_states) < 50):
  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
  if answer_state == 'Exit':
    missing_states = []
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break
  coordinates = data[data.state == answer_state]
  if(not coordinates.empty):
    print(coordinates.x.to_numpy()[0])
    print_answer = Answer(coordinates.state.to_numpy()[0], coordinates.x.to_numpy()[0], coordinates.y.to_numpy()[0])
    guessed_states.append(coordinates.state.to_numpy()[0])
  screen.update()
  time.sleep(0.1)


