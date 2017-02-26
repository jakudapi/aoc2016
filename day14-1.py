'''--- Day 14: One-Time Pad ---

In order to communicate securely with Santa while you're on this mission, you've been using a one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys in your one-time pad, and so you need to generate some more.

To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:

    It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
    One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:

    The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
    The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
    None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
    Eventually, index 22728 meets all of the criteria to generate the 64th key.

So, using our example salt of abc, index 22728 produces the 64th key.

Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?

Your puzzle input is jlmsuwbz.'''

import hashlib
import re
from time import time


PUZZLE_INPUT = "jlmsuwbz"


def is_key(digit, adder):
  '''
  inputs-
    digit: str. repeating digit in the test key
    adder: int. the current adder to puzzle input
  outputs-
    returns True/False. if hash is a valid key
  '''

  regexstring = digit * 5
  find_five = re.compile(regexstring)
  index = adder + 1
  while (index <= adder + 1000):
    hash5 = hashlib.md5()
    hash5.update((PUZZLE_INPUT + str(index)).encode())
    # print("{}: {}".format(index, hash5.hexdigest()))
    result = find_five.search(hash5.hexdigest())
    if result:  # found 5 repeating digits
      return True
    index += 1
  return False


if __name__ == "__main__":
  start_t = time()
  adder = 0
  pad = []
  find_three = re.compile(r'(\w)\1\1')

  while(True):
    hash = hashlib.md5()
    hash.update((PUZZLE_INPUT + str(adder)).encode())
    #print("{}: {}".format(adder, hash.hexdigest()))
    result = find_three.search(hash.hexdigest())
    if result:  # found 3 repeating digits
      # print("Found a possible key: {} at index {}".format(hash.hexdigest(), adder))
      # print("Checking........")
      if is_key(result.group()[0], adder):
        print("Key {} is valid. Index was {}".format(hash.hexdigest(), adder))
        pad.append(adder)
        if len(pad) >= 64:
          break
      else:
        print("..... was not valid   =(")
    adder += 1

  end_t = time()
  print("this took {} secs.".format(round(end_t - start_t, 2)))
