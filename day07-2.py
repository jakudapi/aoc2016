'''--- Day 7: Internet Protocol Version 7 ---
--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

    aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

'''

import re
from time import time


def ssl_checker(hypernets, chunk):
  '''
  input:hypernets : list of strs representing text inside brackets (inludes brackets too) chunk:str. the IP string either outside brackets

  output: boolean. if aba AND bab patterns around found
  '''
  chunk_length = len(chunk)
  if chunk_length <= 2:
    return False
  else:
    start_index = 0
    stop_index = 3
    while stop_index <= chunk_length:
      test_aba = chunk[start_index:stop_index]
      if test_aba[0] == test_aba[2] and test_aba[0] != test_aba[1] and bab_checker(hypernets, test_aba):
        return True
      else:
        start_index += 1
        stop_index += 1 
  return False


def bab_checker(hypernets, valid_aba):
  """
  input: hypernets : list of strs representing text inside brackets (inludes brackets too)
  valid_aba: str . valid aba sequence of letters as verified from aba_checker()
  output: boolean if bab pattern is found
  """
  valid_bab = valid_aba[1] + valid_aba[0] + valid_aba[1]  # if "aba" ==> valid_bab assigned "bab"
  for hypernet in hypernets:
    if valid_bab in hypernet:
      return True
  return False


if __name__ == "__main__":
  start = time()
  with open("day07input.txt") as fp:
    counter = 0

    key = re.compile(r'\[.+?\]')
    for number, line in enumerate(fp):
      print("Checking line {}: {}".format(number+1, line))
      hypernets = re.findall(key, line)
      line = line.rstrip("\n")
      message = re.split(key, line)  # split string and removes all text between & inc. brackets
      for IP in message:
        print("Checking this IP: {}".format(IP))
        if ssl_checker(hypernets, IP):
          counter += 1
          break
      print("SSL found so far: {}".format(counter))
      #break
  print("This took {} secs".format(round(time()-start,3)))
