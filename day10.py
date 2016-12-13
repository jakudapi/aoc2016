'''--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

    Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
    Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
    Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
    Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?
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
    #self.name = name

  def chips(self):
    return str(self._chip_counter)

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
  if chip1 == 61 and chip2 == 17: print(botname)
  elif chip2 == 61 and chip1 == 17: print(botname)
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

    #print(bot_bank)

    while len(set_of_bots) > 0:
      set_of_bots = bot_to_process(bot_bank)
      #print(set_of_bots)
      for robot in set_of_bots:
        do_work(robot, bot_bank)
      set_of_bots = bot_to_process(bot_bank)
      #print(bot_bank)


