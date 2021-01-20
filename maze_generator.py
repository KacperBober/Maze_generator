import numpy as np
from numpy.random import randint as rand
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import math


class Hexagon:
    """Implementation of hexagon"""

    def __init__(self, x_cord, y_cord, col, row, size):
        self.center_x = x_cord
        self.center_y = y_cord

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
    x_step = np.sqrt(3) * hexagon_size
    y_step = 3/2 * hexagon_size
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
            hexa.create_hex_vertexes()
            rows.append(hexa)
        hexagons.append(rows)
    return hexagons


def create_maze(hexagons, grid_size):
    visited = []
    stack = []

    stack.append(hexagons[0]) # initial point is 0, 0

    while stack:
        current_cell = stack.pop()






hexagon_size = 5/4
size = (10, 10)
hexagons = create_hexagon_grid(size, hexagon_size)

# Create data
x = [hexagon.center_x for hexagon in hexagons]
y = [hexagon.center_y for hexagon in hexagons]

hex_lines_x = [hexagon.hex_points_x for hexagon in hexagons]
hex_lines_y = [hexagon.hex_points_y for hexagon in hexagons]

colors = (0, 0, 0)

# Plot
#plt.scatter(x, y, c=colors, alpha=0.5)

for i in range(0, len(hexagons)):
    x = hex_lines_x[i]
    y = hex_lines_y[i]

    x.append(hex_lines_x[i][0])
    y.append(hex_lines_y[i][0])
    plt.plot(x, y)

plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



