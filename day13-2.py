'''
--- Day 13: A Maze of Twisty Little Cubicles ---
--- Part Two ---

How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?
'''


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
    

if __name__ == "__main__":

  a = (100,100)
  target = (31,39)
  start = (1,1)
  maze, heap, dict_of_nodes = (maze_maker(*a, start=start))
  dijkstra(dict_of_nodes, heap, start, target)
  counter = 0
  for key in dict_of_nodes:
    if dict_of_nodes[key].distance <= 50:
      counter += 1
  print(counter)
  
    
  

  


