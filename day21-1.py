'''--- Day 21: Scrambled Letters and Hash ---

The computer system you're breaking into uses a weird scrambling function to store its passwords. It shouldn't be much trouble to create your own scrambled password so you can add it to the system; you just have to implement the scrambler.

The scrambling function is a series of operations (the exact list is provided in your puzzle input). Starting with the password to be scrambled, apply each operation in succession to the string. The individual operations behave as follows:

    swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
    swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
    rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
    rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
    reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
    move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.

For example, suppose you start with abcde and perform the following operations:

    swap position 4 with position 0 swaps the first and last letters, producing the input for the next step, ebcda.
    swap letter d with letter b swaps the positions of d and b: edcba.
    reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
    rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of the string: bcdea.
    move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
    move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
    rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
    rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.

After these steps, the resulting scrambled password is decab.

Now, you just need to generate a new scrambled password and you can access the system. Given the list of scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?
'''


INPUT = 'abcdefgh'


def swap(password, position1, position2):
  ''' input- password : str. 
      output - returns password with chars in position1 and 2 swapped
  '''
  if position1 <= position2:
    return password[:position1] + password[position2] + password[position1+1:position2] + password[position1] + password[position2+1:]
  else:
    return password[:position2] + password[position1] + password[position2+1:position1] + password[position2] + password[position1+1:]


def rotate(password, direction, steps):
  '''
  inputs- 
  password: str
  direction: str , either "left" or "right"
  steps: int, 0 or greater
  output-  returns str.
  '''
  steps = steps % len(password)
  if direction == "right":
    return password[-steps:] + password[:-steps]
  else:
    return password[steps:] + password[:steps]


def reverse(password, position1, position2):
  '''
  inputs-
  password: str
  position1 and position2: int. 
  outputs - returns str
  '''
  return password[:position1] + password[position2:position1:-1] + password[position1] + password[position2+1:]


def swapletters(password, char1, char2):
  '''
  inputs-
  password:str
  char1, char2: str
  output - returns str
  '''
  index1 = password.find(char1)
  index2 = password.find(char2)
  return swap(password, index1, index2)


def move(password, source, destination):
  '''
  inputs-
  password: str
  source, destination: str. index of password string to move from and to
  output- returns str
  '''
  letter = password[source]
  password = password.replace(letter, '*')  #replaces letter with placeholder
  if destination < source:
    password = password[:destination] + letter + password[destination:]
    return password.replace('*', '')
  else:
    password = password[:destination+1] + letter + password[destination+1:]
    return password.replace('*', '')


def rotate_pos(password, letter):
  '''
  inputs-
  password, letter: str
  outputs- str
  '''
  index = password.find(letter)
  if index >= 4:
    return rotate(password, "right", index+2)
  else:
    return rotate(password, "right", index+1)

if __name__ == "__main__":
  with open("day21input.txt") as fp:
    instructions = fp.readlines()
    for instruction in instructions:
      parse = instruction.rstrip('\n').split(" ")
      if parse[0] == "swap" and parse[1] == "position":
        print("INPUT is {}. Swapping pos {} & {}".format(INPUT, parse[2], parse[5]))
        INPUT = swap(INPUT, int(parse[2]), int(parse[5]))
        print("INPUT is {} after swapping".format(INPUT))
      elif parse[0] == "swap" and parse[1] == "letter":
        print("INPUT is {}. Swapping letter {} & {}".format(INPUT, parse[2], parse[5]))
        INPUT = swapletters(INPUT, parse[2], parse[5])
        print("INPUT is {} after swapping".format(INPUT))
      elif parse[0] == "rotate" and len(parse) == 4:
        print("INPUT is {}. Rotating {} by {}".format(INPUT, parse[1], parse[2]))
        INPUT = rotate(INPUT, parse[1], int(parse[2]))
        print("INPUT is {} after rotating".format(INPUT))
      elif parse[0] == "reverse":
        print("INPUT is {}. Reversing {} through {}".format(INPUT, parse[2], parse[4]))
        INPUT = reverse(INPUT, int(parse[2]), int(parse[4]))
        print("INPUT is {} after reversing".format(INPUT))
      elif parse[0] == "move":
        print("INPUT is {}. Moving pos {} to {}".format(INPUT, parse[2], parse[5]))
        INPUT = move(INPUT, int(parse[2]), int(parse[5]))
        print("INPUT is {} after moving".format(INPUT))
      elif parse[0] == "rotate" and parse[1] == "based":
        print("INPUT is {}. Rotating on letter {}".format(INPUT, parse[6]))
        INPUT = rotate_pos(INPUT, parse[6])
        print("INPUT is {} after rotating".format(INPUT))
  


  print(INPUT)
