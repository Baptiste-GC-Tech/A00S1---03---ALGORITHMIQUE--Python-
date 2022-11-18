#DEBUT

#Admettre la fonction randint() qui renvoi un entier aléatoire entre 2 valeurs incluses
from random import randint
#Admettre la fonction os() qui permet d'éxecuter des commandes dans la console
import os
#Préparation pour vider le contenu de la console
clear = lambda: os.system('cls')

#Définir une conftion morpionTurnManager(board, symbol, coordinates) qui permet d'éditer un tableau de morpion avec un nouveau symbole
def morpionTurnManager(board, symbol, coordinates):
	#Initialiser un tableau 2D updatedBoard égal à board
	updatedBoard = [[] * 3] * 3
	#Assigner à updatedBoard[coordinates[0], coordinates[1]] le caractère symbol
	updatedBoard[coordinates[0], coordinates[1]] = symbol
	#Retourner updatedBoard
	return updatedBoard

#Définir une fonction morpionEndChecker(board) qui permet de définir si une partie de morpion est terminé, et quel en est le résultat
def morpionEndChecker(board):
	#Initialiser une variable xCoord à 0
	xCoord = 0
	#Initialiser une variable yCoord à 0
	yCoord = 0
	#Initialiser une variable gameStatus à None
	gameStatus = None
	#Initialiser une liste winnerSymbol à [None, None]
	winnerSymbol = [None, None]
	#Pour xCoord dans 2, Faire...
	for xCoord in range(2):
		#Si board[xCoord][0] est égal à board[xCoord][1] ET board[xCoord][1] est égal à board[xCoord][2], Alors...
		if board[xCoord][0] == board[xCoord][1] and board[xCoord][1] == board[xCoord][2]:
			#Assigner à gameStatus le string "winned"
			gameStatus = "winned"
			#Assigner à winnerSymbol la liste [xCoord, 1]
			winnerSymbol = [xCoord, 1]
			#Sortir de la boucle
			break
	#Pour yCoord dans 2, Faire...
	for yCoord in range(2):
		#Si board[0][yCoord] est égal à board[1][yCoord] ET board[1][yCoord] est égal à board[2][yCoord], Alors...
		if board[xCoord][0] == board[xCoord][1]  and board[xCoord][1] == board[xCoord][2]:
			#Assigner à gameStatus le string "winned"
			gameStatus = "winned"
			#Assigner à winnerSymbol la liste [1, yCoord]
			winnerSymbol = [1, yCoord]
			#Sortir de la boucle
			break
	#Si board[0][0] est égal à board[1][1] ET board[1][1] est égal à board[2][2], Alors...
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		#Assigner à gameStatus le string "winned"
		gameStatus = "winned"
		#Assigner à winnerSymbol la liste [1, 1]
		winnerSymbol = [1,1]
	#Si board[2][0] est égal à board[1][1] ET board[1][1] est égal à board[0][2], Alors...
	if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
		#Assigner à gameStatus le string "winned"
		gameStatus = "winned"
		#Assigner à winnerSymbol la liste [1, 1]
		winnerSymbol = [1, 1]

	#Si gameStatus est égal à None, Alors...
	if gameStatus == None:
		#Assigner à gameStatus le string "blocked"
		gameStatus = "blocked"
		#Pour x dans 0 à 2, Faire...
		for x in range(0, 2):
			#Pour y dans 0 à 2, Faire...
			for y in range(0, 2):
				#Si board[x][y] est égal à ' ', Alors...
				if board[x][y] == ' ':
					#Assigner à gameStatus la valeur None
					gameStatus = None
					#Sortir de la boucle
					break
	#Si gameStatus est égal à "winned", Alors...
	if gameStatus == "winned":
		#Afficher "!!! VICTOIRE !!!"
		print("!!! VICTOIRE !!!")
		#Si board[winnerSymbol[0]][winnerSymbol[1]] est égal à 'O', Alors...
		if board[winnerSymbol[0]][winnerSymbol[1]] == 'O':
			#Afficher "le Participant 1 à gagné"
			print("Le participant 1 a gagné")
		#Si board[winnerSymbol[0]][winnerSymbol[1]] est égal à 'X', Alors...
		if board[winnerSymbol[0]][winnerSymbol[1]] == 'X':
			#Afficher "le Participant 2 à gagné"
			print("Le participant 1 a gagné")
		#Retourner True
		return True
	#Sinon Si gameStatus est égal à "blocked", Alors...
	elif gameStatus == "blocked":
		#Afficher "!!! ÉGALITÉ !!!"
		print("!!! ÉGALITÉ !!!")
		#Retourner True
		return True
	#Sinon : la partie n'est ni bloquée ni gagnée, Alors...
	else:
		#Retourner False
		return False

