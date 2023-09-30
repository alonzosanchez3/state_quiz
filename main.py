import pandas
import turtle
from answer import Answer

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#   print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv('./50_states.csv')
game = True
while(game):
  answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name")
  print(answer_state)
  coordinates = data[data.state == answer_state.capitalize()]
  print(coordinates.x.to_numpy()[0])
  print_answer = Answer(coordinates.x.to_numpy()[0], coordinates.y.to_numpy()[0])
