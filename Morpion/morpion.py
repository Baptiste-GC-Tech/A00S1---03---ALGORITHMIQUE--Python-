#DEBUT

#Admettre la fonction randint() qui renvoi un entier aléatoire entre 2 valeurs incluses
#Admettre la fonction os() qui permet d'éxecuter des commandes dans la console

#Définir une conftion tictactoeTurnManager(board, symbol, coordinates) qui permet d'éditer un tableau de morpion avec un nouveau symbole
	#Initialiser un tableau 2D updatedBoard égal à board
	#Assigner à updatedBoard[coordintaes[0], coordinates[1]] le caractère symbol
	#Retourner updatedBoard

#Définir une fonction tictactoeEndChecker(board) qui permet de définir si une partie de morpion est terminé, et quel en est le résultat
	#Initialiser une variable xCoord à 0
	#Initialiser une variable yCoord à 0
	#Initialiser une variable gameStatus à None
	#Initialiser une liste winnerSymbol à [None, None]
	#Pour xCoord dans 2, Faire...
		#Si board[xCoord][0] est égal à board[xCoord][1] ET board[xCoord][1] est égal à board[xCoord][2], Alors...
			#Assigner à gameStatus le string "winned"
			#Assigner à winnerSymbol la liste [xCoord, 1]
			#Sortir de la boucle
	#Pour yCoord dans 2, Faire...
		#Si board[0][yCoord] est égal à board[1][yCoord] ET board[1][yCoord] est égal à board[2][yCoord], Alors...
			#Assigner à gameStatus le string "winned"
			#Assigner à winnerSymbol la liste [1, yCoord]
			#Sortir de la boucle
	#Si board[0][0] est égal à board[1][1] ET board[1][1] est égal à board[2][2], Alors...
		#Assigner à gameStatus le string "winned"
		#Assigner à winnerSymbol la liste[1, 1]
	#Si board[2][0] est égal à board[1][1] ET board[1][1] est égal à board[0][2], Alors...
		#Assigner à gameStatus le string "winned"
		#Assigner à winnerSymbol la liste[1, 1]
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
			#Afficher "le Joueur à gagné"
		#Si board[winnerSymbol[0]][winnerSymbol[1]] est égal à 'X', Alors...
			#Afficher "l'Ordinateur' à gagné"
		#Retourner True
	#Sinon Si gameStatus est égal à "blocked", Alors...
		#Afficher "!!! ÉGALITÉ !!!"
		#Retourner True
	#Sinon : la partie n'est ni bloquée ni gagnée, Alors...
		#Retourner False

#Définir une fonction tictactoePrintBoard(board) qui permet d'afficher correctement une partie de morpion
	#Afficher "╔═╦═╦═╗"
	#Afficher "║" + str(board[0][0]) + "║" + str(board[0][1]) + "║" + str(board[0][2]) + "║"
	#Afficher "╠═╬═╬═╣"
	#Afficher "║" + str(board[1][0]) + "║" + str(board[1][1]) + "║" + str(board[1][2]) + "║"
	#Afficher "╠═╬═╬═╣"
	#Afficher "║" + str(board[2][0]) + "║" + str(board[2][1]) + "║" + str(board[2][2]) + "║"
	#Afficher "╚═╩═╩═╝"

#Définir une fonction tictactoeBlinkBoard(board) qui permet d'afficher correctement une partie de morpion avec des traits plus fin
	#Initialiser un tableau 2D lighterBoard égal à board
	#Pour x dans 0 à 2, Faire...
		#Pour y dans 0 à 2, Faire...
			#Si lighterBoard[x][y] est égal à 'O', Alors...
				#Assigner à lighterBoard[x][y] le caractère '○'
			#Sinon Si lighterBoard[x][y] est égal à 'X', Alors...
				#Assigner à ligtherBoard[x][y] le caractère '×'
	#Afficher "┌─┬─┬─┐"
	#Afficher "│" + str(board[0][0]) + "│" + str(board[0][1]) + "│" + str(board[0][2]) + "│"
	#Afficher "├─┼─┼─┤"
	#Afficher "│" + str(board[1][0]) + "│" + str(board[1][1]) + "│" + str(board[1][2]) + "│"
	#Afficher "├─┼─┼─┤"
	#Afficher "│" + str(board[2][0]) + "│" + str(board[2][1]) + "│" + str(board[2][2]) + "│"
	#Afficher "└─┴─┴─┘"
			
