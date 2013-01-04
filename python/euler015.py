"""
Starting in the top left corner of a 2x2 grid, there are 
six routes (without backtracking) to the bottom right corner.
How many routes are there through a 20x20 grid?
"""

down = 2         #grid height
right = 2        #grid width
finish_moves = 4 #check against this
"""
This will take exactly 4 moves
"""

down_moved = 0
right_moved = 0



#move1 options = right, down
	#move 2 options = right, down
		#if right_moved = right_max
			#options = down_moved
		#elif down_moved = down

		#elif
		