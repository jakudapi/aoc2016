"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

"""

def compare(item):
  return item[1]*10000 - ord(item[0]) # item count gets more weight than character alphabetic order

def top_five(counter):
  temp = sorted(tuple(counter.items()), key=compare, reverse=True)
  return ''.join((a[0] for a in temp[0:5]))  # take the top five letters from the tuple of tuples and convert to a string

import csv
from collections import Counter
from itertools import combinations

if __name__ == "__main__":
  with open("day04input.txt") as fp:
    room_ids = fp.read().splitlines()
    sum = 0
    for line in room_ids:
      letters = line[:-11].replace('-', '') # remove checksum&sector and strip hyphens
      count_letters = Counter(letters) #count letters
      test_checksum = top_five(count_letters)
      if test_checksum == line[-6:-1]:  # check against checksum at the end of the input line
        sum += int(line[-10:-7])

    print(sum)
