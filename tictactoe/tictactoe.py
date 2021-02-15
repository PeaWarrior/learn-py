row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def display(row1, row2, row3):
  print(row1)
  print(row2)
  print(row3)

def get_user_input():
  user_input = ' '
  acceptable_range = range(1,9)
  within_range = False

  while user_input.isdigit() == False or within_range == False:
    user_input = input('Enter a number (1 - 9): ')

    if user_input.isdigit() == False:
      print('Sorry, that is not a digit! Try again!')
    else:
      if int(user_input) in acceptable_range:
        within_range = True
      else:
        print('Sorry, number must be 1 - 9. Try again!')

  return int(user_input)

display(row1, row2, row3)
get_user_input()