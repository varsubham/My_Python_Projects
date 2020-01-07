class sudoku:
    case_val=0
    arr_r_c=[]
    new_val=0
    def __init__(self, grid):
        self.grid = grid
    def if_correct(self, grid, row, column, n):
        count = 0
        i = 0
        while (i < len(grid)):
            if (grid[row][i] == n):
                count += 1
            if (grid[i][column] == n):
                count += 1
            i += 1
        grid_row = 3 * int(row / 3)
        grid_col = 3 * int(column / 3)
        i = 0
        while (i <= 2):
            j = 0
            while (j <= 2):
                if (grid[grid_row + i][grid_col + j] == n):
                    count += 1
                j += 1
            i += 1
        if (count == 0):
            return True
        else:
            return False

    def finding_zeros(self, grid):
        i = 0
        count = 0
        while (i < len(grid)):
            j = 0
            while (j < len(grid)):
                if (grid[i][j] == 0):
                    return i, j
                    count += 1
                    break
                j += 1
            i += 1
        if (count == 0):
            return True
    def another_function(self, grid):
        i = self.arr_r_c[-1]
        i_r = i[0]
        i_c = i[1]
        self.new_val = grid[i_r][i_c]
        grid[i_r][i_c] = 0
        del self.arr_r_c[-1]
        self.case_val = 1
    def loop_number(self, grid):
        if (self.case_val == 0):
            i = 1
            count = 0
            while (i <= len(grid)):
                r_zero, c_zero = self.finding_zeros(grid)
                if (self.if_correct(grid, r_zero, c_zero, i)):
                    grid[r_zero][c_zero] = i
                    self.arr_r_c.append([r_zero, c_zero])
                    count += 1
                    break
                i += 1
            if (count == 0):
                self.another_function(grid)
        if (self.case_val == 1):
            i = self.new_val + 1
            count = 0
            while (i <= len(grid)):
                r_zero, c_zero = self.finding_zeros(grid)
                if (self.if_correct(grid, r_zero, c_zero, i)):
                    grid[r_zero][c_zero] = i
                    self.arr_r_c.append([r_zero, c_zero])
                    count += 1
                    self.case_val = 0
                    break
                i += 1
            if (count == 0):
                self.another_function(grid)
    def main(self, grid):
        while (True):
            self.loop_number(grid)
            if (self.finding_zeros(grid) == True):
                break
        for i in grid:
            print(i)
