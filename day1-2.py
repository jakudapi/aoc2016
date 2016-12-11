"""
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""


def checker(me, locations, distance, direction):
  for x in range(1,distance+1):
        me[me['direction']] += 1
        Y = me['N'] - me['S']
        X = me['E'] - me['W']
        if (X,Y) in locations: 
          print("{} up and {} right blocks away".format(Y,X))
          return True
        else:
          locations.add((X,Y))
  return False



if __name__ == "__main__":
  with open("day01input.txt") as fp:

    directions = fp.read().strip().replace('\n','')

    directions = directions.split(", ")

    compass = {"N":{"L":"W", "R":"E"}, "S":{"L":"E", "R":"W"}, "E":{"L":"N", "R":"S"}, "W":{"L":"S", "R":"N"}}

    me = {"N":0, "S":0, "E":0, "W":0, "direction":'N'}

    locations = {(0,0)}  # starting spot

    for direction in directions:
      turn = direction[0]
      distance = int(direction[1:])
      me['direction'] = compass[me['direction']][turn]
      if checker(me, locations, distance, direction):
        break
      
 
     



