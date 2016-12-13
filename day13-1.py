'''
--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

    Find x*x + 3*x + 2*x*y + y + y*y.
    Add the office designer's favorite number (your puzzle input).
    Find the binary representation of that sum; count the number of bits that are 1.
        If the number of bits that are 1 is even, it's an open space.
        If the number of bits that are 1 is odd, it's a wall.

For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., the corner of the building containing 0,0 would look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###

Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###

Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1352.'''


import numpy as np 
from functools import total_ordering
import heapq


DESIGNER = 1352

@total_ordering
class Node(object):
  def __init__(self, coordinate, terrain, visited=False, distance=99999):
    self._visited = visited
    self._distance = distance
    self._terrain = terrain
    self._coordinate = coordinate

  def __repr__(self):
    return str(self._coordinate) + " dist: " + str(self._distance) + " " + str(self._visited)

  def __lt__(self, other):
    return self._distance < other.distance

  def __eq__(self, other):
    return self._distance == other.distance

  @property
  def coordinate(self):
    return self._coordinate

  @property
  def visited(self):
    return self._visited

  @visited.setter
  def visited(self, value):
    self.visited = value

  @property
  def terrain(self):
    return self._terrain

  @property
  def distance(self):
    return self._distance

  @distance.setter
  def distance(self, value):
    self._distance = value

def space_decoder(x, y):
  '''
  input-  x,y: int. coordinates
  Output- returns "#" for wall, or "." for open
  '''
  value = (x*x + 3*x + 2*x*y + y + y*y) + DESIGNER
  count_of_ones = bin(value).count('1')
  if count_of_ones % 2 == 0:
    return "."
  else:
    return "#"


def maze_maker(max_x, max_y, start):
  '''
  inputs: max_x, max_y: int. max coordinates for the rectangle
  start: (col, row) tuple of start coordinate
  outputs: tuple (np.array with walls and open spaces, heapq[Node] all nodes, dict[Node]
  '''
  heap = []
  dict_of_nodes = {}

  maze = np.array(np.zeros(max_x*max_y, dtype=str)).reshape((max_y, max_x))
  for rownum, row in enumerate(maze):
    for colnum, col in enumerate(row):
      terrain = space_decoder(colnum, rownum)
      maze[rownum, colnum] = terrain
      if (colnum, rownum) == start:
        heapq.heappush(heap, Node((colnum,rownum), terrain, distance=0))
        dict_of_nodes[(colnum, rownum)] = Node((colnum,rownum), terrain, distance=0)

      else:
        heapq.heappush(heap, Node((colnum,rownum), terrain))
        dict_of_nodes[(colnum, rownum)] = Node((colnum,rownum), terrain)
        
  return (maze, heap, dict_of_nodes)


def neighbors(col, row):
  '''
  input- col, row: int
  output: yields (col, row) of a possible neighbor
  '''

  for a in ((col+1, row), (col-1, row), (col, row-1), (col, row+1)):
    yield a
       

def dijkstra(dict_of_nodes, heap, start, end):
  '''
  inputs-
  dict_of_nodes[Node]
  heap[Node]
  start: (int, int) , start coordinates (col, row).
  end: (int, int), end coordinates (col, row)
  output-
  return shortest path from start to end
  '''
  counter =0
  while len(heap) > 0:
    current_node = heapq.heappop(heap)
    if current_node.terrain == "#": continue #skip processing a wall-space  
    print("Minimal mode on heap: {}".format(current_node))
    for neighbor in neighbors(*current_node.coordinate):
      if neighbor in dict_of_nodes and dict_of_nodes[neighbor].terrain == '.':
        print("...evaluating node {}".format(neighbor))
        if current_node.distance + 1 < dict_of_nodes[neighbor].distance:
          print("node {}'s distance is now {}".format(neighbor, current_node.distance+1))
          dict_of_nodes[neighbor].distance = current_node.distance + 1
          for index, node in enumerate(heap):
            if node.coordinate == neighbor:
              heap[index].distance = current_node.distance + 1
              heap.sort()
              break
    if current_node.coordinate == end: break
    

if __name__ == "__main__":

  a = (100,100)
  target = (31,39)
  start = (1,1)
  maze, heap, dict_of_nodes = (maze_maker(*a, start=start))
  dijkstra(dict_of_nodes, heap, start, target)
  print(dict_of_nodes[(31,39)])
  
    
  

  


