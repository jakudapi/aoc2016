"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""

from itertools import combinations
import csv

if __name__ == "__main__":
  with open("day03input.txt") as fp:
    count = 0
    for line in csv.reader(fp, delimiter=" ", skipinitialspace=True):
      if len(line) > 0:
        sides = tuple(int(side) for side in line)
        if sides[0] + sides[1] > sides[2]:
          if sides[1] + sides[2] > sides[0]:
            if sides[0] + sides[2] > sides[1]:
              count += 1
  print(count)