#Définir une fonction morpionPrintBoard(board) qui permet d'afficher correctement une partie de morpion
def morpionPrintBoard(board):
	#Afficher "╔═╦═╦═╗"
	print("╔═╦═╦═╗")
	#Afficher "║" + str(board[0][0]) + "║" + str(board[0][1]) + "║" + str(board[0][2]) + "║"
	print("║" + str(board[0][0]) + "║" + str(board[0][1]) + "║" + str(board[0][2]) + "║")
	#Afficher "╠═╬═╬═╣"
	print("╠═╬═╬═╣")
	#Afficher "║" + str(board[1][0]) + "║" + str(board[1][1]) + "║" + str(board[1][2]) + "║"
	print("║" + str(board[1][0]) + "║" + str(board[1][1]) + "║" + str(board[1][2]) + "║")
	#Afficher "╠═╬═╬═╣"
	print("╠═╬═╬═╣")
	#Afficher "║" + str(board[2][0]) + "║" + str(board[2][1]) + "║" + str(board[2][2]) + "║"
	print("║" + str(board[2][0]) + "║" + str(board[2][1]) + "║" + str(board[2][2]) + "║")
	#Afficher "╚═╩═╩═╝"
	print("╚═╩═╩═╝")

#Définir une fonction morpionBlinkBoard(board) qui permet d'afficher correctement une partie de morpion avec des traits plus fin
def morpionBlinkBoard(board):
	#Initialiser un tableau 2D lighterBoard égal à board
	lighterBoard = board
	#Pour x dans 0 à 2, Faire...
	for x in range(0, 2):
		#Pour y dans 0 à 2, Faire...
		for y in range(0, 2):
			#Si lighterBoard[x][y] est égal à 'O', Alors...
			if lighterBoard[x][y] == 'O':
				#Assigner à lighterBoard[x][y] le caractère '○'
				lighterBoard[x][y] == '○'
			#Sinon Si lighterBoard[x][y] est égal à 'X', Alors...
			if lighterBoard[x][y] == 'X':
				#Assigner à ligtherBoard[x][y] le caractère '×'
				lighterBoard[x][y] == '×'
	#Afficher "┌─┬─┬─┐"
	print("┌─┬─┬─┐")
	#Afficher "│" + str(board[0][0]) + "│" + str(board[0][1]) + "│" + str(board[0][2]) + "│"
	print("│" + str(board[0][0]) + "│" + str(board[0][1]) + "│" + str(board[0][2]) + "│")
	#Afficher "├─┼─┼─┤"
	print("├─┼─┼─┤")
	#Afficher "│" + str(board[1][0]) + "│" + str(board[1][1]) + "│" + str(board[1][2]) + "│"
	print("│" + str(board[1][0]) + "│" + str(board[1][1]) + "│" + str(board[1][2]) + "│")
	#Afficher "├─┼─┼─┤"
	print("├─┼─┼─┤")
	#Afficher "│" + str(board[2][0]) + "│" + str(board[2][1]) + "│" + str(board[2][2]) + "│"
	print("│" + str(board[2][0]) + "│" + str(board[2][1]) + "│" + str(board[2][2]) + "│")
	#Afficher "└─┴─┴─┘"
	print("└─┴─┴─┘")





