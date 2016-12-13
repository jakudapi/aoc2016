"""
--- Day 12: Leonardo's Monorail ---
As you head down the fire escape to the monorail, you notice it didn't start; register c needs to be initialized to the position of the ignition key.

If you instead initialize register c to be 1, what value is now left in register a?
"""

with open("day12input.txt") as fp:
  instructions = fp.readlines()
  registers = {'a':0, 'b':0, 'c':1, 'd':0}
  index = 0
  while index < len(instructions):
    #print("index = {}, instr. = {}".format(index, instructions[index].strip('\n')))
    chunks = instructions[index].rstrip('\n').split(' ')
    command = chunks[0]
    if chunks[1].isdigit(): x = int(chunks[1])
    else: x = registers[chunks[1]]
    if chunks[0] == 'cpy':
      registers[chunks[2]] = x
      index += 1
    elif command == 'inc':
      registers[chunks[1]] += 1
      index += 1
    elif command == 'dec':
      registers[chunks[1]] -= 1
      index += 1
    elif command == 'jnz' and x != 0:
      index += int(chunks[2])
    else:
      index += 1
    #print(registers)

  print(registers)




