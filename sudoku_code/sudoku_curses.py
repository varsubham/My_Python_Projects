import curses
#import time
import sudoku_v1

def main(stdscr):
	i=0
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	current_index=[0,0]
	
	new_arr=[]
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
	
	#initial_grid=[[0]*9]*9
	#initial_grid=sudoku_v1.main(grid)
	navigation(stdscr,current_index,grid)
	#print(initial_grid)
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
			if(grid==initial_grid):
				stdscr.addstr(20,20,"YOu won")
			else:
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
	stdscr.refresh()





curses.wrapper(main)