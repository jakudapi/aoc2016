"""
--- Day 8: Two-Factor Authentication ---
--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

"""

from time import time
import numpy as np


def shifter(array, amount):
  """
  array: np.array[int]
  amount: int. times to shift
  OUTPUT-
  returns np.array[int]
  """

  amount = amount % len(array) 
  return np.concatenate((array[-amount:], array[:-amount]))


def rect(screen, num_cols, num_rows):
  """
  screen: np.array representing the screen
  num_cols: int. 
  num_rowls: int
  OUTPUT-
  none
  """
  screen[:num_rows, :num_cols] = '#'  # turns pixels on


def rotate(screen, axis, index, shift):
  """
  screen: np.array representing the screen
  axis: str. either "row" or "column
  index: int. what "row" or "column" 
  shift: int. how much to shift (wraps around end)
  OUTPUT-
  none
  """
  if axis == 'row':
    screen[index] = shifter(screen[index], shift)
  elif axis == 'column':
    screen[:,index] = shifter(screen[:,index], shift)


with open("day08input.txt") as fp:
  screen = np.zeros((6,50), dtype=str)  #initialize blank screen. 6 rows, 50 cols.
  screen.fill('_')
  for line in fp:
    instruction = line.rstrip("\n").split(" ")  # split line into list of words
    if instruction[0] == 'rect':
      coordinates = instruction[1].split('x')  # ie '12x3' => ['12','3']
      rect(screen, num_cols=int(coordinates[0]), num_rows=int(coordinates[1]))
    elif instruction[0] == "rotate":
      index = int(instruction[2].split('=')[1])  #  'x=32'=> ['x','32']=> 32
      rotate(screen, axis=instruction[1], index=index, shift=int(instruction[4]))
  #print("Pixels on: {}".format(screen.sum()))
  for x in range(5,51,5):
    print(screen[:,x-5:x])
