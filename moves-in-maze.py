import sys
import math
from collections import deque, namedtuple
from typing import List, Optional


def idebug(*args):
    # return
    print(*args, file=sys.stderr)


def debug(*args):
    # return
    print(*args, file=sys.stderr)

Pos = namedtuple('Pos', ['x', 'y'])

def bfs_distance(start: Pos, dest: Pos) -> Optional[str]:
    queue: deque = deque([(start, 0)])
    visited: set = {start}
    while queue:
        cell, distance = queue.popleft()
        if cell == dest:
            return str(distance) if distance < 10 else chr(distance + 55)
        for dx, dy in {(0, 1), (-1, 0), (0, -1), (1, 0)}:
            new_x, new_y = cell.x + dx, cell.y + dy
            if new_x == w:
                new_x = 0
            elif new_x == -1:
                new_x = w - 1
            elif new_y == h:
                new_y = 0
            elif new_y == -1:
                new_y = h - 1
            new_cell: Pos = Pos(new_x, new_y)
            if grid[new_y][new_x] == "#" or new_cell in visited:
                continue
            queue.append((new_cell, distance + 1))
            visited.add(new_cell)
    return None


w, h = [int(i) for i in input().split()]
idebug(w, h)

grid = []
for i in range(h):
    row = input()
    idebug(row)
    grid.append(list(map(str, list(row))))
    if 'S' in row:
        start: Pos = Pos(x=row.index('S'), y=i)

for i in range(h):
    distances: List[str] = grid[i]
    if start.y == i:
        distances[start.x] = '0'
    for x in range(w):
        if grid[i][x] != '#':
            distance: Optional[str] = bfs_distance(start=start, dest=Pos(x, i))
            if distance:
                distances[x] = distance
    answer: str = ''.join(distances)
    print(answer)
