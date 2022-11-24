#Admettre la fonction sleep() qui fait attendre le programme
#Admettre la fonction randint() qui renvoi un entier aléatoire entre 2 valeurs incluses
#Admettre la fonction os() qui permet d'éxecuter des commandes dans la console
#Préparation pour vider le contenu de la console


#Définir une conftion morpionTurnManager(board, symbol, coordinates) qui permet d'éditer un tableau de morpion avec un nouveau symbole
	#Initialiser un tableau 2D updatedBoard égal à board
	#Assigner à updatedBoard[coordinates[0], coordinates[1]] le caractère symbol
	#Retourner updatedBoard


#Définir une fonction morpionEndChecker(board) qui permet de définir si une partie de morpion est terminé, et quel en est le résultat
	#Initialiser une variable xCoord à 0
	#Initialiser une variable yCoord à 0
	#Initialiser une variable gameStatus à None
	#Initialiser une liste winnerSymbol à [None, None]

	#Pour xCoord dans 3, Faire...
		#Si board[xCoord][0] est égal à board[xCoord][1] ET board[xCoord][1] est égal à board[xCoord][2], Alors...
			#Assigner à gameStatus le string "winned"
			#Assigner à winnerSymbol la liste [xCoord, 1]
			#Sortir de la boucle
	#Pour yCoord dans 3, Faire...
		#Si board[0][yCoord] est égal à board[1][yCoord] ET board[1][yCoord] est égal à board[2][yCoord], Alors...
			#Assigner à gameStatus le string "winned"
			#Assigner à winnerSymbol la liste [1, yCoord]
			#Sortir de la boucle
	#Si board[0][0] est égal à board[1][1] ET board[1][1] est égal à board[2][2], Alors...
		#Assigner à gameStatus le string "winned"
		#Assigner à winnerSymbol la liste [1, 1]
	#Si board[2][0] est égal à board[1][1] ET board[1][1] est égal à board[0][2], Alors...
		#Assigner à gameStatus le string "winned"
		#Assigner à winnerSymbol la liste [1, 1]

	#Si gameStatus est égal à None, Alors...
		#Assigner à gameStatus le string "blocked"
		#Pour x dans 0 à 2, Faire...
			#Pour y dans 0 à 2, Faire...
				#Si board[x][y] est égal à ' ', Alors...
					#Assigner à gameStatus la valeur None
					#Sortir de la boucle

	#Si gameStatus est égal à "winned", Alors...
		#Afficher "!!! VICTOIRE !!!"
		#Si board[winnerSymbol[0]][winnerSymbol[1]] est égal à 'O', Alors...
			#Afficher "le Participant 1 à gagné"
		#Sinon Si board[winnerSymbol[0]][winnerSymbol[1]] est égal à 'X', Alors...
			#Afficher "le Participant 2 à gagné"
		#Retourner True
	#Sinon Si gameStatus est égal à "blocked", Alors...
		#Afficher "!!! ÉGALITÉ !!!"
		#Retourner True
	#Sinon : la partie n'est ni bloquée ni gagnée, Alors...
		#Retourner False


