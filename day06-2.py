'''
--- Day 6: Signals and Noise ---
--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?


'''

from collections import Counter

columns = {0:Counter(), 1:Counter(), 2:Counter(), 3:Counter(), 4:Counter(), 5:Counter(), 6:Counter(), 7:Counter()}

with open("day06input.txt") as fp:
  for line in fp:
    temp = line.rstrip("\n")
    for index, letter in enumerate(temp):
      columns[index][letter] += 1
  for column in columns:
    print(columns[column].most_common()[-1][0])
