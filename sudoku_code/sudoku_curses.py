import curses
import sudoku_solver_algorithm
import copy
import random_sudoku

def main(stdscr):
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	current_index=[0,0]
	
	new_arr=[]
	
	rand_grid_to_solve=random_sudoku.random_grid()
	#initial_grid=[[0]*9]*9
	#initial_grid=sudoku_v1.main(grid)
	solved_grid=copy.deepcopy(rand_grid_to_solve)
	sudoku_solver_algorithm.main(solved_grid)
	grid=random_sudoku.new_sudoku(solved_grid)

	navigation(stdscr,current_index,grid)

	#print(initial_grid)
	#print(new_arr)
	#print(sudoku_solver_algorithm.grid)
	#print(sudoku_solver_algorithm.main(grid))
	#print(solved_grid)
	while(True):
		key=stdscr.getch()
		if(key==curses.KEY_UP and current_index[0]>0):
			current_index[0]-=1
		elif(key==curses.KEY_DOWN and current_index[0]<8):
			current_index[0]+=1
		elif(key==curses.KEY_LEFT and current_index[1]>0):
			current_index[1]-=1
		elif(key==curses.KEY_RIGHT and current_index[1]<8):
			current_index[1]+=1
		'''elif(key==10):
			print(grid==solved_grid)
			if(grid==new_arr):
				stdscr.addstr(20,20,"YOu won")
			elif(grid!=new_arr):
				stdscr.addstr(20,20,"You loose")'''
		if(grid[current_index[0]][current_index[1]]==0):
			if(key>=48 and key<=57):
				stdscr.addstr(2*current_index[0],4*current_index[1], chr(key))
				grid[current_index[0]][current_index[1]]=int(chr(key))
				new_arr.append([current_index[0],current_index[1]])
		if(current_index in new_arr):
			if(key==263):
				stdscr.addstr(2*current_index[0],4*current_index[1], str(0))
				grid[current_index[0]][current_index[1]]=0
				new_arr.remove([current_index[0],current_index[1]])
				#print(new_arr)
		if((key==curses.KEY_ENTER or key in [10,13])):
			#print(solved_grid)
			if(grid==solved_grid):
				stdscr.addstr(20,20,"True ")
			else:
				stdscr.addstr(20,20,"False")
		stdscr.refresh()
		navigation(stdscr,current_index,grid)
	

def navigation(stdscr,selected_index,grid):
	i=0
	while(i<=8):
		j=0
		while(j<=8):
			k=grid[i][j]
			if(selected_index==[i,j]):
				stdscr.attron(curses.color_pair(1))
				stdscr.addstr(2*i,4*j,str(k))
				stdscr.attroff(curses.color_pair(1))
			else:
				stdscr.addstr(2*i,4*j,str(k))
			j+=1
			#stdscr.refresh()
		i+=1
	vert=0
	while(vert<=16):
		stdscr.addstr(vert,10,"|")
		stdscr.addstr(vert,22,"|")

		vert+=1
	horiz=0
	while(horiz<=32):
		stdscr.addstr(5,horiz,"--")
		stdscr.addstr(11,horiz,"--")
		horiz+=1
	stdscr.addstr(23,0,"Press \"Enter\" After Filling to check if its correct")
	stdscr.addstr(22,0,"Press \"BackSpace\" to remove an entry")
	stdscr.refresh()





curses.wrapper(main)