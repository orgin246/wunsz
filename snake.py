from enum import Enum

class Direction(Emun):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT =3


class Snake:
 lenght = None
 direction = None
 body = None
 Block_size = None
 color = (0,0,255)
 bounds = None

  def __init__(self, Block_size, bounds):
    self.block_size = block_size
    self.bounds = bounds
    self.respawn

  def respawn(self):
    self.lenght = 3
    self.body = [(20,20), (20,40), (20,60)]
    self.direction = Direction.DOWN
