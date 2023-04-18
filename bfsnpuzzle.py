import math
import collections

class Node:
	def __init__(self, puzzle, parent=None, action=None):
		self.puzzle = puzzle
		self.parent = parent
		self.action = action

	def state(self):
		#print(self.puzzle.board)
		return self.puzzle.board
	
	def path(self):
		node, p = self, []
        	while node:
            		p.append(node.state())
            		node = node.parent
		#print(p)
		return p
        	#print(reversed(p))
	
	def solved(self):
		return self.puzzle.solved()

	def actions(self):
		return self.puzzle.actions()
 
class Environment:
	def __init__(self, board):
		self.board = board
		self.width = int(math.sqrt(len(self.board)))

	def copy(self):
		board = []
		for element in self.board:
			board.append(element)
		return board

	def moved(self, (r,c),(i,j)):
		copy = self.copy()
		copy[r * self.width + c], copy[i * self.width + j] = copy[i * self.width + j], copy[r * self.width + c] 
		return copy

	def goal(self):
		goal = []
		for i in range (1, len(self.board)):
			goal.append(i)
		goal.append(-1)
		return str(goal)

	def solved(self):
		return str(self.board) == self.goal()

	def actions(self):
		block_pos = self.board.index(-1)
		block_r = block_pos / self.width
		block_c = block_pos % self.width
		moves = []

		directions = {"R":(block_r, block_c + 1),
			      "L":(block_r, block_c - 1),
			      "T":(block_r - 1, block_c),
			      "D":(block_r + 1, block_c)}
		for action, (i,j) in directions.items():
			if i >= 0 and j >= 0 and i < self.width and j < self.width:
				move = self.moved((block_r, block_c),(i,j)),action
				moves.append(move)
		return moves
				

	def showboard(self):
		newnode = Node(self.board)
		print(newnode.state()[0])
		return self.board

class Agent:
	def __init__(self, start):
		self.start = start

	def solver(self):
		board = self.start.board
		fringe = collections.deque([Node(self.start)])
		#print(Node(self.start).state())
		#print(fringe[0].puzzle)
		visited = set()
		visited.add(str(fringe[0].state()))
		#print(visited)
		'''k = 0'''
		while fringe:
			'''k = k + 1
			if k > 8:
				break'''
			node = fringe.pop()
			if node.solved():
				return node.path()
			for move, action in node.actions():
				child = Node(Environment(move), node, action)
				#print("Parent", node.state())
				#print(action, child.state()) 
				if str(child.state()) not in visited:
					#print("added to", child.state())
					fringe.appendleft(child)
					visited.add(str(child.state()))
		
		


##input to be take here....

#board = [-1,2,3,1,4,5,7,8,6]
i = int(input())
for k in range(0, i):
	n = int(input())
	board = []
	for i in range(0, n):
		temp = []
		temp = [int(x) for x in raw_input().split()]
		#print(temp)
		for t in temp:
			board.append(t)
	#print(str(board))
	p = Environment(board)
	s = Agent(p)
	solved_p = s.solver()
	#print(solved_p)



	for path in reversed(solved_p):
		soln = ''
		for elem in path:
			soln += str(elem)+' '
		print(soln)
#print(p.solved())
#print(p.actions())