#Définir une fonction tictactoeVsCpu() qui permet de jouer à une partie de morpion avec l'ordinateur
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	#Initialiser une variable gameOver à False
	#Initialiser une liste playerChoice à [-1, -1]
	#Initialiser une liste cpuChoice à [-1, -1]
	#Initialiser une variable isValidChoice à False
	#Tant que gameOver est à False, Alors...
		#Si turnOf est égal à 1, Alors...
			#Vider l'écran de la console
			#Afficher "C'est au tour du Joueur !"
			#Appeler la fonction tictactoePrintBoard(board)
			#Tant que isValidChoice est à False, Alors...
				#Tant que playerChoice[0] n'est pas compris entre 0 et 2, Alors...
					#Assigner à playerChoice[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
					#Si playerChoice[0] n'est pas compris entre 0 et 2, Alors...
						#Afficher un message d'erreur : la position n'est pas valide
				#Tant que playerChoice[1] n'est pas compris entre 0 et 2, Alors...
					#Assigner à playerChoice[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
					#Si playerChoice[1] n'est pas compris entre 0 et 2, Alors...
						#Afficher un message d'erreur : la position n'est pas valide
				#Si board[playerChoice[0]][playerChoice[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
				#Sinon : board[playerChoice[0]][playerChoice[1]] est différente de ' ', Alors...
					#Afficher un message d'erreur : la case est occupée
			#Assigner à board le retour de l'appel de la fonction tictactoeTurnManager(board, 'O', playerChoice)
			#Assigner à playerChoice la liste [-1, -1]
			#Assigner à turnOf la valeur 2
			#Assigner à isValidChoice la valeur False
		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour de l'Ordinateur !"
			#Tant que isValidChoice est à False, Alors...
				#Tant que cpuChoice[0] n'est pas compris entre 0 et 2, Alors...
					#Assigner à cpuChoice[0] le retour de l'appel de la fonction randint(0, 2)
				#Tant que cpuChoice[0] n'est pas compris entre 0 et 2, Alors...
					#Assigner à cpuChoice[1] le retour de l'appel de la fonction randint(0, 2)
				#Si board[cpuChoice[0]][cpuChoice[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
			#Assigner à board le retour de l'appel de la fonction tictactoeTurnManager(board, 'X', cpuChoice)
			#Assigner à playerChoice la liste [-1, -1]
			#Assigner à turnOf la valeur 1
			#Assigner à isValidChoice la valeur False
		#Assigner à gameOver le retour de l'appel de la fonction tictactoeEndChecker(board)
	#Afficher un message de retour au menu

#Définir une fonction tictactoeVsIA qui permet de jouer à une partie de morpion contre une IA imbattable

#Définir une fonction tictactoaVsPlayer qui permet de jouer à une partie de morpion contre un autre joueur
	#Initialiser un tableau 2D board de format 3 par 3 avec uniquement des cases comportant ' '
	#Initialiser une variable turnOf avec le retour de randint(1, 2)
	#Initialiser une variable gameOver à False
	#Initialiser une liste playerChoice1 à [-1, -1]
	#Initialiser une liste playerChoice2 à [-1, -1]
	#Initialiser une variable isValidChoice à False
	#Tant que gameOver est à False, Alors...
		#Si turnOf est égal à 1, Alors...
			#Vider l'écran de la console
			#Afficher "C'est au tour du Joueur 1 !"
			#Appeler la fonction tictactoePrintBoard(board)
			#Tant que isValidChoice est à False, Alors...
				#Tant que playerChoice1[0] n'est pas compris entre 0 et 2, Alors...
					#Assigner à playerChoice1[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
					#Si playerChoice1[0] n'est pas compris entre 0 et 2, Alors...
						#Afficher un message d'erreur : la position n'est pas valide
				#Tant que playerChoice1[1] n'est pas compris entre 0 et 2, Alors...
					#Assigner à playerChoice1[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
					#Si playerChoice1[1] n'est pas compris entre 0 et 2, Alors...
						#Afficher un message d'erreur : la position n'est pas valide
				#Si board[playerChoice1[0]][playerChoice1[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
				#Sinon : board[playerChoice1[0]][playerChoice1[1]] est différente de ' ', Alors...
					#Afficher un message d'erreur : la case est occupée
			#Assigner à board le retour de l'appel de la fonction tictactoeTurnManager(board, 'O', playerChoice1)
			#Assigner à playerChoice1 la liste [-1, -1]
			#Assigner à turnOf la valeur 2
			#Assigner à isValidChoice la valeur False
		#Sinon : turnOf est égal à 2, Alors...
			#Afficher "C'est au tour de l'Ordinateur !"
			#Tant que isValidChoice est à False, Alors...
				#Tant que playerChoice2[0] n'est pas compris entre 0 et 2, Alors...
					#Assigner à playerChoice2[0] le retour de l'appel de la fonction input("Quel ligne visez-vous ? ")
					#Si playerChoice2[0] n'est pas compris entre 0 et 2, Alors...
						#Afficher un message d'erreur : la position n'est pas valide
				#Tant que playerChoice2[1] n'est pas compris entre 0 et 2, Alors...
					#Assigner à playerChoice2[1] le retour de l'appel de la fonction input("Quel colonne visez-vous ? ")
					#Si playerChoice2[1] n'est pas compris entre 0 et 2, Alors...
						#Afficher un message d'erreur : la position n'est pas valide
				#Si board[playerChoice2[0]][playerChoice2[1]] est égal à ' ', Alors...
					#Assigner à isValidChoice la valeur True
				#Sinon : board[playerChoice2[0]][playerChoice2[1]] est différente de ' ', Alors...
					#Afficher un message d'erreur : la case est occupée
			#Assigner à board le retour de l'appel de la fonction tictactoeTurnManager(board, 'X', playerChoice2)
			#Assigner à playerChoice2 la liste [-1, -1]
			#Assigner à turnOf la valeur 1
			#Assigner à isValidChoice la valeur False
		#Assigner à gameOver le retour de l'appel de la fonction tictactoeEndChecker(board)
	#Afficher un message de retour au menu


