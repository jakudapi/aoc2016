"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
    rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

    rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?
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
  screen[:num_rows, :num_cols] = 1  # turns pixels on


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
  screen = np.zeros((6,50), dtype=np.int)  #initialize blank screen. 6 rows, 50 cols.
  for line in fp:
    instruction = line.rstrip("\n").split(" ")  # split line into list of words
    if instruction[0] == 'rect':
      coordinates = instruction[1].split('x')  # ie '12x3' => ['12','3']
      rect(screen, num_cols=int(coordinates[0]), num_rows=int(coordinates[1]))
      print(screen)
    elif instruction[0] == "rotate":
      index = int(instruction[2].split('=')[1])  #  'x=32'=> ['x','32']=> 32
      rotate(screen, axis=instruction[1], index=index, shift=int(instruction[4]))
      print(screen)
  print("Pixels on: {}".format(screen.sum()))