#Définir une fonction morpionVsCpu() qui permet de jouer à une partie de morpion avec l'ordinateur
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	#Initialiser une variable gameOver à False
	#Initialiser une liste playerChoice à [None, None]
	#Initialiser une liste cpuChoice à [None, None]
	#Initialiser une variable isValidChoice à False
	#Tant que gameOver est à False, Alors...
		#Si turnOf est égal à 1, Alors...
			#Vider l'écran de la console
			#Afficher "C'est au tour du Joueur !"
			#Appeler la fonction morpionPrintBoard(board)
			#Tant que isValidChoice est à False, Alors...
				#Assigner à playerChoice[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				#Assigner à playerChoice[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				#Si playerChoice[0] ou playerChoice[1] ne sont pas compris entre 0 et 2, Alors...
					#Afficher un message d'erreur : la position n'est pas valide
				#Sinon Si board[playerChoice[0]][playerChoice[1]] est différent de ' ', Alors...
					#Afficher un message d'erreur : la case est occupée
				#Sinon : board[playerChoice[0]][playerChoice[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', playerChoice)
			#Assigner à turnOf la valeur 2
		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour de l'Ordinateur !"
			#Tant que isValidChoice est à False, Alors...
				#Assigner à cpuChoice[0] le retour de l'appel de la fonction randint(0, 2)
				#Assigner à cpuChoice[1] le retour de l'appel de la fonction randint(0, 2)
				#Si board[cpuChoice[0]][cpuChoice[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', cpuChoice)
			#Assigner à turnOf la valeur 1
		#Assigner à isValidChoice la valeur False
		#Assigner à gameOver le retour de l'appel de la fonction morpionEndChecker(board)
	#Afficher un message de retour au menu