#Définir une fonction morpionPrintBoard(board) qui permet d'afficher correctement une partie de morpion
	#Afficher "╔═╦═╦═╗"
	#Afficher "║" + str(board[0][0]) + "║" + str(board[0][1]) + "║" + str(board[0][2]) + "║"
	#Afficher "╠═╬═╬═╣"
	#Afficher "║" + str(board[1][0]) + "║" + str(board[1][1]) + "║" + str(board[1][2]) + "║"
	#Afficher "╠═╬═╬═╣"
	#Afficher "║" + str(board[2] [0]) + "║" + str(board[2][1]) + "║" + str(board[2][2]) + "║"
	#Afficher "╚═╩═╩═╝"


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
			#Appeler la fonction morpionPrintBoard(board)
			#Assigner à turnOf la valeur 2

		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour de l'Ordinateur !"
			#Tant que isValidChoice est à False, Alors...
				#Assigner à cpuChoice[0] le retour de l'appel de la fonction randint(0, 2)
				#Assigner à cpuChoice[1] le retour de l'appel de la fonction randint(0, 2)
				#Si board[cpuChoice[0]][cpuChoice[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
			#Assigner à board le retour de l'appel de la fonction morpionTurnManager(board, 'X', cpuChoice)
			#Appeler la fonction morpionPrintBoard(board)
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
	#Initialiser une liste XXportunity à []
	#Initialiser une variable Ocounter à 0
	#Initialiser une liste OOportunity à []
	#Initialiser une varibale spaceCounter à 0

	#Tant que gameOver est à False, Alors...

		#Si turnOf est égal à 1, Alors...
			#Vider l'écran de la console
			#Afficher "C'est au tour du Joueur !"
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
			#Appeler la fonction morpionPrintBoard(board)
			#Assigner à turnOf la valeur 2

		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour de l'IA !"

			#  RESET DES NOUVELLES "portunity"

			#Assigner à OOportunity la liste []
			#Assigner à XXportunity la liste []

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
			#Si Ocounter est égal à 2 et Xcounter est égal à 0, Alors...
				#Ajouter à OOportunity le string "d1"
			#Sinon Si Xcounter est égal à 2 et Ocounter est égal à 0, Alors...
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

			#Si XXportunity est différente de [], Alors...
				#Assigner à IAChoosed le retour de l'appel de la fonction randint(0, len(XXportunity)-1)

				#Si XXportunity[IAChoosed][0] est égal à 'r', Alors...
					#Pour y dans 0 à 2, Faire...
						#Si board[int(XXportunity[IAChoosed][1]) - 1][y] est égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur int(XXportunity[IAChoosed][1]) - 1
							#Assigner à IAChoice[1] la valeur y
							#Sortir de la boucle

				#Si XXportunity[IAChoosed][0] est égal à 'c', Alors...
					#Pour x dans 0 à 2, Faire...
						#Si board[x][int(XXportunity[IAChoosed][1]) - 1] est égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur x
							#Assigner à IAChoice[1] la valeur int(XXportunity[IAChoosed][1]) - 1
							#Sortir de la boucle

				#Si XXportunity[IAChoosed] est égal à "d1", Alors...
					#Pour xy dans 0 à 2, Faire...
						#Si board[xy][xy] est égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur xy
							#Assigner à IAChoice[1] la valeur xy
							#Sortir de la boucle

				#Si XXportunity[IAChoosed] est égal à "d2", Alors...
					#Si board[0][2] est égal à ' ', Alors...
						#Assigner à IAChoice[0] la valeur 0
						#Assigner à IAChoice[1] la valeur 2
					#Sinon Si board[1][1] est égal à ' ', Alors...
						#Assigner à IAChoice[0] la valeur 1
						#Assigner à IAChoice[1] la valeur 1
					#Sinon Si board[2][0] est égal à ' ', Alors...
						#Assigner à IAChoice[0] la valeur 2
						#Assigner à IAChoice[1] la valeur 0

			#  CONTRE D'UNE OPPORTUNITÉ DE DÉFAITE S'IL Y A


			#Sinon Si OOportunity est différente de [], Alors...
				#Assigner à IAChoosed le retour de l'appel de la fonction randint(0, len(OOportunity)-1)
				
				#Si OOportunity[IAChoosed][0] est égal à 'r', Alors...
					#Pour y dans 0 à 2, Faire...
						#Si board[int(OOportunity[IAChoosed][1]) - 1][y] est égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur int(OOportunity[IAChoosed][1]) - 1
							#Assigner à IAChoice[1] la valeur y
							#Sortir de la boucle
							
				#Si OOportunity[IAChoosed][0] est égal à 'c', Alors...
					#Pour x dans 0 à 2, Faire...
						#Si board[x][int(OOportunity[IAChoosed][1]) - 1] est égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur x
							#Assigner à IAChoice[1] la valeur int(OOportunity[IAChoosed][1]) - 1
							#Sortir de la boucle
							
				#Si OOportunity[IAChoosed] est égal à "d1", Alors...
					#Pour xy dans 0 à 2, Faire...
						#Si board[xy][xy] est égal à ' ', Alors...
							#Assigner à IAChoice[0] la valeur xy
							#Assigner à IAChoice[1] la valeur xy
							#Sortir de la boucle
							
				#Si OOportunity[IAChoosed] est égal à "d2", Alors...
					#Si board[0][2] est égal à ' ', Alors...
						#Assigner à IAChoice[0] la valeur 0
						#Assigner à IAChoice[1] la valeur 2
					#Sinon Si board[1][1] est égal à ' ', Alors...
						#Assigner à IAChoice[0] la valeur 1
						#Assigner à IAChoice[1] la valeur 1
					#Sinon : board[2][0] est égal à ' ', Alors...
						#Assigner à IAChoice[0] la valeur 2
						#Assigner à IAChoice[1] la valeur 0

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
					
				#Sinon Si spaceCounter est égal à 8, Alors...
					#Tant que isValidChoice est à False, Alors...
						#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
						#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
						#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ' et IAChoice est différente de toutes les listes suivantes : [0, 1] [1, 0] [1, 2] [2, 1], Alors...
							#Assigner à isValidChoice la valeur True
							
				#Sinon Si spaceCounter est égal à 7, Alors...
					#Si board[0][1] ou board[2][1] est égal à 'O', Alors...
						#Tant que isValidChoice est à False, Alors...
							#Assigner à IAChoice[0] la valeur playerChoice[0]
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
								#Assigner à isValidChoice la valeur True
								
					#Sinon Si board[1][0] ou board[1][2] est égal à 'O', Alors...
						#Tant que isValidChoice est à False, Alors...
							#Assigner à IAChoice[0] la retour de l'appel de la fonction randint(0, 2)
							#Assigner à IAChoice[1] la valeur playerChoice[1]
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
								#Assigner à isValidChoice la valeur True
								
					#Sinon : le Joueur à joué dans les diagonales, Alors...
						#Tant que isValidChoice est à False, Alors...
							#Assigner à IAChoice[0] le retour de l'appel de la fonction randint(0, 2)
							#Assigner à IAChoice[1] le retour de l'appel de la fonction randint(0, 2)
							#Si board[IAChoice[0]][IAChoice[1]] est égal à ' ', Alors...
								#Assigner à isValidChoice la valeur True
								
				#Sinon Si spaceCounter est égal à 6, Alors...
					#Si board[1][1] est égal à 'X', Alors...
						#Si board[0][1] et board[1][0] sont égal à 'O', Alors...
							#Assigner à IAChoice[0] la valeur 0
							#Assigner à IAChoice[1] la valeur 0
						#Sinon Si board[0][1] et board[1][2] sont égal à 'O', Alors...
							#Assigner à IAChoice[0] la valeur 0
							#Assigner à IAChoice[1] la valeur 2
						#Sinon Si board[2][1] et board[1][0] sont égal à 'O', Alors...
							#Assigner à IAChoice[0] la valeur 2
							#Assigner à IAChoice[1] la valeur 0
						#Sinon : board[2][1] et board[1][2] sont égal à 'O', Alors...
							#Assigner à IAChoice[0] la valeur 2
							#Assigner à IAChoice[1] la valeur 2
							
				#Sinon Si spaceCounter est égal à 5, Alors...
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
			#Appeler la fonction morpionPrintBoard(board)
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
			#Appeler la fonction morpionPrintBoard(board)
			#Assigner à turnOf la valeur 2

		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour du Joueur 2 !"
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
			#Appeler la fonction morpionPrintBoard(board)
			#Assigner à turnOf la valeur 1

		#Assigner à isValidChoice la valeur False
		#Assigner à gameOver le retour de l'appel de la fonction morpionEndChecker(board)
	#Afficher un message de retour au menu



