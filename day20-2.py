'''--- Day 20: Firewall Rules ---
--- Part Two ---

How many IPs are allowed by the blacklist?

'''


IP_MAX = 4294967295


def comparer(x):  #compare based upon the int value of the first IPnum aka before the hyphen
  return int(x.split('-')[0])


def line_to_tuple(ip_range):
  temp = ip_range.split('-')
  return (int(temp[0]), int(temp[1].rstrip("\n")))

with open("day20input.txt") as fp:
  blacklist = sorted(list(fp.readlines()), key=comparer)
  valid_ip = 0
  list_of_ips = []
  
  for start, finish in map(line_to_tuple, blacklist):
    if valid_ip < finish and valid_ip >= start:
      valid_ip = finish + 1
    elif valid_ip < start:
      list_of_ips.extend(range(valid_ip, start))  #add valid ips from [current, start). 
      valid_ip = finish + 1

  print(len(list_of_ips))

  

