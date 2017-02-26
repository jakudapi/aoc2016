'''--- Day 14: One-Time Pad ---
--- Part Two ---

Of course, in order to make this process even more secure, you've also implemented key stretching.

Key stretching forces attackers to spend more time generating hashes. Unfortunately, it forces everyone else to spend more time, too.

To implement key stretching, whenever you generate a hash, before you use it, you first find the MD5 hash of that hash, then the MD5 hash of that hash, and so on, a total of 2016 additional hashings. Always use lowercase hexadecimal representations of hashes.

For example, to find the stretched hash for index 0 and salt abc:

    Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.
    Then, find the MD5 hash of that hash: eec80a0c92dc8a0777c619d9bb51e910.
    Then, find the MD5 hash of that hash: 16062ce768787384c81fe17a7a60c7e3.
    ...repeat many times...
    Then, find the MD5 hash of that hash: a107ff634856bb300138cac6568c0f24.

So, the stretched hash for index 0 in this situation is a107ff.... In the end, you find the original hash (one use of MD5), then find the hash-of-the-previous-hash 2016 times, for a total of 2017 uses of MD5.

The rest of the process remains the same, but now the keys are entirely different. Again for salt abc:

    The first triple (222, at index 5) has no matching 22222 in the next thousand hashes.
    The second triple (eee, at index 10) hash a matching eeeee at index 89, and so it is the first key.
    Eventually, index 22551 produces the 64th key (triple fff with matching fffff at index 22859.

Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key stretching, what index now produces your 64th one-time pad key?

Your puzzle input is still jlmsuwbz.'''

import hashlib
import re
from time import time
from multiprocessing import Pool, cpu_count


PUZZLE_INPUT = "jlmsuwbz"
SIZE_OF_LOOKUP = 25001  # minimum size is 1001


def is_key(digit, adder, lookup):
  '''
  inputs-
    digit: str. repeating digit in the test key
    adder: int. the current adder to puzzle input
    lookup: list[str] the pre-gen hashes
  outputs-
    returns True/False. if hash is a valid key
  '''

  regexstring = digit * 5
  find_five = re.compile(regexstring)
  index = adder + 1
  while (index <= adder + 1000):
    result = find_five.search(lookup[index % SIZE_OF_LOOKUP])
    if result:  # found 5 repeating digits
      return True
    index += 1
  return False


def pregen_hash(index, size=20000):
  '''
  uses multiprocessing.Pool for faster creation
  inputs- index:int to add to puzzle input, size:int size of list to create
  outputs- returns list of hashes
  '''
  p = Pool(int(cpu_count() / 2))
  adders = [PUZZLE_INPUT + str(x + index) for x in range(size)]
  big_hash = p.map(extended_key, adders)
  return big_hash


def extended_key(input):
  '''
  inputs- input:str
  outputs- returns str of extended key
  '''
  for x in range(2017):
    hash = hashlib.md5()
    hash.update(input.encode())
    input = hash.hexdigest()
  return hash.hexdigest()


if __name__ == "__main__":
  start_t = time()
  adder_at_last_pregen = 0
  adder = 0
  pad = []
  find_three = re.compile(r'(\w)\1\1')
  lookup = pregen_hash(0, SIZE_OF_LOOKUP)

  while(True):
    result = find_three.search(lookup[adder])
    if result:  # found 3 repeating digits
      # print("Found a possible key: {} at index {}".format(hash.hexdigest(), adder))
      # print("Checking........")
      if is_key(result.group()[0], adder, lookup):
        print("Key {} is valid. Index was {}".format(lookup[adder], adder))
        pad.append(adder)
        if len(pad) >= 64:
          break  # we're done!
    adder += 1

  end_t = time()
  print("this took {} secs.".format(round(end_t - start_t, 2)))
