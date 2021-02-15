import math

rows = [
  ' ', ' ', ' ',
  ' ', ' ', ' ',
  ' ', ' ', ' '
]
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
clear = "\n" * 100
game_on = True
user = 'X'
win = False
draw = False

def display(rows):
  print(f'{rows[0]}|{rows[1]}|{rows[2]}')
  print('-----')
  print(f'{rows[3]}|{rows[4]}|{rows[5]}')
  print('-----')
  print(f'{rows[6]}|{rows[7]}|{rows[8]}')

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
  
    if rows[user_input] == ' ':
      print(clear)
      rows[user_input] = user
      valid_input = True
    else:
      print(clear)
      display(rows)
      print('Slot already taken. Choose a different slot (1 - 9).')

def check_win():
  for combo in winning_combos:
    if user == rows[combo[0]] == rows[combo[1]] == rows[combo[2]]:
      display(rows)
      print(f'{user} won!')
      return True
  return False

def check_draw():
  for slot in rows:
    if slot == ' ':
      return False
  if win != True:
    display(rows)
    print('Game is a draw!')
    return True

while game_on:
  display(rows)
  change_slot()
  win = check_win()
  draw = check_draw()
  user = 'O' if user == 'X' else 'X'

  if win or draw:
    game_on = start_game()
    print(clear)
    if game_on:
      user = 'X'
      rows = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']