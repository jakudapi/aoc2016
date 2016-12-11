'''--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?
'''

import re
from time import time


def abba_checker(chunk):
  '''
  input: chunk:str. the IP string either inside or outside brackets. no brackets should be passed in
  output: boolean if an ABBA is detected
  '''

  chunk_length = len(chunk)
  if chunk_length <= 3:
    return False
  else:
    start_index = 0
    stop_index = 4
    while stop_index <= chunk_length:
      test_abba = chunk[start_index:stop_index]
      print(test_abba)
      if test_abba[0:2] == (test_abba[3]+test_abba[2]) and test_abba[0] != test_abba[1]:
        #  i.e. if "ab" == reversed("ba") and "a" != "b"
        return True
      else:
        start_index += 1
        stop_index += 1 
  return False


if __name__ == "__main__":
  start = time()
  with open("day07input.txt") as fp:
    counter = 0

    key = re.compile(r'\[.+?\]')
    for number, line in enumerate(fp):
      print("Checking line {}: {}".format(number+1, line))
      abba_in_hypernet = False
      hypernet = re.findall(key, line)
      for chunk in hypernet:
        print("Checking this chunk: {}".format(chunk[1:-1]))
        if abba_checker(chunk[1:-1]):
          abba_in_hypernet = True
          break
      if abba_in_hypernet: continue # stop evaluating line, the line doesn't support TLS
      line = line.rstrip("\n")
      message = re.split(key, line)  # split string and removes all text between & inc. brackets
      for IP in message:
        print("Checking this IP: {}".format(IP))
        if abba_checker(IP):
          counter += 1
          break
      print("TLS found so far: {}".format(counter))
  print("This took {} secs".format(round(time()-start,2)))
