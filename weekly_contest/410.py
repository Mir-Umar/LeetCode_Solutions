'''
There is a snake in an n x n matrix grid and can move in four possible directions. Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.

The snake starts at cell 0 and follows a sequence of commands.

You are given an integer n representing the size of the grid and an array of strings commands where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT". It's guaranteed that the snake will remain within the grid boundaries throughout its movement.

Return the position of the final cell where the snake ends up after executing commands.
'''
import numpy as np
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        #n = len(commands)
        sq = np.arange(n*n)
        mt = sq.reshape(n,n)
        row = 0
        col = 0
        for i in range(len(commands)):
            if commands[i]=='UP':
                row = row-1
                col=col
            elif commands[i]=="RIGHT":
                row=row
                col=col+1
            elif commands[i]=="DOWN":
                row = row+1
                col=col
            elif commands[i]=="LEFT":
                row=row
                col=col-1
        return mt[row][col]