#Définir une fonction morpionVsIA qui permet de jouer à une partie de morpion contre une IA imbattable
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	#Initialiser une variable gameOver à False
	#Initialiser une liste playerChoice à [None, None]
	#Initialiser une liste IAChoice à [None, None]
	#Initialiser une variable IAChoosed à False
	#Initialiser une variable isValidChoice à False
	#Initialiser une variable Xcounter à 0
	#Initialiser une liste XXportunity à [None]
	#Initialiser une variable Ocounter à 0
	#Initialiser une liste OOportunity à [None]
	#Initialiser une varibale spaceCounter à 0
	#Initialiser une variable boardStatus à "common"
	#Tant que gameOver est à False, Alors...
		#Si turnOf est égal à 1, Alors...
			#Vider l'écran de la console
			#Afficher "C'est au tour du Joueur !"
			#Appeler la fonction morpionPrintBoard(board)
			#Tant que isValidChoice est à False, Alors...
				#Assigner à playerChoice[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				#Assigner à playerChoice[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				#Si playerChoice[0] ou playerChoice[1] ne sont pas compris entre 0 et 2, Alors...
					#Afficher un message d'erreur : la position n'est pas valide
				#Sinon Si board[playerChoice[0]][playerChoice[1]] est différent de ' ', Alors...
					#Afficher un message d'erreur : la case est occupée
				#Sinon : board[playerChoice[0]][playerChoice[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', playerChoice)
			#Assigner à turnOf la valeur 2
		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour de l'IA !"

				#  RESET DES NOUVELLES "portunity"

				#Assigner à OOportunity la liste [None]
				#Assigner à XXportunity la liste [None]


				#  REMPLISSAGE DES "portunity"

				#Pour x dans 0 à 2, Faire...
					#Assigner à Ocounter la valeur 0
					#Assigner à Xcounter la valeur 0
					#Pour y dans 0 à 2, Faire...
						#Si board[x][y] est égal à 'O', Alors...
							#Incrémenter Ocounter de 1
						#Sinon Si board[x][y] est égal à 'X', Alors...
							#Incrémenter Xcounter de 1
					#Si Ocounter est égal à 2 et Xcounter est égal à 0, Alors...
						#Ajouter dans OOportunity le string "r" + str(x+1)
					#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
						#Ajouter dans XXportunity le string "r" + str(x+1)

				#Pour y dans 0 à 2, Faire...
					#Assigner à Ocounter la valeur 0
					#Assigner à Xcounter la valeur 0
					#Pour x dans 0 à 2, Faire...
						#Si board[x][y] est égal à 'O', Alors...
							#Incrémenter Ocounter de 1
						#Sinon Si board[x][y] est égal à 'X', Alors...
							#Incrémenter Xcounter de 1
					#Si Ocounter est égal à 2 et Xcounter est égal à 0, Alors...
						#Ajouter dans OOportunity le string "c" + str(y+1)
					#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
						#Ajouter dans XXportunity le string "c" + str(y+1)

				#Assigner à Ocounter la valeur 0
				#Assigner à Xcounter la valeur 0
				#Pour x dans 0 à 2, Faire...
					#Si board[x][x] est égal à 'O', Alors...
						#Incrémenter Ocounter de 1
					#Sinon Si board[x][x] est égal à 'X', Alors...
						#Incrémenter Xcounter de 1
				#Sinon Si Ocounter est égal à 2 et Xcounter est égal à 0, Alors...
					#Ajouter à OOportunity le string "d1"
				#Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
					#Ajouter à XXportunity le string "d1"

				#Assigner à Ocounter la valeur 0
				#Assigner à Xcounter la valeur 0
				#Si board[0][2] est égal à 'O', Alors...
					#Incrémenter Ocounter de 1
				#Sinon Si board[0][2] est égal à 'X', Alors...
					#Incrémenter Xcounter de 1
				#Si board[1][1] est égal à 'O', Alors...
					#Incrémenter Ocounter de 1
				#Sinon Si board[1][1] est égal à 'X', Alors...
					#Incrémenter Xcounter de 1
				#Si board[2][0] est égal à 'O', Alors...
					#Incrémenter Ocounter de 1
				#Sinon Si board[2][0] est égal à 'X', Alors...
					#Incrémenter Xcounter de 1
				#Si Ocounter est égal à 2 et Xocunter est égal à 0, Alors...
					#Ajouter à OOportunity le string "d2"
				#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
					#Ajouter à XXportunity le string "d2"

				#  SAISIE D'UNE OPPORTUNITÉ DE VICTOIRE S'IL Y A


				#Si XXportunity est différente de [None], Alors...
					#Si XXportunity[0][0] est égal à 'r', Alors...
						#Pour y dans 0 à 2, Faire...
							#Si board[int(XXportunity[0][1])][y] est égal à ' ', Alors...
								#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [int(XXportunity[0][1]), y])
								#Sortir de la boucle

					#Si XXportunity[0][0] est égal à 'c', Alors...
						#Pour x dans 0 à 2, Faire...
							#Si board[x][int(XXportunity[0][1])] est égal à ' ', Alors...
								#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [x, int(XXportunity[0][1])])
								#Sortir de la boucle

					#Si XXportunity[0] est égal à "d1", Alors...
						#Pour xy dans 0 à 2, Faire...
							#Si board[xy][xy] est égal à ' ', Alors...
								#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [xy, xy])
								#Sortir de la boucle

					#Si XXportunity[0] est égal à "d2", Alors...
						#Si board[0][2] est égal à ' ', Alors...
							#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [0, 2])
							#Sortir de la boucle
						#Sinon Si board[1][1] est égal à ' ', Alors...
							#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [1, 1])
							#Sortir de la boucle
						#Sinon Si board[2][0] est égal à ' ', Alors...
							#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [2, 0])
							#Sortir de la boucle

				#  CONTRE D'UNE OPPORTUNITÉ DE DÉFAITE S'IL Y A


				#Sinon Si OOportunity est différente de [None], Alors...
					#Si OOportunity[0][0] est égal à 'r', Alors...
						#Pour y dans 0 à 2, Faire...
							#Si board[int(OOportunity[0][1])][y] est égal à ' ', Alors...
								#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [int(OOportunity[0][1]), y])
								#Sortir de la boucle

					#Si OOportunity[0][0] est égal à 'c', Alors...
						#Pour x dans 0 à 2, Faire...
							#Si board[x][int(OOportunity[0][1])] est égal à ' ', Alors...
								#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [x, int(OOportunity[0][1])])
								#Sortir de la boucle

					#Si OOportunity[0] est égal à "d1", Alors...
						#Pour xy dans 0 à 2, Faire...
							#Si board[xy][xy] est égal à ' ', Alors...
								#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [xy, xy])
								#Sortir de la boucle

					#Si OOportunity[0] est égal à "d2", Alors...
						#Si board[0][2] est égal à ' ', Alors...
							#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [0, 2])
							#Sortir de la boucle
						#Sinon Si board[1][1] est égal à ' ', Alors...
							#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [1, 1])
							#Sortir de la boucle
						#Sinon Si board[2][0] est égal à ' ', Alors...
							#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', [2, 0])
							#Sortir de la boucle

				#  ALGORITHME DE STRATÉGIE PARFAITE SI AUCUN DES DEUX


				#Sinon, Alors...
					#Assigner à spaceCounter la valeur 0
					#Pour x dans 0 à 2, Faire...
						#Pour y dans 0 à 2, Faire...
							#Si board[x][y] est égal à ' ', Alors...
								#Incrémenter spaceCounter de 1

					#Si board[1][1] est égal à ' ', Alors...
						#Assigner à IAChoice[0] la valeur 1
						#Assigner à IAChoice[1] la valeur 1
						#Assigner à IAChoosed la valeur True

					#Sinon Si spaceCounter est égal à 8 et IAChoosed est égal à False, Alors...
						#Tant que isValidChoice est à False, Alors...
							#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ' et IAChoice est différente de toutes les listes suivantes : [0, 1] [1, 0] [1, 2] [2, 1], Alors...
								#Assigner à isValidChoice la valeur True
								#Assigner à IAChoosed la valeur True

					#Sinon Si spaceCounter est égal à 7 et IAChoosed est égal à False, Alors...
						#Si board[0][1] ou board[2][1] est égal à 'O', Alors...
							#Tant que isValidChoice est à False, Alors...
								#Assigner à IAChoice[0] la valeur playerChoice[0]
								#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
								#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
									#Assigner à isValidChoice la valeur True
									#Assigner à IAChoosed la valeur True

						#Si board[1][0] ou board[1][2] est égal à 'O', Alors...
							#Tant que isValidChoice est à False, Alors...
								#Assigner à IAChoice[0] la retour de l'appel de la fonction randint(0, 2)
								#Assigner à IAChoice[1] la valeur playerChoice[1]
								#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
									#Assigner à isValidChoice la valeur True
									#Assigner à IAChoosed la valeur True

						#Sinon : le Joueur à joué dans les diagonales, Alors...
							#Tant que isValidChoice est à False, Alors...
								#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
								#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
								#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
									#Assigner à isValidChoice la valeur True
									#Assigner à IAChoosed la valeur True

					#Sinon Si spaceCounter est égal à 6 et IAChoosed est égal à False, Alors...
						#Si board[1][1] est égal à 'X', Alors...
							#Si board[0][1] et board[1][0] sont égal à 'O', Alors...
								#Assigner à IAChoice[0] la valeur 0
								#Assigner à IAChoice[1] la valeur 0
								#Assigner à IAChoosed la valeur True
							#Sinon Si board[0][1] et board[1][2] sont égal à 'O', Alors...
								#Assigner à IAChoice[0] la valeur 0
								#Assigner à IAChoice[1] la valeur 2
								#Assigner à IAChoosed la valeur True
							#Sinon Si board[2][1] et board[1][0] sont égal à 'O', Alors...
								#Assigner à IAChoice[0] la valeur 2
								#Assigner à IAChoice[1] la valeur 0
								#Assigner à IAChoosed la valeur True
							#Sinon Si board[2][1] et board[1][2] sont égal à 'O', Alors...
								#Assigner à IAChoice[0] la valeur 2
								#Assigner à IAChoice[1] la valeur 2
								#Assigner à IAChoosed la valeur True

						#Sinon, Alors...
							#Tant que isValidChoice est à False, Alors...
								#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
								#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
								#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
									#Assigner à isValidChoice la valeur True
									#Assigner à IAChoosed la valeur True

					#Sinon Si spaceCounter est égal à 5 et IAChoosed est égal False, Alors...
						#Si board[0][0], board[0][1] et board[1][0] sont égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur 0
							#Assigner à IAChoice[1] la valeur 0
						#Sinon Si board[0][2], board[0][1] et board[1][2] sont égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur 0
							#Assigner à IAChoice[1] la valeur 2
						#Sinon Si board[2][0], board[2][1] et board[1][0] sont égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur 2
							#Assigner à IAChoice[1] la valeur 0
						#Sinon Si board[2][2], board[2][1] et board[1][2] sont égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur 2
							#Assigner à IAChoice[1] la valeur 2

						#Sinon : le Joueur ne s'est pas mis en danger, Alors...
							#Tant que isValidChoice est à False, Alors...
								#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
								#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
								#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ' et IAChoice est différent de toutes les listes suivante : [0, 0] [0, 2] [2, 0] [2, 2], Alors...
									#Assigner à isValidChoice la valeur True

					#Sinon : Aucune occasion de victoire ou défaite assurée n'est présente, Alors...
						#Tant que isValidChoice est à False, Alors...
							#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ' et IAChoice est différent de toutes les listes suivante : [0, 0] [0, 2] [2, 0] [2, 2], Alors...
								#Assigner à isValidChoice la valeur True
								
			#  ON APPLIQUE LA DÉCISION DE L'IA


			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', IAChoice)
			#Assigner à turnOf la valeur 1
		#Assigner à isValidChoice la valeur False
		#Assigner à IAChoosed la valeur False
		#Assigner à gameOver le retour de l'appel de la fonction morpionEndChecker(board)
	#Afficher un message de retour au menu



