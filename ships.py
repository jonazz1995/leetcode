"""
// "X" marks the presence of a ship
// A, B and C are points defined below
   +-+-+-+
 y2|B| |C|
   +-+-+-+
   | |X| |
   +-+-+-+
   | | |X|
   +-+-+-+
 y1|A| | |
   +-+-+-+
   x1   x2

   Point A(0,0);
   Point B(0,3);
   Point C(2,3);
   hasShips(A,C) == true;
   hasShips(B,C) == false;
   hasShips(C,C) == false;

   countShips(A,C) == 2;
   countShips(B,C) == 0;
   countShips(C,C) == 0;
O(n * m)
ocean = arr
ROWS = len(ocean) 4
COLS = len(ocean[0]) 3
"""
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    

def hashShips(top_left: Point, bottom_right: Point) -> bool:
    return True

def countShips(top_left: Point, bottom_right: Point) -> int:
    pass
    

