import math
from collections import defaultdict, OrderedDict
import numpy as np


class solver():
    def __init__(self, grid) -> None:
        self.grid = grid
        self.rows = {i_row:self.grid[i_row] for i_row in range(9)}
        self.cols = {i_col:self.grid[:,i_col] for i_col in range(9)}

        self.blocks = OrderedDict()
        for i_row in range(9):
            for i_col in range(9):
                start_index_row = ((i_row//3)*3)    
                start_index_col = ((i_col//3)*3)
                self.blocks[(start_index_row,start_index_col)] = self.grid[start_index_row:start_index_row+3,
                                                                           start_index_col:start_index_col+3]

    def find_superpositions(self, tuple_indices):
        i_row = tuple_indices[0]
        i_col = tuple_indices[1]
        
        superpositions = set(range(1,10))

        row_set = set(self.grid[i_row])
        superpositions = superpositions.difference(row_set)
        row_col = set(self.grid[:,i_col])
        superpositions = superpositions.difference(row_col)

        start_index_row = ((i_row//3)*3)
        start_index_col = ((i_col//3)*3)

        block_set = np.unique(self.grid[start_index_row:start_index_row+3,start_index_col:start_index_col+3])
        superpositions = superpositions.difference(block_set)

        return superpositions

    def collapse_wave_function(self,grid_dict):
        for indices in grid_dict: 
            if type(grid_dict[indices])==set and len(grid_dict[indices])==1:
                grid_dict[indices] = list(grid_dict[indices])[0]
        return grid_dict
