case_val=0
arr_r_c=[]
new_val=0

def ifcorrect(grid,row,column,n):
    count=0
    i=0
    while(i<len(grid)):
        if(grid[row][i]==n):
            count+=1
        if(grid[i][column]==n):
            count+=1
        i+=1
    grid_row=3*int(row/3)
    grid_col=3*int(column/3)
    i=0
    while(i<=2):
        j=0
        while(j<=2):
            if(grid[grid_row+i][grid_col+j]==n):
                count+=1
            j+=1
        i+=1
    if(count==0):
        return True
    else:
        return False

def finding_zeros(grid):
    i=0
    count=0
    while(i<len(grid)):
        j=0
        while(j<len(grid)):
            if(grid[i][j]==0):
                return i,j
                count+=1
                break
            j+=1
        i+=1
    if(count==0):
        return True

def another_function(grid):
    global case_val
    global arr_r_c
    global new_val
    i=arr_r_c[-1]
    i_r=i[0]
    i_c=i[1]
    new_val=grid[i_r][i_c]
    grid[i_r][i_c]=0
    del arr_r_c[-1]
    case_val=1
    #print(arr_r_c)

def loopnumber(grid):
    global case_val
    global arr_r_c
    global new_val
    #print(arr_r_c)
    if(case_val==0):
        i=1
        count=0
        while(i<=len(grid)):
            r_zero,c_zero=finding_zeros(grid)
            if(ifcorrect(grid,r_zero,c_zero,i)):
                grid[r_zero][c_zero]=i
                arr_r_c.append([r_zero,c_zero])
                count+=1
                break
            i+=1
        if(count==0):
            another_function(grid)
    if(case_val==1):
        i=new_val+1
        count=0 
        while(i<=len(grid)):
            r_zero,c_zero=finding_zeros(grid)
            if(ifcorrect(grid,r_zero,c_zero,i)):
                grid[r_zero][c_zero]=i
                arr_r_c.append([r_zero,c_zero])
                count+=1
                case_val=0
                break
            i+=1
        if(count==0):
            another_function(grid)
    


def main(grid):
    
    while(True):
        loopnumber(grid)
        if(finding_zeros(grid)==True):
            break
    return grid
        
'''if __name__=='__main__':

    grid=[
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]
    for i in main(grid):
        print(i)'''
