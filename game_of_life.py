# Conway's game of life

import random
import time
import copy
import sys

WIDTH = 45
HEIGHT = 15

nextCells = []
for x in range(WIDTH):
    column = []     # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')      # Add a living cell
        else:
            column.append(' ')      # Add a dead cell
    nextCells.append(column)
try:
    while True:
        print('\n\n\n\n\n\n\n')
        currentCells = copy.deepcopy(nextCells)
        # Print currentCells on the screen
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y], end='')
            print()
        # Calculate the next step's cells based on current step's cell
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get the neighbouring coordinates
                leftCoord = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT
                # Count the number of living neighbours
                numNeighbours = 0
                if currentCells[leftCoord][aboveCoord] == '#':
                    numNeighbours += 1
                if currentCells[x][aboveCoord] == '#':
                    numNeighbours += 1
                if currentCells[rightCoord][aboveCoord] == '#':
                    numNeighbours += 1
                if currentCells[leftCoord][belowCoord] == '#':
                    numNeighbours += 1
                if currentCells[x][belowCoord] == '#':
                    numNeighbours += 1
                if currentCells[rightCoord][belowCoord] == '#':
                    numNeighbours += 1

                if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                    # Living cells with 2 or 3 neighbours stay alive
                    nextCells[x][y] = '#'
                elif currentCells[x][y] == ' ' and numNeighbours == 3:
                    # Dead cells with 3 neighbours become alive
                    nextCells[x][y] = '#'
                else:
                    # Everything else dies or stays dead
                    nextCells[x][y] = ''
        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