#Définir une fonction morpionVsPlayer qui permet de jouer à une partie de morpion contre un autre joueur
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	#Initialiser une variable gameOver à False
	#Initialiser une liste player1Choice à [None, None]
	#Initialiser une liste player2Choice à [None, None]
	#Initialiser une variable isValidChoice à False
	#Tant que gameOver est à False, Alors...
		#Si turnOf est égal à 1, Alors...
			#Vider l'écran de la console
			#Afficher "C'est au tour du Joueur 1 !"
			#Appeler la fonction morpionPrintBoard(board)
			#Tant que isValidChoice est à False, Alors...
				#Assigner à playerChoice1[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				#Assigner à playerChoice1[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				#Si playerChoice1[0] ou playerChoice1[1] ne sont pas compris entre 0 et 2, Alors...
					#Afficher un message d'erreur : la position n'est pas valide
				#Sinon Si board[playerChoice1[0]][playerChoice1[1]] est différent de ' ', Alors...
					#Afficher un message d'erreur : la case est occupée
				#Sinon : board[playerChoice1[0]][playerChoice1[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', playerChoice1)
			#Assigner à turnOf la valeur 2
		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour de l'Ordinateur !"
			#Tant que isValidChoice est à False, Alors...
				#Assigner à playerChoice2[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				#Assigner à playerChoice2[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				#Si playerChoice2[0] ou playerChoice2[1] ne sont pas compris entre 0 et 2, Alors...
					#Afficher un message d'erreur : la position n'est pas valide
				#Sinon Si board[playerChoice2[0]][playerChoice2[1]] est différent de ' ', Alors...
					#Afficher un message d'erreur : la case est occupée
				#Sinon : board[playerChoice2[0]][playerChoice2[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', playerChoice2)
			#Assigner à turnOf la valeur 1
		#Assigner à isValidChoice la valeur False
		#Assigner à gameOver le retour de l'appel de la fonction morpionEndChecker(board)
	#Afficher un message de retour au menu