#Définir une fonction tictactoe() qui permet de lancer une partie de morpion
	#Initialiser une variable gameClose à False
	#Initialiser une variable menuNav à None

	#Vider l'écran de la console

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
			#Appeler la fonction tictactoeVsCpu
			#Vider l'écran de la console
		#Sinon Si menuNav est égal à 2, Alors...
			#Appeler la fonction tictactoeVsIA
			#Vider l'écran de la console
		#Sinon Si menuNav est égal à 3, Alors...
			#Appeler la fonction tictactoeVsPlayer
			#Vider l'écran de la console
		#Sinon, Alors...
			#Afficher un message d'erreur
			#Vider l'écran de la console
	#Afficher un message de fermeture

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

Check toutes les lignes de victoires
Si XXportunity, alors finish
Sinon Si OOportunity, alors block
Sinon : 

Si empty
╔═╦═╦═╗
║ ║ ║ ║
╠═╬═╬═╣
║ ║ ║ ║
╠═╬═╬═╣
║ ║ ║ ║
╚═╩═╩═╝
	Alors center
	╔═╦═╦═╗
	║ ║ ║ ║
	╠═╬═╬═╣
	║ ║X║ ║
	╠═╬═╬═╣
	║ ║ ║ ║
	╚═╩═╩═╝
	Si N-cross
	╔═╦═╦═╗
	║ ║•║ ║
	╠═╬═╬═╣
	║•║X║O║
	╠═╬═╬═╣
	║ ║•║ ║
	╚═╩═╩═╝
		Alors same line
		╔═╦═╦═╗
		║ ║ ║X║
		╠═╬═╬═╣
		║ ║X║O║
		╠═╬═╬═╣
		║ ║ ║×║
		╚═╩═╩═╝
		Si block
		╔═╦═╦═╗
		║ ║ ║X║
		╠═╬═╬═╣
		║ ║X║O║
		╠═╬═╬═╣
		║O║ ║ ║
		╚═╩═╩═╝
			Alors corner no-neighbours
			╔═╦═╦═╗
			║X║ ║X║
			╠═╬═╬═╣
			║ ║X║O║
			╠═╬═╬═╣
			║O║ ║ ║
			╚═╩═╩═╝ ==> WIN
		Sinon ==> WIN
	Sinon
	╔═╦═╦═╗
	║•║ ║O║
	╠═╬═╬═╣
	║ ║X║ ║
	╠═╬═╬═╣
	║•║ ║•║
	╚═╩═╩═╝
		Alors random
Sinon Si
╔═╦═╦═╗
║ ║ ║ ║
╠═╬═╬═╣
║ ║O║ ║
╠═╬═╬═╣
║ ║ ║ ║
╚═╩═╩═╝
	Alors random-corner
	╔═╦═╦═╗
	║×║ ║X║
	╠═╬═╬═╣
	║ ║O║ ║
	╠═╬═╬═╣
	║×║ ║×║
	╚═╩═╩═╝
Sinon
╔═╦═╦═╗
║ ║O║ ║
╠═╬═╬═╣
║•║ ║•║
╠═╬═╬═╣
║ ║•║ ║
╚═╩═╩═╝
	Alors
	╔═╦═╦═╗
	║ ║O║ ║
	╠═╬═╬═╣
	║ ║ ║ ║
	╠═╬═╬═╣
	║ ║ ║ ║
	╚═╩═╩═╝
-----------------------
Si centre dispo, alors grab
Si centre à 'X' + 1 seul 'O' + en D-cross, alors Gagner
Si centre occupé + 1 seul 'O' + aucun 'X', alors prendre un coin au pif
Sinon au pif

Après avoir jouer, lister les XXportunity