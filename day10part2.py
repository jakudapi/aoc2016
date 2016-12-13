'''--- Day 10: Balance Bots ---
What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?
'''


from collections import defaultdict
from collections import Counter


class Instruction():
  def __init__(self, low, high):
    self.low = low
    self.high = high
  def __str__(self):
    return str(self.low) + ", " + str(self.high)
  def __repr__(self):
    return str(self.low) + ", " + str(self.high)


class Bot(object):
  def __init__(self, chip1=None, chip2=None, instruction=None):
    self._chip_counter = Counter()  #empty Counter of chips. 
    if chip1: self._chip_counter[chip1] = 1
    if chip2: self._chip_counter[chip2] = 1
    self.instruction = instruction

  def num_chips(self):
    return len(self._chip_counter)  # a bin should hever have more than one value chip...

  def __str__(self):
    return "Bot has chips {} and instruction {}".format(self._chip_counter.keys(), self.instruction)
  
  def __repr__(self):
    return "Bot has chips {} and instruction {}".format(self._chip_counter.keys(), self.instruction)
  
  def pop_chip(self):
    return self._chip_counter.popitem()[0]  #just return "key" aka "chip value"
  
  def receive_chip(self, value):
    self._chip_counter[value] += 1  # key is "chip value"


def bot_to_process(bot_bank):
  """
  returns set of bots with 2 chips to process
  """
  set_of_bots = {0}-{0}
  for robot in bot_bank:
    if bot_bank[robot].num_chips() == 2:
      #print("Bot {} will do work".format(robot))
      set_of_bots.add(robot)
  return set_of_bots
    
def do_work(botname, bot_bank):
  chip1 = bot_bank[botname].pop_chip()  
  chip2 = bot_bank[botname].pop_chip()
 
  if chip1 < chip2:
    bot_bank[bot_bank[botname].instruction.low].receive_chip(chip1)
    bot_bank[bot_bank[botname].instruction.high].receive_chip(chip2)
  else:
    bot_bank[bot_bank[botname].instruction.low].receive_chip(chip2)
    bot_bank[bot_bank[botname].instruction.high].receive_chip(chip1)


if __name__ == "__main__":
  with open("day10input.txt") as fp:
    set_of_bots = {'na'}

    instructions = fp.readlines()
    bot_bank = defaultdict(Bot)
    for line in instructions:
      chunk = line.rstrip("\n").split(" ")
      if len(chunk) == 6:
        value = int(chunk[1])
        botname = "bot " + chunk[5]
        bot_bank[botname].receive_chip(value)
      elif len(chunk) == 12:
        botname = "bot " + chunk[1]
        low = chunk[5] + " " + chunk[6]  # first item is bot/bin , 2nd is name
        high = chunk[10] + " " + chunk[11]
        bot_bank[botname].instruction = Instruction(low, high)

    while len(set_of_bots) > 0:  # while there are still bots with 2 chips
      set_of_bots = bot_to_process(bot_bank)
      for robot in set_of_bots:
        do_work(robot, bot_bank)
      set_of_bots = bot_to_process(bot_bank)

    print(bot_bank['output 0'])
    print(bot_bank['output 1'])
    print(bot_bank['output 2'])

