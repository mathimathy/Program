def clear():
	print("\n"*50)
def printScreen(board,turn):
	clear()
	print(f'{turn}\'s turn')
	for row in board:
		printableColumn=''
		for column in row:
			printableColumn+=column+"|"
		printableColumn=printableColumn[:-1]
		print(printableColumn)
def checkWin(board):
	if board[0][0]==board[0][1]==board[0][2]:
		return board[0][0]
	elif board[1][0]==board[1][1]==board[1][2]:
		return board[1][0]
	elif board[2][0]==board[2][1]==board[2][2]:
		return board[2][0]
	elif board[0][0]==board[1][0]==board[2][0]:
		return board[0][0]
	elif board[0][1]==board[1][1]==board[2][1]:
		return board[0][1]
	elif board[0][2]==board[1][2]==board[2][2]:
		return board[0][2]
	elif board[0][0]==board[1][1]==board[2][2]:
		return board[0][0]
	elif board[2][0]==board[1][1]==board[0][2]:
		return board[1][1]
	return None

def main():
	while True:
		playing=True
		board=[[" "," "," "],[" "," "," "],[" "," "," "]]
		turn="X"
		while playing:
			printScreen(board,turn)
			while True:
				try:
					row=int(input("Veuillez insérer le numéro de ligne: "))-1
					column=int(input("Veuillez insérer le numéro de colonne: "))-1
					if row<=2 and column<=2 and row>=0 and column>=0:
						if board[row][column]==" ":
							break
						else:
							print("Il y a déjà un sigle !")
					else:
						print("Vous devez entrer un nombre entre 0 et 2 !")
				except:
					print("Vous devez entrer un nombre !")
			board[row][column]=turn

			winner=checkWin(board)
			if winner=="X":
				printScreen(board, turn)
				print("X wins !")
				playing=False
			elif winner=="O":
				printScreen(board,turn)
				print("O wins !")
				playing=False
			if turn=="X":
				turn="O"
			else:
				turn="X"
		if input("Voulez-vous rejouer (oui ou non) ? ")=="non":
			quit()

if __name__ == '__main__':
	main()