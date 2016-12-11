'''
--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

    You start at "5" and don't move at all (up and left are both edges), ending at 5.
    Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
    Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
    Finally, after five more moves, you end at 3.

So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?

'''

if __name__ == '__main__':
  with open("day02input.txt") as fp:
    directions = fp.readlines()

    moves = {
              1:{'L':1, 'R':1, 'U':1, 'D':3},
              2:{'L':2, 'R':3, 'U':2, 'D':6},
              3:{'L':2, 'R':4, 'U':1, 'D':7},
              4:{'L':3, 'R':4, 'U':4, 'D':8},
              5:{'L':5, 'R':6, 'U':5, 'D':5},
              6:{'L':5, 'R':7, 'U':2, 'D':'A'},
              7:{'L':6, 'R':8, 'U':3, 'D':'B'},
              8:{'L':7, 'R':9, 'U':4, 'D':'C'},
              9:{'L':8, 'R':9, 'U':9, 'D':9},
              'A':{'L':'A', 'R':'B', 'U':6, 'D':'A'},
              'B':{'L':'A', 'R':'C', 'U':7, 'D':'D'},
              'C':{'L':'B', 'R':'C', 'U':8, 'D':'C'},
              'D':{'L':'D', 'R':'D', 'U':'B', 'D':'D'},
            }

    code = [5 for x in range(len(directions))]

    for index, digit in enumerate(code):
      for instruction in directions[index]:
        if instruction != '\n':
          digit = moves[digit][instruction]
      code[index] = digit

    print(code)