#Définir une fonction morpion() qui permet de lancer une partie de morpion
	#Initialiser une variable gameClose à False
	#Initialiser une variable menuNav à None

	#Tant que gameClose est égal à False, Alors...
		#Afficher le header du menu
		#Afficher la commande pour quitter le jeu
		#Afficher la commande pour lancer une partie contre l'ordinateur
		#Afficher la commande pour lancer une partie contre l'IA
		#Afficher la commence pour lancer une partie contre un autre joueur
		#Afficher le footer du menu

		#Assigner à menuNav le retour d'input("Votre choix : ")
		#Si menuNav est égal à 0, Alors...
			#Assigner à gameClose la valeur True
		#Sinon Si menuNav est égal à 1, Alors...
			#Appeler la fonction morpionVsCpu
		#Sinon Si menuNav est égal à 2, Alors...
			#Appeler la fonction morpionVsIA
		#Sinon Si menuNav est égal à 3, Alors...
			#Appeler la fonction morpionVsPlayer
		#Sinon, Alors...
			#Afficher un message d'erreur
	#Afficher un message de fermeture




from time import sleep
from random import randint
import os
clear = lambda: os.system('cls')


def morpionTurnManager(board, symbol, coordinates):
	updatedBoard = board
	updatedBoard[coordinates[0]][coordinates[1]] = symbol
	return updatedBoard


