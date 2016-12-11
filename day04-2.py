"""
--- Day 4: Security Through Obscurity ---

--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?


"""


import csv
from collections import Counter
from itertools import combinations


def decrypter(room_name, checksum):
  shift = checksum % 26  
  decrypted = ['' for x in range(len(room_name))]  #list of empty chars
  for index, letter in enumerate(room_name):
    if letter == '-': 
      decrypted[index] = '-'
    else:
      charvalue = ord(letter) + shift  
      if charvalue > 122:  # if greater than 'z'
        charvalue = charvalue - 122 + 96  # cycle
      decrypted[index] = chr(charvalue)  # store char
  return ''.join(decrypted)


def compare(item):  #custom key function for the sorted() builtin func
  """ input is a tuple of (char, count), ie ('a', 99)
  return a custom weight, of 10000 x count + ordinal_of_char
  """
  char_value = ord(item[0])

  if char_value == 45:
    char_value = 99999999999  # no value to hyphens 
   
  return item[1]*10000 - char_value # item count gets more weight than character alphabetic order

def top_five(counter):
  temp = sorted(tuple(counter.items()), key=compare, reverse=True)
  return ''.join((a[0] for a in temp[0:5]))  # take the top five letters from the tuple of tuples and convert to a string

if __name__ == "__main__":
  with open("day04input.txt") as fp:
    room_ids = fp.read().splitlines()
    sum = 0
    for line in room_ids:
      letters = line[:-11]#.replace('-', '') # remove checksum&sector and strip hyphens
      count_letters = Counter(letters) #count letters
      test_checksum = top_five(count_letters)
      if test_checksum == line[-6:-1]:  # check against checksum at the end of the input line
        name = decrypter(letters, int(line[-10:-7]))
        if "north" in name:
          print("room: {}, sector: {}".format(name, line[-10:-7]))


