def printBoardPosition():
	# shows index positions and the corresponding numbers
	print('0|1|2')
	print('-+-+-')
	print('3|4|5')
	print('-+-+-')
	print('6|7|8')

def printBoard(board):
	# prints the current board situation
	print(board[0]+'|'+board[1]+'|'+board[2])
	print('-+-+-')
	print(board[3]+'|'+board[4]+'|'+board[5])
	print('-+-+-')
	print(board[6]+'|'+board[7]+'|'+board[8])

def takeUserInput(board):
	move = int(input('enter position:'))
	while (move < 0) or (move > 8) or (str(board[int(move)]) != ' '):
 		print('enter valid input')
 		move = int(input('enter position:'))
	return move

def getEmptyPlaces(board):
	# gets empty places on the board
	emptyPlaces = []
	for key, value in board.items():
		if value == ' ':
			emptyPlaces.append(key)
	return emptyPlaces

def winning(board, player):
	# check for all winning combinations
	if (board[0] == board[1] == board[2] == player or
		board[3] == board[4] == board[5] == player or
		board[6] == board[7] == board[8] == player or
		board[0] == board[3] == board[6] == player or
		board[1] == board[4] == board[7] == player or
		board[2] == board[5] == board[8] == player or
		board[0] == board[4] == board[8] == player or
		board[2] == board[4] == board[6] == player):
		return True
	else:
		return False

def getBoardCopy(board):
	# get duplicate board for testing purposes
	dupeBoard = board.copy()
	return dupeBoard

def minimax(board, player):
	availableSpots = getEmptyPlaces(board)
	
	# assigning socres to various scenarios
	if (winning(board, '0')):
		return {'score': 10}
	elif (len(availableSpots) == 0):
		return {'score': 0}
	elif (winning(board, 'x')):
		return {'score': -10}

	moves = []

	for spot in availableSpots:
		move = {'index': spot}
		board[spot] = player
		if(player == '0'):
			result = minimax(board, 'x')
			move['score'] = result['score']
		else:
			result = minimax(board, '0')
			move['score'] = result['score']
		board[spot] = ' '
		moves.append(move)

	if(player == '0'):
		bestScore = -10000
		for move in moves:
			if move['score'] > bestScore:
				bestScore = move['score']
				bestMove = move
	else:
		bestScore = 10000
		for move in moves:
			if move['score'] < bestScore:
				bestScore = move['score']
				bestMove = move
	return bestMove

def generateReply(board, machine):
	dupBoard = getBoardCopy(board)
	bestMove = minimax(dupBoard, machine)
	return bestMove['index']

def play(board):
	result = str(input('want first move?(y/n)'))
	if(result == 'y'):
		user = 'x'
		machine = '0'
	else:
		machine = 'x'
		user = '0'
		board[generateReply(board, machine)] = machine
		printBoard(board)

	gameIsPlaying = True

	while gameIsPlaying:
		emptySpots = getEmptyPlaces(board)
		if len(emptySpots) == 0:
			print('draw')
			gameIsPlaying = False
			break


		p = takeUserInput(board)
		board[int(p)] = user
		emptySpots = getEmptyPlaces(board)
		if winning(board, user):
			printBoard(board)
			print('congrats')
			gameIsPlaying = False
		elif len(emptySpots) == 0:
			printBoard(board)
			print('draw')
			gameIsPlaying = False
			break
		else:
			board[generateReply(board, machine)] = machine
			printBoard(board)

		if winning(board, machine):
			print('you lost')
			gameIsPlaying = False

board = {
	0: ' ', 1: ' ', 2: ' ',
	3: ' ', 4: ' ', 5: ' ',
	6: ' ', 7: ' ', 8: ' ',
}

printBoardPosition()

play(board)