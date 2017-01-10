'''--- Day 20: Firewall Rules ---

You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.

For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:

5-8
0-2
4-7

The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?
'''


def comparer(x):  #compare based upon the int value of the first IPnum aka before the hyphen
  return int(x.split('-')[0])


def line_to_tuple(ip_range):
  temp = ip_range.split('-')
  return (int(temp[0]), int(temp[1].rstrip("\n")))

with open("day20input.txt") as fp:
  blacklist = sorted(list(fp.readlines()), key=comparer)
  valid_ip = 0
  
  for start, finish in map(line_to_tuple, blacklist):
    if valid_ip < finish and valid_ip >= start:
      valid_ip = finish + 1

  print(valid_ip)

  

