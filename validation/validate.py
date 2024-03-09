from collections import OrderedDict, defaultdict
from collections import Counter                                                                                                                                                                                                                                                   
from copy import deepcopy

class validate():

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
                
        

    def validate_unique(self, _list: list, row: int = None, col: int = None, block: tuple[int,int] = (None, None)) -> tuple[bool,list]:
        # ignore 0 
        og_list = deepcopy(_list)
        _list = _list[_list!=0]

        check = len(_list)==len(set(list(_list)))
        error = [i for i,j in Counter(_list).items() if j>1]

        # Find the index of error value
        error_indices = []
        for value in error:
            if og_list.ndim!=1:
                for row_index,row in enumerate(og_list):                
                    for col_index,col in enumerate(row):
                        if og_list[row_index][col_index]==value:
                            error_indices.append([row_index,col_index])
            else:
                error_index = [[0,i] for i, x in enumerate(og_list) if x == value]
                error_indices.extend(error_index)

        return (check, error_indices)

    def validate_max(self, _list: list) -> tuple[bool,list]:
        # ignore 0 
        og_list = deepcopy(_list)
        _list = _list[_list!=0]
        if len(_list)==0:
            return (True,[])
        
        check = max(_list)<=9
        if not check:
            error = [i for i in _list if i>9]
            # Find the index of error value 
            error_indices = []
            for value in error:
                error_index = [[0,i] for i, x in enumerate(og_list) if x == value]
                error_indices.extend(error_index)
        else:
            error_indices = []

        return (max(_list)<=9, error_indices)
    
    def validate_rows(self) -> bool|int:
        row_error_dict = defaultdict(list)

        for index,row in self.rows.items():
            unique_check = self.validate_unique(row)
            max_check = self.validate_max(row)

            if unique_check[0] and max_check[0]:
                continue 
            else: 
                error_indices = unique_check[1]
                error_indices.extend(max_check[1])
                for val in error_indices:
                    val[0]+=index
                row_error_dict[index].extend(error_indices)
        self.row_error_dict = row_error_dict
        print(f'Row Error Dict : {self.row_error_dict}')     

    def validate_cols(self) -> bool:

        col_error_dict = defaultdict(list)
        for index,col in self.cols.items():
            unique_check = self.validate_unique(col)
            max_check = self.validate_max(col)
            if unique_check[0] and max_check[0]:
                continue 
            else: 
                error_indices = unique_check[1]
                error_indices.extend(max_check[1])
                for val in error_indices:
                    val[0]+=index
                
                error_indices = [[j,i] for i,j in error_indices]
                col_error_dict[index].extend(error_indices)

        self.col_error_dict = col_error_dict

        print(f'Col Error Dict : {self.col_error_dict}')   
    
    def validate_blocks(self) -> bool:
        block_error_dict = defaultdict(list)

        for index, block in self.blocks.items():
            unique_check = self.validate_unique(block)

            if unique_check[0]:
                continue
            else: 
                error_indices = unique_check[1]
                for i in error_indices:
                    i[0]+=index[0]
                    i[1]+=index[1]
                block_error_dict[index].extend(error_indices)
        
        self.block_error_dict = block_error_dict
        print(f'Block Error Dict : {self.block_error_dict}')

    def get_errors(self):
        errors = list(self.row_error_dict.values())+list(self.col_error_dict.values())+list(self.block_error_dict.values())
        errors = sum(errors,[])
        errors = [tuple(i) for i in errors]
        
        errors = set(errors)
        
        return errors
    
    


    


  