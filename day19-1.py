'''--- Day 19: An Elephant Named Joseph ---

The Elves contact you over a highly secure emergency channel. Back at the North Pole, the Elves are busy misunderstanding White Elephant parties.

Each Elf brings a present. They all sit in a circle, numbered starting with position 1. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. An Elf with no presents is removed from the circle and does not take turns.

For example, with five Elves (numbered 1 to 5):

  1
5   2
 4 3

    Elf 1 takes Elf 2's present.
    Elf 2 has no presents and is skipped.
    Elf 3 takes Elf 4's present.
    Elf 4 has no presents and is also skipped.
    Elf 5 takes Elf 1's two presents.
    Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
    Elf 3 takes Elf 5's three presents.

So, with five Elves, the Elf that sits starting in position 3 gets all the presents.

With the number of Elves given in your puzzle input, which Elf gets all the presents?

Your puzzle input is 3014603.'''

INPUT = 3014603
from itertools import cycle
import numpy as np
from time import time

class Elf(object):
  def __init__(self, name):
    self._name = name
    self._num_gifts = 1
    self._right = None
    self._left = None

  def __repr__(self):
    return "{}: has {} gifts".format(self._name, self._num_gifts)

  @property
  def left(self):
    return self._left

  @left.setter
  def left(self, elf):
    self._left = elf

  @property
  def right(self):
    return self._right

  @right.setter
  def right(self, elf):
    self._right = elf

  @property
  def gifts(self):
    return self._num_gifts

  @gifts.setter
  def gifts(self, value):
    self._num_gifts = value


def elf_printer(elf):
  head = elf
  while elf.left!= head:
    print(elf)
    elf = elf.left
  print(elf)


if __name__ == "__main__":
  start_t = time()
  first_elf = Elf(1)
  current_elf = first_elf

  # setup the circle of elves
  for x in range(2, INPUT+1):
    current_elf.left = Elf(x)
    current_elf.left.right = current_elf
    current_elf = current_elf.left

  # last points to first elf, first elf "left" points to last elf
  current_elf.left = first_elf
  first_elf.right = current_elf

  current_elf = first_elf

  #print out the original cycle of elves
  #elf_printer(current_elf)

  while current_elf.left != current_elf:
    current_elf.gifts = current_elf.gifts + current_elf.left.gifts
    remove_elf = current_elf.left
    current_elf.left = remove_elf.left
    current_elf.left.right = current_elf
    #print(current_elf)
    del remove_elf
    current_elf = current_elf.left


  end_t = time()
  print("This took {} secs".format(round(end_t-start_t,3)))
  print(current_elf)

  


