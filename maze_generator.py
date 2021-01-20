import numpy as np
from numpy.random import randint as rand
import matplotlib.pyplot as plt
import math


class Hexagon:
    """Implementation of hexagon"""

    def __init__(self, x_cord, y_cord, col, row, size):
        self.center_x = x_cord
        self.center_y = y_cord

        self.visited = False

        self.size = size

        self.hex_points_x = []
        self.hex_points_y = []

        self.grid_col = col
        self.grid_row = row

        self.allowed_moves = [0] * 6
        self.neighbours = [1] * 6

    def create_hex_vertexes(self):
        for i in range(1, 7):
            angle_deg = 60 * i - 30
            angle_rad = math.pi / 180 * angle_deg
            x = (self.center_x + self.size * np.cos(angle_rad))
            y = (self.center_y + self.size * np.sin(angle_rad))
            self.hex_points_x.append(x)
            self.hex_points_y.append(y)


# this function return truth table for allowed moves for hexagon
def allowed_moves(hexagon, size):
    moves = [False] * 6
    if hexagon.grid_row == 0 and hexagon.grid_col == 0: # bottom left
        moves = [1,1,0,0,0,0]
    elif hexagon.grid_row == 0 and hexagon.grid_col == size[1] - 1: # bottom right
        moves = [1,0,0,0,1,1]
    elif hexagon.grid_row == size[0]-1 and hexagon.grid_col == 0:
        moves = [0,1,1,1,0,0]
    elif hexagon.grid_row == size[0]-1 and hexagon.grid_col == size[1]-1:
        moves = [0,0,0,1,1,0]
    elif hexagon.grid_row == 0:
        moves = [1,1,0,0,1,1]
    elif hexagon.grid_row == size[0]-1:
        moves = [0,1,1,1,1,0]
    elif hexagon.grid_col == 0:
        if hexagon.grid_row % 2 == 1:
            moves = [1,1,1,1,0,1]
        else:
            moves = [1,1,1,0,0,0]
    elif hexagon.grid_col == size[1]-1:
        if hexagon.grid_row % 2 == 1:
            moves = [0,0,0,1,1,1]
        else:
            moves = [1,0,1,1,1,1]
    else:
        moves = [1,1,1,1,1,1]

    return moves


def create_hexagon_grid(size, hexagon_size):
    hexagons = []
    x_step = np.sqrt(3) * hexagon_size -0.1
    y_step = 3/2 * hexagon_size - 0.1
    for row in range(0, size[0]):
        rows = []
        for col in range(0, size[1]):
            if col % 2 == 0:
                x_cord = x_step * row
            else:
                x_cord = x_step * row + x_step/2
            y_cord = y_step * col
            hexa = Hexagon(x_cord, y_cord, row, col, hexagon_size)
            hexa.allowed_moves = allowed_moves(hexa, size)
            hexa.neighbours = hexa.allowed_moves[:]
            hexa.create_hex_vertexes()
            rows.append(hexa)
        hexagons.append(rows)
    return hexagons


def unvisited_neighbours(heksagons, neighbours):
    unvisited = []
    for i in range(0, len(neighbours)):
        if heksagons[neighbours[i][0]][neighbours[i][1]].visited == False:
            unvisited.append(neighbours[i])
    return unvisited


def maze(heksagons, size):
    initial_cel = heksagons[0][0]
    initial_cel.visited = True
    stack = [initial_cel]
    while stack:
        current_cell = stack.pop()
        neighbours, indexes = find_neighbours(current_cell)
        unvisited_n = unvisited_neighbours(heksagons, neighbours)
        if len(unvisited_n):
            stack.append(current_cell)
            ran = rand(0, len(unvisited_n))
            wall = indexes[ran]
            current_cell.allowed_moves[wall] = 0
            x, y = unvisited_n[ran]
            current_cell = heksagons[x][y]
            current_cell.allowed_moves[convert_index(wall)] = 0
            current_cell.visited = True
            stack.append(current_cell)




def convert_index(x):
    converted_value = 0
    if x == 0:
        converted_value = 3
    elif x ==1:
        converted_value = 4
    elif x == 2:
        converted_value = 5
    elif x == 3:
        converted_value = 0
    elif x == 4:
        converted_value = 1
    else:
        converted_value = 2
    return converted_value


def find_neighbours(hexagon):
    allowed_moves = []
    move_index = []
    if hexagon.grid_row % 2 == 0:
        for i in range(0, len(hexagon.allowed_moves)):
            if hexagon.allowed_moves[i] == 1:
                allowed_moves.append(move_to_index_parity(hexagon, i))
                move_index.append(i)
    else:
        for i in range(0, len(hexagon.allowed_moves)):
            if hexagon.allowed_moves[i] == 1:
                allowed_moves.append(move_to_index_not_parity(hexagon, i))
                move_index.append(i)
    return [allowed_moves, move_index]


def move_to_index_parity(hexagon, x):
    if x == 0:
        return[hexagon.grid_row + 1, hexagon.grid_col]
    elif x == 1:
        return[hexagon.grid_row, hexagon.grid_col + 1]
    elif x == 2:
        return[hexagon.grid_row - 1, hexagon.grid_col]
    elif x == 3:
        return[hexagon.grid_row - 1, hexagon.grid_col - 1]
    elif x == 4:
        return[hexagon.grid_row, hexagon.grid_col - 1]
    else:
        return[hexagon.grid_row + 1, hexagon.grid_col - 1]

def move_to_index_not_parity(hexagon, x):
    if x == 0:
        return[hexagon.grid_row + 1, hexagon.grid_col + 1]
    elif x == 1:
        return[hexagon.grid_row, hexagon.grid_col + 1]
    elif x == 2:
        return[hexagon.grid_row - 1, hexagon.grid_col + 1]
    elif x == 3:
        return[hexagon.grid_row - 1, hexagon.grid_col]
    elif x == 4:
        return[hexagon.grid_row, hexagon.grid_col - 1]
    else:
        return[hexagon.grid_row + 1, hexagon.grid_col]



hexagon_size = 5/4
size = (5, 5)
hexagons = create_hexagon_grid(size, hexagon_size)

x = []
y = []

hex_lines_x = []
hex_lines_y = []

maze(hexagons, size)

for hex_rows in hexagons:
    for i in range(0,len(hex_rows)):
        x.append(hex_rows[i].center_x)
        y.append(hex_rows[i].center_y)

        for j in range(0, 6):
            if hex_rows[i].allowed_moves[j] == hex_rows[i].neighbours[j]:
                hexagon = hex_rows[i]
                if j == 0:
                    plt.plot([hexagon.hex_points_x[0],hexagon.hex_points_x[5]],[hexagon.hex_points_y[0],hexagon.hex_points_y[5]], color = 'k')
                else:
                    plt.plot([hexagon.hex_points_x[j-1], hexagon.hex_points_x[j]], [hexagon.hex_points_y[j-1],hexagon.hex_points_y[j]],  color = 'k')

# Plot
#plt.scatter(x, y, alpha=0.5)

plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



