import random
def random_grid():
	mylist=[]
	for i in range(0,10):
		mylist.append(i)
	rand_grid=[ [0]*9 for _ in range(9) ]
	i=0
	while(i<=8):
		rand_val=random.choice(mylist)
		rand_grid[i][i]=rand_val
		mylist.remove(rand_val)
		i+=1
	return rand_grid

def new_sudoku(solved_grid):
	difficulty_level=40
	final_grid=[ [0]*9 for _ in range(9) ]
	index_point=[]
	i=0
	while(i<=8):
		j=0
		while(j<=8):
			index_point.append([i,j])
			j+=1
		i+=1
	k=1
	while(k<=difficulty_level):
		rand_index=random.choice(index_point)
		final_grid[rand_index[0]][rand_index[1]]=solved_grid[rand_index[0]][rand_index[1]]
		index_point.remove(rand_index)
		k+=1
	return final_grid