'''
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar

The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?
'''

from collections import Counter

columns = {0:Counter(), 1:Counter(), 2:Counter(), 3:Counter(), 4:Counter(), 5:Counter(), 6:Counter(), 7:Counter()}

with open("day06input.txt") as fp:
  for line in fp:
    temp = line.rstrip("\n")
    for index, letter in enumerate(temp):
      columns[index][letter] += 1
  for column in columns:
    print(columns[column].most_common(1)[0][0])