#Définir une fonction morpion() qui permet de lancer une partie de morpion
def morpion():
	#Initialiser une variable gameClose à False
	gameClose = False
	#Initialiser une variable menuNav à None
	menuNav = None

	#Vider l'écran de la console
	clear()

	#Tant que gameClose est égal à False, Alors...
	while gameClose == False:
		#Afficher le header du menu
		print("----------=<(MORPION)>=----------")
		#Afficher la commande pour quitter le jeu
		print("0 - Quitter")
		#Afficher la commande pour lancer une partie contre l'ordinateur
		print("1 - Partie contre l'Ordinateur")
		#Afficher la commande pour lancer une partie contre l'IA
		print("2 - Partie contre l'IA")
		#Afficher la commence pour lancer une partie contre un autre joueur
		print("3 - Partie contre un Joueur")
		#Afficher le footer du menu
		print("----------====]<⌂>[====----------")

		#Assigner à menuNav le retour d'input("Votre choix : ")
		menuNav = int(input("Votre choix : "))
		#Si menuNav est égal à 0, Alors...
		if menuNav == 0:
			#Assigner à gameClose la valeur True
			gameClose = True
		#Sinon Si menuNav est égal à 1, Alors...
		elif menuNav == 1:
			#Appeler la fonction morpionVsCpu
			morpionVsCpu()
		#Sinon Si menuNav est égal à 2, Alors...
		elif menuNav == 2:
			#Appeler la fonction morpionVsIA
			morpionVsIA()
		#Sinon Si menuNav est égal à 3, Alors...
		elif menuNav == 3:
			#Appeler la fonction morpionVsPlayer
			morpionVsPlayer()
		#Sinon, Alors...
		else:
			#Afficher un message d'erreur
			print("\nOPTION INEXISTANTE\n")
	#Afficher un message de fermeture
	print("fermeture")
	print("fermeture.")
	print("fermeture..")
	print("fermeture...")

