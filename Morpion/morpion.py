#DEBUT

#Admettre la fonction sleep() qui fait attendre le programme
from time import sleep
#Admettre la fonction randint() qui renvoi un entier aléatoire entre 2 valeurs incluses
from random import randint
#Admettre la fonction os() qui permet d'éxecuter des commandes dans la console
import os
#Préparation pour vider le contenu de la console
clear = lambda: os.system('cls')

#Définir une conftion morpionTurnManager(board, symbol, coordinates) qui permet d'éditer un tableau de morpion avec un nouveau symbole
def morpionTurnManager(board, symbol, coordinates):
	#Initialiser un tableau 2D updatedBoard égal à board
	updatedBoard = board
	#Assigner à updatedBoard[coordinates[0], coordinates[1]] le caractère symbol

	updatedBoard[coordinates[0]][coordinates[1]] = symbol
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
	#Pour xCoord dans 3, Faire...
	for xCoord in range(3):
		#Si board[xCoord][0] est égal à board[xCoord][1] ET board[xCoord][1] est égal à board[xCoord][2], Alors...
		if (board[xCoord][0] == board[xCoord][1] and board[xCoord][1] == board[xCoord][2]) and board[xCoord][0] != ' ':
			#Assigner à gameStatus le string "winned"
			gameStatus = "winned"
			#Assigner à winnerSymbol la liste [xCoord, 1]
			winnerSymbol = [xCoord, 1]
			#Sortir de la boucle
			break
	#Pour yCoord dans 3, Faire...
	for yCoord in range(3):
		#Si board[0][yCoord] est égal à board[1][yCoord] ET board[1][yCoord] est égal à board[2][yCoord], Alors...
		if (board[0][yCoord] == board[1][yCoord]  and board[1][yCoord] == board[2][yCoord]) and board[0][yCoord] != ' ':
			#Assigner à gameStatus le string "winned"
			gameStatus = "winned"
			#Assigner à winnerSymbol la liste [1, yCoord]
			winnerSymbol = [1, yCoord]
			#Sortir de la boucle
			break
	#Si board[0][0] est égal à board[1][1] ET board[1][1] est égal à board[2][2], Alors...
	if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != ' ':
		#Assigner à gameStatus le string "winned"
		gameStatus = "winned"
		#Assigner à winnerSymbol la liste [1, 1]
		winnerSymbol = [1,1]
	#Si board[2][0] est égal à board[1][1] ET board[1][1] est égal à board[0][2], Alors...
	if (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[2][0] != ' ':
		#Assigner à gameStatus le string "winned"
		gameStatus = "winned"
		#Assigner à winnerSymbol la liste [1, 1]
		winnerSymbol = [1, 1]

	#Si gameStatus est égal à None, Alors...
	if gameStatus == None:
		#Assigner à gameStatus le string "blocked"
		gameStatus = "blocked"
		#Pour x dans 0 à 2, Faire...
		for x in range(0, 3):
			#Pour y dans 0 à 2, Faire...
			for y in range(0, 3):
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
		#Sinon Si board[winnerSymbol[0]][winnerSymbol[1]] est égal à 'X', Alors...
		elif board[winnerSymbol[0]][winnerSymbol[1]] == 'X':
			#Afficher "le Participant 2 à gagné"
			print("Le participant 2 a gagné")
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
	#Afficher "║" + str(board[2] [0]) + "║" + str(board[2][1]) + "║" + str(board[2][2]) + "║"
	print("║" + str(board[2][0]) + "║" + str(board[2][1]) + "║" + str(board[2][2]) + "║")
	#Afficher "╚═╩═╩═╝"
	print("╚═╩═╩═╝")

#Définir une fonction morpionBlinkBoard(board) qui permet d'afficher correctement une partie de morpion avec des traits plus fin
def morpionBlinkBoard(board):
	#Initialiser un tableau 2D lighterBoard égal à board
	lighterBoard = board
	#Pour x dans 0 à 2, Faire...
	for x in range(0, 3):
		#Pour y dans 0 à 2, Faire...
		for y in range(0, 3):
			#Si lighterBoard[x][y] est égal à 'O', Alors...
			if lighterBoard[x][y] == 'O':
				#Assigner à lighterBoard[x][y] le caractère '○'
				lighterBoard[x][y] = '○'
			#Sinon Si lighterBoard[x][y] est égal à 'X', Alors...
			if lighterBoard[x][y] == 'X':
				#Assigner à ligtherBoard[x][y] le caractère '×'
				lighterBoard[x][y] = '×'

	#Pour i de 0 jusqu'à 4, Faire...
	for i in range(3):
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
		
		#Attendre 400 ms
		sleep(0.17)
		#Vider l'écran de la console
		

		#Appeler la fonction qui affiche la table normalement
		morpionPrintBoard(board)

		#Attendre 400 ms
		sleep(0.17)
		#Vider l'écran de la console
		

		#Incrémenter i de 1
		i = i + 1



#Définir une fonction morpionVsCpu() qui permet de jouer à une partie de morpion avec l'ordinateur
def morpionVsCpu():
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	board = [[' ' for i in range(3)] for i in range(3)]
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	turnOf = randint(1, 2)
	#Initialiser une variable gameOver à False
	gameOver = False
	#Initialiser une liste playerChoice à [None, None]
	playerChoice = [None, None]
	#Initialiser une liste cpuChoice à [None, None]
	cpuChoice = [None, None]
	#Initialiser une variable isValidChoice à False
	isValidChoice = False

	#Tant que gameOver est à False, Alors...
	while not gameOver:
		#Si turnOf est égal à 1, Alors...
		if turnOf == 1:
			#Vider l'écran de la console
			
			#Afficher "C'est au tour du Joueur !"
			print("C'est autour du Joueur !")
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Tant que isValidChoice est à False, Alors...
			while not isValidChoice:
				#Assigner à playerChoice[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				playerChoice[0] = int(input("Quel ligne visez-vous ? "))
				#Assigner à playerChoice[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				playerChoice[1] = int(input("Quel colonne visez-vous ? "))
				#Si playerChoice[0] ou playerChoice[1] ne sont pas compris entre 0 et 2, Alors...
				if (playerChoice[0] < 0 or playerChoice[0] > 2) or (playerChoice[1] < 0 or playerChoice[1] > 2):
					#Afficher un message d'erreur : la position n'est pas valide
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				#Sinon Si board[playerChoice[0]][playerChoice[1]] est différent de ' ', Alors...
				elif board[playerChoice[0]][playerChoice[1]] != ' ':
					#Afficher un message d'erreur : la case est occupée
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				#Sinon : board[playerChoice[0]][playerChoice[1]] est égal à ' ', Alors...
				else:
					#Assigner à isValidChoice la valeur True
					isValidChoice = True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', playerChoice)
			board = morpionTurnManager(board, 'O', playerChoice)
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Assigner à turnOf la valeur 2
			turnOf = 2

		#Sinon : turnOf est égal à 2, Alors...
		else:
			#Afficher "C'est au tour de l'Ordinateur !"
			print("C'est au tour de l'Ordinateur !")
			#Tant que isValidChoice est à False, Alors...
			while not isValidChoice:
				#Assigner à cpuChoice[0] le retour de l'appel de la fonction randint(0, 2)
				cpuChoice[0] = randint(0, 2)
				#Assigner à cpuChoice[1] le retour de l'appel de la fonction randint(0, 2)
				cpuChoice[1] = randint(0, 2)
				#Si board[cpuChoice[0]][cpuChoice[1]] est égal à ' ', Alors...
				if board[cpuChoice[0]][cpuChoice[1]] == ' ':
					#Assigner à isValidChoice la valeur True
					isValidChoice = True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', cpuChoice)
			board = morpionTurnManager(board, 'X', cpuChoice)
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Assigner à turnOf la valeur 1
			turnOf = 1
		#Assigner à isValidChoice la valeur False
		isValidChoice = False
		#Assigner à gameOver le retour de l'appel de la fonction morpionEndChecker(board)
		gameOver = morpionEndChecker(board)
	#Afficher un message de retour au menu
	print(" Retour vers le Menu")
	print(" Retour vers le Menu.")
	print(" Retour vers le Menu..")
	print(" Retour vers le Menu...")



#Définir une fonction morpionVsIA qui permet de jouer à une partie de morpion contre une IA imbattable
def morpionVsIA():
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	board = [[' ' for i in range(3)] for i in range(3)]
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	turnOf = randint(1, 2)
	#Initialiser une variable gameOver à False
	gameOver = False
	#Initialiser une liste playerChoice à [None, None]
	playerChoice = [None, None]
	#Initialiser une liste IAChoice à [None, None]
	IAChoice = [None, None]
	#Initialiser une variable IAChoosed à False
	IAChoosed = False
	#Initialiser une variable isValidChoice à False
	isValidChoice = False
	#Initialiser une variable Xcounter à 0
	Xcounter = 0
	#Initialiser une liste XXportunity à []
	XXportunity = []
	#Initialiser une variable Ocounter à 0
	Ocounter = 0
	#Initialiser une liste OOportunity à []
	OOportunity = []
	#Initialiser une varibale spaceCounter à 0
	spaceCounter = 0
	#Initialiser une variable boardStatus à "common"
	boardStatus = "common"

	#Tant que gameOver est à False, Alors...
	while not gameOver:
		#Si turnOf est égal à 1, Alors...
		if turnOf == 1:
			#Vider l'écran de la console
			#Afficher "C'est au tour du Joueur !"
			print("C'est au tour du Joueur !")
			#Tant que isValidChoice est à False, Alors...
			while not isValidChoice:
				#Assigner à playerChoice[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				playerChoice[0] = int(input("Quel ligne visez-vous ? "))
				#Assigner à playerChoice[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				playerChoice[1] = int(input("Quel colonne visez-vous ? "))
				#Si playerChoice[0] ou playerChoice[1] ne sont pas compris entre 0 et 2, Alors...
				if (playerChoice[0] < 0 or playerChoice[0] > 2) or (playerChoice[1] < 0 or playerChoice[1] > 2):
					#Afficher un message d'erreur : la position n'est pas valide
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				#Sinon Si board[playerChoice[0]][playerChoice[1]] est différent de ' ', Alors...
				elif board[playerChoice[0]][playerChoice[1]] != ' ':
					#Afficher un message d'erreur : la case est occupée
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				#Sinon : board[playerChoice[0]][playerChoice[1]] est égal à ' ', Alors...
				else:
					#Assigner à isValidChoice la valeur True
					isValidChoice = True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', playerChoice)
			board = morpionTurnManager(board, 'O', playerChoice)
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Assigner à turnOf la valeur 2
			turnOf = 2

		#Sinon : turnOf est égal à 2, Alors...
		else:
			#Afficher "C'est au tour de l'IA !"
			print("C'est au tour de l'IA !")

			#  RESET DES NOUVELLES "portunity"

			#Assigner à OOportunity la liste []
			OOportunity = []
			#Assigner à XXportunity la liste []
			XXportunity = []


			#  REMPLISSAGE DES "portunity"

			#Pour x dans 0 à 2, Faire...
			for x in range(0, 3):
				#Assigner à Ocounter la valeur 0
				Ocounter = 0
				#Assigner à Xcounter la valeur 0
				Xcounter = 0
				#Pour y dans 0 à 2, Faire...
				for y in range(0, 3):
					#Si board[x][y] est égal à 'O', Alors...
					if board[x][y] == 'O':
						#Incrémenter Ocounter de 1
						Ocounter = Ocounter + 1
					#Sinon Si board[x][y] est égal à 'X', Alors...
					elif board[x][y] == 'X':
						#Incrémenter Xcounter de 1
						Xcounter = Xcounter + 1
				#Si Ocounter est égal à 2 et Xcounter est égal à 0, Alors...
				if Ocounter == 2 and Xcounter == 0:
					#Ajouter dans OOportunity le string "r" + str(x+1)
					OOportunity.append("r" + str(x+1))
					print("   ~ OOportunité en r"+str(x+1))
					sleep(1.5)
				#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
				elif Xcounter == 2 and Ocounter == 0:
					#Ajouter dans XXportunity le string "r" + str(x+1)
					XXportunity.append("r" + str(x+1))
					print("   ~ XXportunité en r"+str(x+1))
					sleep(1.5)

			#Pour y dans 0 à 2, Faire...
			for y in range(0, 3):
				#Assigner à Ocounter la valeur 0
				Ocounter = 0
				#Assigner à Xcounter la valeur 0
				Xcounter = 0
				#Pour x dans 0 à 2, Faire...
				for x in range(0, 3):
					#Si board[x][y] est égal à 'O', Alors...
					if board[x][y] == 'O':
						#Incrémenter Ocounter de 1
						Ocounter = Ocounter + 1
					#Sinon Si board[x][y] est égal à 'X', Alors...
					elif board[x][y] == 'X':
						#Incrémenter Xcounter de 1
						Xcounter = Xcounter + 1
				#Si Ocounter est égal à 2 et Xcounter est égal à 0, Alors...
				if Ocounter == 2 and Xcounter == 0:
					#Ajouter dans OOportunity le string "c" + str(y+1)
					OOportunity.append("c" + str(y+1))
					print("   ~ OOportunité en c"+str(y+1))
					sleep(1.5)				#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
				elif Xcounter == 2 and Ocounter == 0:
					#Ajouter dans XXportunity le string "c" + str(y+1)
					XXportunity.append("c" + str(y+1))
					print("   ~ XXportunité en c"+str(y+1))
					sleep(1.5)
			#Assigner à Ocounter la valeur 0
			Ocounter = 0
			#Assigner à Xcounter la valeur 0
			Xcounter = 0
			#Pour x dans 0 à 2, Faire...
			for x in range(0, 3):
				#Si board[x][x] est égal à 'O', Alors...
				if board[x][x] == 'O':
					#Incrémenter Ocounter de 1
					Ocounter = Ocounter + 1
				#Sinon Si board[x][x] est égal à 'X', Alors...
				elif board[x][x] == 'X':
					#Incrémenter Xcounter de 1
					Xcounter = Xcounter + 1
			#Si Ocounter est égal à 2 et Xcounter est égal à 0, Alors...
			if Ocounter == 2 and Xcounter == 0:
				#Ajouter à OOportunity le string "d1"
				OOportunity.append("d1")
				print("   ~ OOportunité en d1")
				sleep(1.5)
			#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
			if Xcounter == 2 and Ocounter == 0:
				#Ajouter à XXportunity le string "d1"
				XXportunity.append("d1")
				print("   ~ XXportunité en d1")
				sleep(1.5)

			#Assigner à Ocounter la valeur 0
			Ocounter = 0
			#Assigner à Xcounter la valeur 0
			Xcounter = 0
			#Si board[0][2] est égal à 'O', Alors...
			if board[0][2] == 'O':
				#Incrémenter Ocounter de 1
				Ocounter = Ocounter + 1
			#Sinon Si board[0][2] est égal à 'X', Alors...
			elif board[0][2] == 'X':
				#Incrémenter Xcounter de 1
				Xcounter = Xcounter + 1
			#Si board[1][1] est égal à 'O', Alors...
			if board[1][1] == 'O':
				#Incrémenter Ocounter de 1
				Ocounter = Ocounter + 1
			#Sinon Si board[1][1] est égal à 'X', Alors...
			elif board[1][1] == 'X':
				#Incrémenter Xcounter de 1
				Xcounter = Xcounter + 1
			#Si board[2][0] est égal à 'O', Alors...
			if board[2][0] == 'O':
				#Incrémenter Ocounter de 1
				Ocounter = Ocounter + 1
			#Sinon Si board[2][0] est égal à 'X', Alors...
			elif board[2][0] == 'X':
				#Incrémenter Xcounter de 1
				Xcounter = Xcounter + 1
			#Si Ocounter est égal à 2 et Xocunter est égal à 0, Alors...
			if Ocounter == 2 and Xcounter == 0:
				#Ajouter à OOportunity le string "d2"
				OOportunity.append("d2")
				print("   ~ OOportunité en d2")
				sleep(1.5)
			#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
			elif Xcounter == 2 and Ocounter == 0:
				#Ajouter à XXportunity le string "d2"
				XXportunity.append("d2")
				print("   ~ XXportunité en d2")
				sleep(1.5)

			#  SAISIE D'UNE OPPORTUNITÉ DE VICTOIRE S'IL Y A

			#Si XXportunity est différente de [], Alors...
			if XXportunity != []:
				print("   ~ JE RENTRE DANS LE IF WOO")
				#Assigner à IAChoosed le retour de l'appel de la fonction randint(0, len(XXportunity)-1)
				IAChoosed = randint(0, len(XXportunity) - 1)
				print("   ~ XXportunité saisie :")
				print(XXportunity[IAChoosed])
				sleep(1.5)

				#Si XXportunity[IAChoosed][0] est égal à 'r', Alors...
				if XXportunity[IAChoosed][0] == 'r':
					#Pour y dans 0 à 2, Faire...
					for y in range(0, 3):
						#Si board[int(XXportunity[IAChoosed][1]) - 1][y] est égal à ' ', Alors...
						if board[int(XXportunity[IAChoosed][1]) - 1][y] == ' ':
							#Assigner à IAChoice[0] la valeur int(XXportunity[IAChoosed][1]) - 1
							IAChoice[0] = int(XXportunity[IAChoosed][1]) - 1
							#Assigner à IAChoice[1] la valeur y
							IAChoice[1] = y
							#Sortir de la boucle
							break

				#Si XXportunity[IAChoosed][0] est égal à 'c', Alors...
				if XXportunity[IAChoosed][0] == 'c':
					#Pour x dans 0 à 2, Faire...
					for x in range(0, 3):
						#Si board[x][int(XXportunity[IAChoosed][1]) - 1] est égal à ' ', Alors...
						if board[x][int(XXportunity[IAChoosed][1]) - 1] == ' ':
							#Assigner à IAChoice[0] la valeur x
							IAChoice[0] = x
							#Assigner à IAChoice[1] la valeur int(XXportunity[IAChoosed][1]) - 1
							IAChoice[1] = int(XXportunity[IAChoosed][1]) - 1
							#Sortir de la boucle
							break

				#Si XXportunity[IAChoosed] est égal à "d1", Alors...
				if XXportunity[IAChoosed] == "d1":
					#Pour xy dans 0 à 2, Faire...
					for xy in range(0, 3):
						#Si board[xy][xy] est égal à ' ', Alors...
						if board[xy][xy] == ' ':
							#Assigner à IAChoice[0] la valeur xy
							IAChoice[0] = xy
							#Assigner à IAChoice[1] la valeur xy
							IAChoice[1] = xy
							#Sortir de la boucle
							break

				#Si XXportunity[IAChoosed] est égal à "d2", Alors...
				if XXportunity[IAChoosed] == "d2":
					#Si board[0][2] est égal à ' ', Alors...
					if board[0][2] == ' ':
						#Assigner à IAChoice[0] la valeur 0
						IAChoice[0] = 0
						#Assigner à IAChoice[1] la valeur 2
						IAChoice[1] = 2
					#Sinon Si board[1][1] est égal à ' ', Alors...
					elif board[1][1] == ' ':
						#Assigner à IAChoice[0] la valeur 1
						IAChoice[0] = 1
						#Assigner à IAChoice[1] la valeur 1
						IAChoice[1] = 1
					#Sinon Si board[2][0] est égal à ' ', Alors...
					else:
						#Assigner à IAChoice[0] la valeur 2
						IAChoice[0] = 2
						#Assigner à IAChoice[1] la valeur 0
						IAChoice[1] = 0

			#  CONTRE D'UNE OPPORTUNITÉ DE DÉFAITE S'IL Y A

			#Sinon Si OOportunity est différente de [], Alors...
			elif OOportunity != []:
				print("   ~ JE RENTRE DANS LE ELIF WOO")
				#Assigner à IAChoosed le retour de l'appel de la fonction randint(0, len(OOportunity)-1)
				IAChoosed = randint(0, len(OOportunity) - 1)
				print(IAChoosed)
				print("   ~ OOportunité bloquée :")
				print(OOportunity[IAChoosed])
				sleep(1.5)

				#Si OOportunity[IAChoosed][0] est égal à 'r', Alors...
				if OOportunity[IAChoosed][0] == 'r':
					#Pour y dans 0 à 2, Faire...
					for y in range(0, 3):
						#Si board[int(OOportunity[IAChoosed][1]) - 1][y] est égal à ' ', Alors...
						if board[int(OOportunity[IAChoosed][1]) - 1][y] == ' ':
							#Assigner à IAChoice[0] la valeur int(OOportunity[IAChoosed][1]) - 1
							IAChoice[0] = int(OOportunity[IAChoosed][1]) - 1
							#Assigner à IAChoice[1] la valeur y
							IAChoice[1] = y
							#Sortir de la boucle
							break

				#Si OOportunity[IAChoosed][0] est égal à 'c', Alors...
				if OOportunity[IAChoosed][0] == 'c':
					#Pour x dans 0 à 2, Faire...
					for x in range(0, 3):
						#Si board[x][int(OOportunity[IAChoosed][1]) - 1] est égal à ' ', Alors...
						if board[x][int(OOportunity[IAChoosed][1]) - 1] == ' ':
							#Assigner à IAChoice[0] la valeur x
							IAChoice[0] = x
							#Assigner à IAChoice[1] la valeur int(OOportunity[IAChoosed][1]) - 1
							IAChoice[1] = int(OOportunity[IAChoosed][1]) - 1
							#Sortir de la boucle
							break

				#Si OOportunity[IAChoosed] est égal à "d1", Alors...
				if OOportunity[IAChoosed] == "d1":
					#Pour xy dans 0 à 2, Faire...
					for xy in range(0, 3):
						#Si board[xy][xy] est égal à ' ', Alors...
						if board[xy][xy] == ' ':
							#Assigner à IAChoice[0] la valeur xy
							IAChoice[0] = xy
							#Assigner à IAChoice[1] la valeur xy
							IAChoice[1] = xy
							#Sortir de la boucle
							break

				#Si OOportunity[IAChoosed] est égal à "d2", Alors...
				if OOportunity[IAChoosed] == "d2":
					#Si board[0][2] est égal à ' ', Alors...
					if board[0][2] == ' ':
						#Assigner à IAChoice[0] la valeur 0
						IAChoice[0] = 0
						#Assigner à IAChoice[1] la valeur 2
						IAChoice[1] = 2
					#Sinon Si board[1][1] est égal à ' ', Alors...
					elif board[1][1] == ' ':
						#Assigner à IAChoice[0] la valeur 1
						IAChoice[0] = 1
						#Assigner à IAChoice[1] la valeur 1
						IAChoice[1] = 1
					#Sinon : board[2][0] est égal à ' ', Alors...
					else:
						#Assigner à IAChoice[0] la valeur 2
						IAChoice[0] = 2
						#Assigner à IAChoice[1] la valeur 0
						IAChoice[1] = 0

			#  ALGORITHME DE STRATÉGIE PARFAITE SI AUCUN DES DEUX


			#Sinon, Alors...
			else:
				#Assigner à spaceCounter la valeur 0
				spaceCounter = 0
				#Pour x dans 0 à 2, Faire...
				for x in range(0, 3):
					#Pour y dans 0 à 2, Faire...
					for y in range(0, 3):
						#Si board[x][y] est égal à ' ', Alors...
						if board[x][y] == ' ':
							#Incrémenter spaceCounter de 1
							spaceCounter = spaceCounter + 1
				print("   ~ Trouvé "+str(spaceCounter)+" espace vide")
				sleep(1.5)

				#Si board[1][1] est égal à ' ', Alors...
				if board[1][1] == ' ':
					#Assigner à IAChoice[0] la valeur 1
					IAChoice[0] = 1
					#Assigner à IAChoice[1] la valeur 1
					IAChoice[1] = 1
					print("   ~ Centre récupérer")
					sleep(1.5)

				#Sinon Si spaceCounter est égal à 8, Alors...
				elif spaceCounter == 8:
					print("   ~ MODE DÉFENSE : Jeu en croix penchée")
					sleep(1.5)
					#Tant que isValidChoice est à False, Alors...
					while not isValidChoice:
						#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
						IAChoice[0] = randint(0, 2)
						#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
						IAChoice[1] = randint(0, 2)
						#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ' et IAChoice est différente de toutes les listes suivantes : [0, 1] [1, 0] [1, 2] [2, 1], Alors...
						if board[IAChoice[0]][IAChoice[1]] == ' ' and (IAChoice != [0, 1] and IAChoice != [1, 0] and IAChoice != [1, 2] and IAChoice != [2, 1]):
							#Assigner à isValidChoice la valeur True
							isValidChoice = True

				#Sinon Si spaceCounter est égal à 7, Alors...
				elif spaceCounter == 7:
					print("   ~ MODE ATTAQUE : Jeu sur la même ligne/colonne que le joueur (croix droite) OU random (croix penchée)")
					sleep(1.5)
					#Si board[0][1] ou board[2][1] est égal à 'O', Alors...
					if board[0][1] == 'O' or board[2][1] == 'O':
						#Tant que isValidChoice est à False, Alors...
						while not isValidChoice:
							#Assigner à IAChoice[0] la valeur playerChoice[0]
							IAChoice[0] = playerChoice[0]
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							IAChoice[1] = randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
							if board[IAChoice[0]][IAChoice[1]] == ' ':
								#Assigner à isValidChoice la valeur True
								isValidChoice = True

					#Sinon Si board[1][0] ou board[1][2] est égal à 'O', Alors...
					elif board[1][0] == 'O' or board[1][2] == 'O':
						#Tant que isValidChoice est à False, Alors...
						while not isValidChoice:
							#Assigner à IAChoice[0] la retour de l'appel de la fonction randint(0, 2)
							IAChoice[0] = randint(0, 2)
							#Assigner à IAChoice[1] la valeur playerChoice[1]
							IAChoice[1] = playerChoice[1]
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
							if board[IAChoice[0]][IAChoice[1]] == ' ':
								#Assigner à isValidChoice la valeur True
								isValidChoice = True

					#Sinon : le Joueur à joué dans les diagonales, Alors...
					else:
						#Tant que isValidChoice est à False, Alors...
						while not isValidChoice:
							#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
							IAChoice[0] = randint(0, 2)
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							IAChoice[1] = randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
							if board[IAChoice[0]][IAChoice[1]] == ' ':
								#Assigner à isValidChoice la valeur True
								isValidChoice = True

				#Sinon Si spaceCounter est égal à 6, Alors...
				elif spaceCounter == 6:
					print("   ~ MODE DÉFENSE : Jeu en dans le coin proche du joueur pour éviter un setup (croix droite x2) OU random croix penchée")
					sleep(1.5)
					#Si board[1][1] est égal à 'X', Alors...
					if board[1][1] == 'X':
						#Si board[0][1] et board[1][0] sont égal à 'O', Alors...
						if board[0][1] == 'O' and board[1][0] == 'O':
							#Assigner à IAChoice[0] la valeur 0
							IAChoice[0] = 0
							#Assigner à IAChoice[1] la valeur 0
							IAChoice[1] = 0
						#Sinon Si board[0][1] et board[1][2] sont égal à 'O', Alors...
						elif board[0][1] == 'O' and board[1][2] == 'O':
							#Assigner à IAChoice[0] la valeur 0
							IAChoice[0] = 0
							#Assigner à IAChoice[1] la valeur 2
							IAChoice[1] = 2
						#Sinon Si board[2][1] et board[1][0] sont égal à 'O', Alors...
						elif board[2][1] == 'O' and board[1][0] == 'O':
							#Assigner à IAChoice[0] la valeur 2
							IAChoice[0] = 2
							#Assigner à IAChoice[1] la valeur 0
							IAChoice[1] = 0
						#Sinon : board[2][1] et board[1][2] sont égal à 'O', Alors...
						else:
							#Assigner à IAChoice[0] la valeur 2
							IAChoice[0] = 2
							#Assigner à IAChoice[1] la valeur 2
							IAChoice[1] = 2

					#Sinon, Alors...
					else:
						#Tant que isValidChoice est à False, Alors...
						while not isValidChoice:
							#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
							IAChoice[0] = randint(0, 2)
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							IAChoice[1] = randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
							if board[IAChoice[0]][IAChoice[1]] == ' ' and (IAChoice != [0, 1] and IAChoice != [1, 0] and IAChoice != [1, 2] and IAChoice != [2, 1]):
								#Assigner à isValidChoice la valeur True
								isValidChoice = True

				#Sinon Si spaceCounter est égal à 5, Alors...
				elif spaceCounter == 5:
					print("   ~ MODE ATTAQUE : Jeu dans un coin sans voisin pour setup le joueur OU pas dans les coins (pas setupable)")
					sleep(1.5)
					#Si board[0][0], board[0][1] et board[1][0] sont égal à ' ', Alors...
					if board[0][0] == ' ' and board[0][1] == ' ' and board[1][0] == ' ':
						#Assigner à IAChoice[0] la valeur 0
						IAChoice[0] = 0
						#Assigner à IAChoice[1] la valeur 0
						IAChoice[1] = 0
					#Sinon Si board[0][2], board[0][1] et board[1][2] sont égal à ' ', Alors...
					elif board[0][2] == ' ' and board[0][1] == ' ' and board[1][2] == ' ':
						#Assigner à IAChoice[0] la valeur 0
						IAChoice[0] = 0
						#Assigner à IAChoice[1] la valeur 2
						IAChoice[1] = 2
					#Sinon Si board[2][0], board[2][1] et board[1][0] sont égal à ' ', Alors...
					elif board[2][0] == ' ' and board[2][1] == ' ' and board[1][0] == ' ':
						#Assigner à IAChoice[0] la valeur 2
						IAChoice[0] = 2
						#Assigner à IAChoice[1] la valeur 0
						IAChoice[1] = 0
					#Sinon Si board[2][2], board[2][1] et board[1][2] sont égal à ' ', Alors...
					elif board[2][2] == ' ' and board[2][1] == ' ' and board[1][2] == ' ':
						#Assigner à IAChoice[0] la valeur 2
						IAChoice[0] = 2
						#Assigner à IAChoice[1] la valeur 2
						IAChoice[1] = 2

					#Sinon : le Joueur ne s'est pas mis en danger, Alors...
					else:
						#Tant que isValidChoice est à False, Alors...
						while not isValidChoice:
							#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
							IAChoice[0] = randint(0, 2)
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							IAChoice[1] = randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ' et IAChoice est différent de toutes les listes suivante : [0, 0] [0, 2] [2, 0] [2, 2], Alors...
							if board[IAChoice[0]][IAChoice[1]] == ' ' and (IAChoice != [0, 0] and IAChoice != [0, 2] and IAChoice != [2, 0] and IAChoice != [2, 2]):
								#Assigner à isValidChoice la valeur True
								isValidChoice = True

				#Sinon : Aucune occasion de victoire ou défaite assurée n'est présente, Alors...
				else:
					print("   ~ MODE RANDOM")
					sleep(1.5)
					#Tant que isValidChoice est à False, Alors...
					while not isValidChoice:
						#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
						IAChoice[0] = randint(0, 2)
						#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
						IAChoice[1] = randint(0, 2)
						#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ' et IAChoice est différent de toutes les listes suivante : [0, 0] [0, 2] [2, 0] [2, 2], Alors...
						if board[IAChoice[0]][IAChoice[1]] == ' ':
							#Assigner à isValidChoice la valeur True
							isValidChoice = True
								
			#  ON APPLIQUE LA DÉCISION DE L'IA


			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', IAChoice)
			print("   ~ IAChoice, mesdames et messieurs")
			print(IAChoice)
			board = morpionTurnManager(board, 'X', IAChoice)
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Assigner à turnOf la valeur 1
			turnOf = 1
		#Assigner à isValidChoice la valeur False
		isValidChoice = False
		#Assigner à IAChoosed la valeur False
		IAChoosed = False
		#Assigner à gameOver le retour de l'appel de la fonction morpionEndChecker(board)
		gameOver = morpionEndChecker(board)
	#Afficher un message de retour au menu



#Définir une fonction morpionVsPlayer qui permet de jouer à une partie de morpion contre un autre joueur
def morpionVsPlayer():
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	board = [[' ' for i in range(3)] for i in range(3)]
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	turnOf = randint(1, 2)
	#Initialiser une variable gameOver à False
	gameOver = False
	#Initialiser une liste player1Choice à [None, None]
	playerChoice1 = [None, None]
	#Initialiser une liste player2Choice à [None, None]
	playerChoice2 = [None, None]
	#Initialiser une variable isValidChoice à False
	isValidChoice = False
	#Tant que gameOver est à False, Alors...
	while not gameOver:
		#Si turnOf est égal à 1, Alors...
		if turnOf == 1:
			#Vider l'écran de la console
			
			#Afficher "C'est au tour du Joueur 1 !"
			print("C'est au tour du Joueur 1 !")
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Tant que isValidChoice est à False, Alors...
			while not isValidChoice:
				#Assigner à playerChoice1[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				playerChoice1[0] = int(input("Quel ligne visez-vous ?"))
				#Assigner à playerChoice1[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				playerChoice1[1] = int(input("Quel colonne visez-vous ?"))
				#Si playerChoice1[0] ou playerChoice1[1] ne sont pas compris entre 0 et 2, Alors...
				if (playerChoice1[0] < 0 or playerChoice1[0] > 2) or (playerChoice1[1] < 0 or playerChoice1[1] > 2):
					#Afficher un message d'erreur : la position n'est pas valide
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				#Sinon Si board[playerChoice1[0]][playerChoice1[1]] est différent de ' ', Alors...
				elif board[playerChoice1[0]][playerChoice1[1]] != ' ':
					#Afficher un message d'erreur : la case est occupée
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				#Sinon : board[playerChoice1[0]][playerChoice1[1]] est égal à ' ', Alors...
				else:
					#Assigner à isValidChoice la valeur True
					isValidChoice = True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'O', playerChoice1)
			board = morpionTurnManager(board, 'O', playerChoice1)
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Assigner à turnOf la valeur 2
			turnOf = 2

		#Sinon : turnOf est égal à 2, Alors...
		else:
			#Vider l'écran de la console
			
			#Afficher "C'est au tour du Joueur 2 !"
			print("C'est au Joueur 2 !")
			#Tant que isValidChoice est à False, Alors...
			while not isValidChoice:
				#Assigner à playerChoice2[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
				playerChoice2[0] = int(input("Quel ligne visez-vous ?"))
				#Assigner à playerChoice2[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
				playerChoice2[1] = int(input("Quel colonne visez-vous ?"))
				#Si playerChoice2[0] ou playerChoice2[1] ne sont pas compris entre 0 et 2, Alors...
				if (playerChoice2[0] < 0 or playerChoice2[0] > 2) or (playerChoice2[1] < 0 or playerChoice2[1] > 2):
					#Afficher un message d'erreur : la position n'est pas valide
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				#Sinon Si board[playerChoice2[0]][playerChoice2[1]] est différent de ' ', Alors...
				elif board[playerChoice2[0]][playerChoice2[1]] != ' ':
					#Afficher un message d'erreur : la case est occupée
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				#Sinon : board[playerChoice2[0]][playerChoice2[1]] est égal à ' ', Alors...
				else:
					#Assigner à isValidChoice la valeur True
					isValidChoice = True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', playerChoice2)
			board = morpionTurnManager(board, 'X', playerChoice2)
			#Appeler la fonction morpionPrintBoard(board)
			morpionPrintBoard(board)
			#Assigner à turnOf la valeur 1
			turnOf = 1
		#Assigner à isValidChoice la valeur False
		isValidChoice = False
		#Assigner à gameOver le retour de l'appel de la fonction morpionEndChecker(board)
		gameOver = morpionEndChecker(board)
	#Afficher un message de retour au menu
	print(" Retour vers le Menu")
	print(" Retour vers le Menu.")
	print(" Retour vers le Menu..")
	print(" Retour vers le Menu...")


#Définir une fonction morpion() qui permet de lancer une partie de morpion
def morpion():
	#Initialiser une variable gameClose à False
	gameClose = False
	#Initialiser une variable menuNav à None
	menuNav = None

	#Vider l'écran de la console
	

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

#

morpion()