'''
--- Day 15: Timing is Everything ---
--- Part Two ---

After getting the first capsule (it contained a star! what great fortune!), the machine detects your success and begins to rearrange itself.

When it's done, the discs are back in their original configuration as if it were time=0 again, but a new disc with 11 positions and starting at position 0 has appeared exactly one second below the previously-bottom disc.

With this new disc, and counting again starting from time=0 with the configuration in your puzzle input, what is the first time you can press the button to get another capsule?


Disc #1 has 17 positions; at time=0, it is at position 1.
Disc #2 has 7 positions; at time=0, it is at position 0.
Disc #3 has 19 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 0.
Disc #5 has 3 positions; at time=0, it is at position 0.
Disc #6 has 13 positions; at time=0, it is at position 5.
'''

# key = disc number, value = tuple(num_positions, starting_position)
INPUT = {1: (17, 1), 2: (7, 0), 3: (19, 2), 4: (5, 0), 5: (3, 0), 6: (13, 5), 7: (11, 0)}
TEST = {1: (5, 4), 2: (2, 1)}

if __name__ == "__main__":
  button_push = [0 for x in range(3000000)]

  for x in range(1, len(INPUT) + 1):
    time_to_reach_disc = x
    for time in range(len(button_push)):
      disc_position_when_capsule_arrives = (x + time + INPUT[x][1]) % INPUT[x][0]
      if disc_position_when_capsule_arrives == 0:
        button_push[time] += 1  # capsule would fall through

  # 1st valid time would be the first index in button_push that has value = number of discs
  print("Push button at time= {}".format(button_push.index(len(INPUT))))