#FIN

# 	179│
# 	196─
# 	186║
# 	205═

# 	[218,194,191] ┌┬┐
# 	[195,197,180] ├┼┤
# 	[192,193,217] └┴┘

# 	[201,203,187] ╔╦╗
# 	[204,206,185] ╠╬╣
# 	[200,202,188] ╚╩╝

# ╔═╗   ╔═╦═╗
# ║ ║   ║O║O║
# ╚═╝   ╠═╬═╣
#       ║O║X║
#       ╚═╩═╝
# ┌─┐   ┌─┬─┐
# │ │   │X│X│
# └─┘   ├─┼─┤
#       │O│X│
#       └─┴─┘

# Check toutes les lignes de victoires
# Si XXportunity, alors finish
# Sinon Si OOportunity, alors block
# Sinon : 

# Si empty
# ╔═╦═╦═╗
# ║ ║ ║ ║
# ╠═╬═╬═╣
# ║ ║ ║ ║
# ╠═╬═╬═╣
# ║ ║ ║ ║
# ╚═╩═╩═╝
# 	Alors center
# 	╔═╦═╦═╗
# 	║ ║ ║ ║
# 	╠═╬═╬═╣
# 	║ ║X║ ║
# 	╠═╬═╬═╣
# 	║ ║ ║ ║
# 	╚═╩═╩═╝
# 	Si N-cross
# 	╔═╦═╦═╗
# 	║ ║•║ ║
# 	╠═╬═╬═╣
# 	║•║X║O║
# 	╠═╬═╬═╣
# 	║ ║•║ ║
# 	╚═╩═╩═╝
# 		Alors same line
# 		╔═╦═╦═╗
# 		║ ║ ║X║
# 		╠═╬═╬═╣
# 		║ ║X║O║
# 		╠═╬═╬═╣
# 		║ ║ ║×║
# 		╚═╩═╩═╝
# 		Si block
# 		╔═╦═╦═╗
# 		║ ║ ║X║
# 		╠═╬═╬═╣
# 		║ ║X║O║
# 		╠═╬═╬═╣
# 		║O║ ║ ║
# 		╚═╩═╩═╝
# 			Alors corner no-neighbours
# 			╔═╦═╦═╗
# 			║X║ ║X║
# 			╠═╬═╬═╣
# 			║ ║X║O║
# 			╠═╬═╬═╣
# 			║O║ ║ ║
# 			╚═╩═╩═╝ ==> WIN
# 		Sinon ==> WIN
# 	Sinon
# 	╔═╦═╦═╗
# 	║•║ ║O║
# 	╠═╬═╬═╣
# 	║ ║X║ ║
# 	╠═╬═╬═╣
# 	║•║ ║•║
# 	╚═╩═╩═╝
# 		Alors random
# Sinon Si
# ╔═╦═╦═╗
# ║ ║ ║ ║
# ╠═╬═╬═╣
# ║ ║O║ ║
# ╠═╬═╬═╣
# ║ ║ ║ ║
# ╚═╩═╩═╝
# 	Alors random-corner
# 	╔═╦═╦═╗
# 	║×║ ║X║
# 	╠═╬═╬═╣
# 	║ ║O║ ║
# 	╠═╬═╬═╣
# 	║×║ ║×║
# 	╚═╩═╩═╝
# Sinon
# ╔═╦═╦═╗
# ║ ║O║ ║
# ╠═╬═╬═╣
# ║•║ ║•║
# ╠═╬═╬═╣
# ║ ║•║ ║
# ╚═╩═╩═╝
# 	Alors
# 	╔═╦═╦═╗
# 	║ ║O║ ║
# 	╠═╬═╬═╣
# 	║ ║ ║ ║
# 	╠═╬═╬═╣
# 	║ ║ ║ ║
# 	╚═╩═╩═╝
# -----------------------
# Si centre dispo, alors grab
# Si centre à 'X' + 1 seul 'O' + en D-cross, alors Gagner
# Si centre occupé + 1 seul 'O' + aucun 'X', alors prendre un coin au pif
# Sinon au pif

# Après avoir jouer, lister les XXportunity