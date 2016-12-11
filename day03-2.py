"""
--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?


"""

def checker(sides):
  if sides[0] + sides[1] > sides[2]:
    if sides[1] + sides[2] > sides[0]:
      if sides[0] + sides[2] > sides[1]:
        return 1
  return 0


from itertools import combinations
import csv

if __name__ == "__main__":
  with open("day03input.txt") as fp:
    count = 0
    a=[0,0,0]
    b=[0,0,0]
    c=[0,0,0]
    for index, line in enumerate(csv.reader(fp, delimiter=" ", skipinitialspace=True)):
      if len(line) > 0 and index % 3 == 0:
        sides = tuple(int(side) for side in line)
        a[0] = sides[0]
        b[0] = sides[1]
        c[0] = sides[2]
      elif len(line) > 0 and index % 3 == 1:
        sides = tuple(int(side) for side in line)
        a[1] = sides[0]
        b[1] = sides[1]
        c[1] = sides[2]
      elif len(line) > 0 and index % 3 == 2:
        sides = tuple(int(side) for side in line)
        a[2] = sides[0]
        b[2] = sides[1]
        c[2] = sides[2]
        count += checker(a)
        count += checker(b)
        count += checker(c)


        
  print(count)

