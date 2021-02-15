import math

rows= [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]
clear = "\n" * 100
game_on = True
user = 'X'

def display(rows):
  print(rows[0])
  print(rows[1])
  print(rows[2])

def get_user_input():
  user_input = ' '
  acceptable_range = range(1,10)
  within_range = False

  while user_input.isdigit() == False or within_range == False:
    user_input = input('Enter a number (1 - 9): ')

    if user_input.isdigit() == False:
      print('Sorry, that is not a digit! Try again!')
    else:
      if int(user_input) in acceptable_range:
        within_range = True
      else:
        print('Sorry, number out of acceptable range (1 - 9). Try again!')

  return int(user_input) - 1

def start_game():
  user_start = 'wrong'
  while user_start not in ['Y', 'N']:
    user_start = input('Would you like to keep playing? Y or N ').upper()
    if user_start not in ['Y', 'N']:
      print(clear)
      print('Please choose Y or N')
  
  if user_start == 'Y':
    return True
  else:
    return False
  
def change_slot():
  valid_input = False

  while valid_input == False:
    user_input = get_user_input()
    row = math.floor(user_input / 3)
    slot = user_input % 3
  
    if rows[row][slot] == ' ':
      rows[row][slot] = user
      valid_input = True
    else:
      print('Slot already taken. Choose a different slot (1 - 9).')


while game_on:
  display(rows)
  change_slot()
  user = 'O' if user == 'X' else 'X'

  game_on = start_game()