def morpionEndChecker(board):
	xCoord = 0
	yCoord = 0
	gameStatus = None
	winnerSymbol = [None, None]

	for xCoord in range(3):
		if (board[xCoord][0] == board[xCoord][1] and board[xCoord][1] == board[xCoord][2]) and board[xCoord][0] != ' ':
			gameStatus = "winned"
			winnerSymbol = [xCoord, 1]
			break
	for yCoord in range(3):
		if (board[0][yCoord] == board[1][yCoord]  and board[1][yCoord] == board[2][yCoord]) and board[0][yCoord] != ' ':
			gameStatus = "winned"
			winnerSymbol = [1, yCoord]
			break
	if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != ' ':
		gameStatus = "winned"
		winnerSymbol = [1,1]
	if (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[2][0] != ' ':
		gameStatus = "winned"
		winnerSymbol = [1, 1]

	if gameStatus == None:
		gameStatus = "blocked"
		for x in range(0, 3):
			for y in range(0, 3):
				if board[x][y] == ' ':
					gameStatus = None
					break

	if gameStatus == "winned":
		print("!!! VICTOIRE !!!")
		if board[winnerSymbol[0]][winnerSymbol[1]] == 'O':
			print("Le participant 1 a gagné")
		elif board[winnerSymbol[0]][winnerSymbol[1]] == 'X':
			print("Le participant 2 a gagné")
		return True
	elif gameStatus == "blocked":
		print("!!! ÉGALITÉ !!!")
		return True
	else:
		return False


def morpionPrintBoard(board):
	print("╔═╦═╦═╗")
	print("║" + str(board[0][0]) + "║" + str(board[0][1]) + "║" + str(board[0][2]) + "║")
	print("╠═╬═╬═╣")
	print("║" + str(board[1][0]) + "║" + str(board[1][1]) + "║" + str(board[1][2]) + "║")
	print("╠═╬═╬═╣")
	print("║" + str(board[2][0]) + "║" + str(board[2][1]) + "║" + str(board[2][2]) + "║")
	print("╚═╩═╩═╝")


def morpionVsCpu():
	board = [[' ' for i in range(3)] for i in range(3)]
	turnOf = randint(1, 2)
	gameOver = False
	playerChoice = [None, None]
	cpuChoice = [None, None]
	isValidChoice = False

	while not gameOver:

		if turnOf == 1:
			print("C'est autour du Joueur !")
			morpionPrintBoard(board)
			while not isValidChoice:
				playerChoice[0] = int(input("Quel ligne visez-vous ? "))
				playerChoice[1] = int(input("Quel colonne visez-vous ? "))
				if (playerChoice[0] < 0 or playerChoice[0] > 2) or (playerChoice[1] < 0 or playerChoice[1] > 2):
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				elif board[playerChoice[0]][playerChoice[1]] != ' ':
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				else:
					isValidChoice = True
			board = morpionTurnManager(board, 'O', playerChoice)
			morpionPrintBoard(board)
			turnOf = 2

		else:
			print("C'est au tour de l'Ordinateur !")
			while not isValidChoice:
				cpuChoice[0] = randint(0, 2)
				cpuChoice[1] = randint(0, 2)
				if board[cpuChoice[0]][cpuChoice[1]] == ' ':
					isValidChoice = True
			board = morpionTurnManager(board, 'X', cpuChoice)
			morpionPrintBoard(board)
			turnOf = 1

		isValidChoice = False
		gameOver = morpionEndChecker(board)
	print(" Retour vers le Menu")
	print(" Retour vers le Menu.")
	print(" Retour vers le Menu..")
	print(" Retour vers le Menu...")


def morpionVsIA():
	board = [[' ' for i in range(3)] for i in range(3)]
	turnOf = randint(1, 2)
	gameOver = False
	playerChoice = [None, None]
	IAChoice = [None, None]
	IAChoosed = False
	isValidChoice = False
	Xcounter = 0
	XXportunity = []
	Ocounter = 0
	OOportunity = []
	spaceCounter = 0

	while not gameOver:

		if turnOf == 1:
			print("C'est au tour du Joueur !")
			while not isValidChoice:
				playerChoice[0] = int(input("Quel ligne visez-vous ? "))
				playerChoice[1] = int(input("Quel colonne visez-vous ? "))
				if (playerChoice[0] < 0 or playerChoice[0] > 2) or (playerChoice[1] < 0 or playerChoice[1] > 2):
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				elif board[playerChoice[0]][playerChoice[1]] != ' ':
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				else:
					isValidChoice = True
			board = morpionTurnManager(board, 'O', playerChoice)
			morpionPrintBoard(board)
			turnOf = 2

		else:
			print("C'est au tour de l'IA !")
			OOportunity = []
			XXportunity = []

			for x in range(0, 3):
				Ocounter = 0
				Xcounter = 0
				for y in range(0, 3):
					if board[x][y] == 'O':
						Ocounter = Ocounter + 1
					elif board[x][y] == 'X':
						Xcounter = Xcounter + 1
				if Ocounter == 2 and Xcounter == 0:
					OOportunity.append("r" + str(x+1))
				elif Xcounter == 2 and Ocounter == 0:
					XXportunity.append("r" + str(x+1))
			for y in range(0, 3):
				Ocounter = 0
				Xcounter = 0
				for x in range(0, 3):
					if board[x][y] == 'O':
						Ocounter = Ocounter + 1
					elif board[x][y] == 'X':
						Xcounter = Xcounter + 1
				if Ocounter == 2 and Xcounter == 0:
					OOportunity.append("c" + str(y+1))
				elif Xcounter == 2 and Ocounter == 0:
					XXportunity.append("c" + str(y+1))
			Ocounter = 0
			Xcounter = 0
			for x in range(0, 3):
				if board[x][x] == 'O':
					Ocounter = Ocounter + 1
				elif board[x][x] == 'X':
					Xcounter = Xcounter + 1
			if Ocounter == 2 and Xcounter == 0:
				OOportunity.append("d1")
			if Xcounter == 2 and Ocounter == 0:
				XXportunity.append("d1")

			Ocounter = 0
			Xcounter = 0
			if board[0][2] == 'O':
				Ocounter = Ocounter + 1
			elif board[0][2] == 'X':
				Xcounter = Xcounter + 1
			if board[1][1] == 'O':
				Ocounter = Ocounter + 1
			elif board[1][1] == 'X':
				Xcounter = Xcounter + 1
			if board[2][0] == 'O':
				Ocounter = Ocounter + 1
			elif board[2][0] == 'X':
				Xcounter = Xcounter + 1
			if Ocounter == 2 and Xcounter == 0:
				OOportunity.append("d2")
			elif Xcounter == 2 and Ocounter == 0:
				XXportunity.append("d2")
			if XXportunity != []:
				IAChoosed = randint(0, len(XXportunity) - 1)

				if XXportunity[IAChoosed][0] == 'r':
					for y in range(0, 3):
						if board[int(XXportunity[IAChoosed][1]) - 1][y] == ' ':
							IAChoice[0] = int(XXportunity[IAChoosed][1]) - 1
							IAChoice[1] = y
							break

				if XXportunity[IAChoosed][0] == 'c':
					for x in range(0, 3):
						if board[x][int(XXportunity[IAChoosed][1]) - 1] == ' ':
							IAChoice[0] = x
							IAChoice[1] = int(XXportunity[IAChoosed][1]) - 1
							break

				if XXportunity[IAChoosed] == "d1":
					for xy in range(0, 3):
						if board[xy][xy] == ' ':
							IAChoice[0] = xy
							IAChoice[1] = xy
							break

				if XXportunity[IAChoosed] == "d2":
					if board[0][2] == ' ':
						IAChoice[0] = 0
						IAChoice[1] = 2
					elif board[1][1] == ' ':
						IAChoice[0] = 1
						IAChoice[1] = 1
					else:
						IAChoice[0] = 2
						IAChoice[1] = 0

			elif OOportunity != []:
				IAChoosed = randint(0, len(OOportunity) - 1)

				if OOportunity[IAChoosed][0] == 'r':
					for y in range(0, 3):
						if board[int(OOportunity[IAChoosed][1]) - 1][y] == ' ':
							IAChoice[0] = int(OOportunity[IAChoosed][1]) - 1
							IAChoice[1] = y
							break

				if OOportunity[IAChoosed][0] == 'c':
					for x in range(0, 3):
						if board[x][int(OOportunity[IAChoosed][1]) - 1] == ' ':
							IAChoice[0] = x
							IAChoice[1] = int(OOportunity[IAChoosed][1]) - 1
							break

				if OOportunity[IAChoosed] == "d1":
					for xy in range(0, 3):
						if board[xy][xy] == ' ':
							IAChoice[0] = xy
							IAChoice[1] = xy
							break

				if OOportunity[IAChoosed] == "d2":
					if board[0][2] == ' ':
						IAChoice[0] = 0
						IAChoice[1] = 2
					elif board[1][1] == ' ':
						IAChoice[0] = 1
						IAChoice[1] = 1
					else:
						IAChoice[0] = 2
						IAChoice[1] = 0

			else:
				spaceCounter = 0
				for x in range(0, 3):
					for y in range(0, 3):
						if board[x][y] == ' ':
							spaceCounter = spaceCounter + 1

				if board[1][1] == ' ':
					IAChoice[0] = 1
					IAChoice[1] = 1

				elif spaceCounter == 8:
					while not isValidChoice:
						IAChoice[0] = randint(0, 2)
						IAChoice[1] = randint(0, 2)
						if board[IAChoice[0]][IAChoice[1]] == ' ' and (IAChoice != [0, 1] and IAChoice != [1, 0] and IAChoice != [1, 2] and IAChoice != [2, 1]):
							isValidChoice = True

				elif spaceCounter == 7:
					if board[0][1] == 'O' or board[2][1] == 'O':
						while not isValidChoice:
							IAChoice[0] = playerChoice[0]
							IAChoice[1] = randint(0, 2)
							if board[IAChoice[0]][IAChoice[1]] == ' ':
								isValidChoice = True

					elif board[1][0] == 'O' or board[1][2] == 'O':
						while not isValidChoice:
							IAChoice[0] = randint(0, 2)
							IAChoice[1] = playerChoice[1]
							if board[IAChoice[0]][IAChoice[1]] == ' ':
								isValidChoice = True

					else:
						while not isValidChoice:
							IAChoice[0] = randint(0, 2)
							IAChoice[1] = randint(0, 2)
							if board[IAChoice[0]][IAChoice[1]] == ' ':
								isValidChoice = True

				elif spaceCounter == 6:
					if board[1][1] == 'X':
						if board[0][1] == 'O' and board[1][0] == 'O':
							IAChoice[0] = 0
							IAChoice[1] = 0
						elif board[0][1] == 'O' and board[1][2] == 'O':
							IAChoice[0] = 0
							IAChoice[1] = 2
						elif board[2][1] == 'O' and board[1][0] == 'O':
							IAChoice[0] = 2
							IAChoice[1] = 0
						else:
							IAChoice[0] = 2
							IAChoice[1] = 2

					else:
						while not isValidChoice:
							IAChoice[0] = randint(0, 2)
							IAChoice[1] = randint(0, 2)
							if board[IAChoice[0]][IAChoice[1]] == ' ' and (IAChoice != [0, 1] and IAChoice != [1, 0] and IAChoice != [1, 2] and IAChoice != [2, 1]):
								isValidChoice = True

				elif spaceCounter == 5:
					if board[0][0] == ' ' and board[0][1] == ' ' and board[1][0] == ' ':
						IAChoice[0] = 0
						IAChoice[1] = 0
					elif board[0][2] == ' ' and board[0][1] == ' ' and board[1][2] == ' ':
						IAChoice[0] = 0
						IAChoice[1] = 2
					elif board[2][0] == ' ' and board[2][1] == ' ' and board[1][0] == ' ':
						IAChoice[0] = 2
						IAChoice[1] = 0
					elif board[2][2] == ' ' and board[2][1] == ' ' and board[1][2] == ' ':
						IAChoice[0] = 2
						IAChoice[1] = 2

					else:
						while not isValidChoice:
							IAChoice[0] = randint(0, 2)
							IAChoice[1] = randint(0, 2)
							if board[IAChoice[0]][IAChoice[1]] == ' ' and (IAChoice != [0, 0] and IAChoice != [0, 2] and IAChoice != [2, 0] and IAChoice != [2, 2]):
								isValidChoice = True

				else:
					while not isValidChoice:
						IAChoice[0] = randint(0, 2)
						IAChoice[1] = randint(0, 2)
						if board[IAChoice[0]][IAChoice[1]] == ' ':
							isValidChoice = True

			board = morpionTurnManager(board, 'X', IAChoice)
			morpionPrintBoard(board)
			turnOf = 1

		isValidChoice = False
		IAChoosed = False
		gameOver = morpionEndChecker(board)


def morpionVsPlayer():
	board = [[' ' for i in range(3)] for i in range(3)]
	turnOf = randint(1, 2)
	gameOver = False
	playerChoice1 = [None, None]
	playerChoice2 = [None, None]
	isValidChoice = False
	while not gameOver:

		if turnOf == 1:
			print("C'est au tour du Joueur 1 !")
			morpionPrintBoard(board)
			while not isValidChoice:
				playerChoice1[0] = int(input("Quel ligne visez-vous ?"))
				playerChoice1[1] = int(input("Quel colonne visez-vous ?"))
				if (playerChoice1[0] < 0 or playerChoice1[0] > 2) or (playerChoice1[1] < 0 or playerChoice1[1] > 2):
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				elif board[playerChoice1[0]][playerChoice1[1]] != ' ':
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				else:
					isValidChoice = True
			board = morpionTurnManager(board, 'O', playerChoice1)
			morpionPrintBoard(board)
			turnOf = 2

		else:
			print("C'est au Joueur 2 !")
			while not isValidChoice:
				playerChoice2[0] = int(input("Quel ligne visez-vous ?"))
				playerChoice2[1] = int(input("Quel colonne visez-vous ?"))
				if (playerChoice2[0] < 0 or playerChoice2[0] > 2) or (playerChoice2[1] < 0 or playerChoice2[1] > 2):
					print("     !! ERR !!\nLa position spécifié n'est pas valide...\n\n")
				elif board[playerChoice2[0]][playerChoice2[1]] != ' ':
					print("     !! ERR !!\nLa case spécifié est occupée...\n\n")
				else:
					isValidChoice = True
			board = morpionTurnManager(board, 'X', playerChoice2)
			morpionPrintBoard(board)
			turnOf = 1
		isValidChoice = False
		gameOver = morpionEndChecker(board)
	print(" Retour vers le Menu")
	print(" Retour vers le Menu.")
	print(" Retour vers le Menu..")
	print(" Retour vers le Menu...")



def morpion():
	gameClose = False
	menuNav = None
	
	while gameClose == False:
		print("----------=<(MORPION)>=----------")
		print("0 - Quitter")
		print("1 - Partie contre l'Ordinateur")
		print("2 - Partie contre l'IA")
		print("3 - Partie contre un Joueur")
		print("----------====]<⌂>[====----------")

		menuNav = int(input("Votre choix : "))
		if menuNav == 0:
			gameClose = True
		elif menuNav == 1:
			morpionVsCpu()
		elif menuNav == 2:
			morpionVsIA()
		elif menuNav == 3:
			morpionVsPlayer()
		else:
			print("\nOPTION INEXISTANTE\n")
	print("fermeture")
	print("fermeture.")
	print("fermeture..")
	print("fermeture...")


morpion()