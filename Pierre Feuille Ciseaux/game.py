# #DEBUT


#--------------LIBRARY--------------#

#On admet la fonction input() qui renvoit la valeur donner par le player
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe
from random import randint
#On admet la fonction os() qui permet d'éxecuter des commandes dans la console
import os
#Préparation pour vider le contenu de la console
clear = lambda: os.system('cls')




#--------------------------------------SHIFIMI TURN----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Définir une fonction shifumiTurn(movePlayer1, movePlayer2) qui renvoi le vainqueur du tour (j1 ou j2) à partir de leur choix respectif. Un retour à 0 signinfie pas de vainqueur
def shifumiTurn(movePlayer1, movePlayer2):
    #Si movePlayer1 est égale à movePlayer2, Alors...


    print("~~~ movePlayer1 = " + str(movePlayer1))
    print("~~~ movePlayer2 = " + str(movePlayer2))
    print("~~~ movePlayer1 érroné ? : " + str(movePlayer1 < 1 or movePlayer1 > 3))
    print("~~~ movePlayer2 érroné ? : " + str(movePlayer2 < 1 or movePlayer2 > 3))
    print("~~~ movePlayer1 ou movePlayer2 érroné ? : " + str((movePlayer1 < 1 or movePlayer1 > 3) or movePlayer2 < 1 or movePlayer2 > 3))


    if movePlayer1 == movePlayer2:
        #Retourner 0
        return 0
    #Sinon si movePlayer1 égale à 1, Alors...
    elif movePlayer1 == 1:
        #Si movePlayer2 égale à 3, Alors...
        if movePlayer2 == 3:
            #Retourner 1
            return 1
        #Sinon, Alors...
        else:
            #Retourner 2
            return 2
    #Sinon si movePlayer1 égale à 2, Alors...
    elif movePlayer1 == 2:
        #Si movePlayer2 égale à 1, Alors...
        if movePlayer2 == 1:
            #Retourner 1
            return 1
        #Sinon
        else:
            #Retourner 2
            return 2
    #Sinon si movePlayer1 égale à 3, Alors...
    elif movePlayer1 == 3:
        #Si movePlayer2 égale de 2, Alors...
        if movePlayer2 == 2:
            #Retourner 1
            return 1
        #Sinon, Alors...
        else:
            #Retourner 2
            return 2
    #Sinon Si aucun des 2 movePlayer n'est valide (entre 1 et 3), Alors...
    elif (movePlayer1 < 1 or movePlayer1 > 3) and (movePlayer2 < 1 or movePlayer2 > 3):
        #Retourner -1
        return -1




#------------------------------------------INFINITE----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Définir la fonction infiniteGameMode qui permet de jouer au shifumi contre l'ordinateur à l'infinie
def infiniteGameMode():
    #Initialiser une variable infiniteContinue à 1
    infiniteContinue = 1
    #Initialiser une variable cpuChoice à None
    cpuChoice = None
    #Initialiser une variable playerChoice à None
    playerChoice = None
    #Initialiser une variable cpuScore à 0
    cpuScore = 0
    #Initialiser une variable playerScore à 0
    playerScore = 0
    #Initialiser une varialbe turnResult à None
    turnResult = None
    #Tant que infiniteContinue est égale à 1
    while infiniteContinue:
        #Assigner à cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [1 , 3]
        cpuChoice = randint(1, 3)
        #Assigner à playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Que faites-vous ce tour ? ")
        playerChoice = int(input("\n1 pour pierre, 2 pour feuille ou 3 pour ciseaux "))
        #Assigner à turnResult le retour de l'appel de shifumiTurn(playerChoice, cpuChoice)
        turnResult = shifumiTurn(playerChoice, cpuChoice)
        #Si turnResult est égal à 0, Alors...
        if turnResult == 0:
            #Afficher "Score inchangé..."
            print("Égalité !")
            print("Score Inchangé...")
        #Sinon Si turnResult est égal à 1, Alors...
        elif turnResult == 1:
            #Incrémenter playerScore de 1
            playerScore = playerScore + 1
            #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
            print("---=<( Vous - Ordi )>=---")
            print("        " + str(playerScore) + " -  " + str(cpuScore))
            print("---=<( SCORE  ACTU )>=---")
        #Sinon Si turnResult est égal à 2, Alors...
        elif turnResult == 2:
            #Incrémenter cpuScore de 1
            cpuScore = cpuScore + 1
            #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
            print("---=<( Vous - Ordi )>=---")
            print("        " + str(playerScore) + " -  " + str(cpuScore))
            print("---=<( SCORE  ACTU )>=---")
        #Sinon : le retour de la fonction shifumiTurn est différente de 0, 1 ou 2, Alors...
        else:
            #Afficher une erreur de saisie
            print("\n!!! CHOIX INVALIDE !!!")
        #Définir la variable infiniteContinue avec comme le retour de l'éxecution de la fonction input("Voulez-vous continuez (1 pour oui, 0 pour non)")
        infiniteContinue = int(input("\nVoulez-vous continuez (1 pour oui, 0 pour non) "))
        #Si infiniteContinue > 0, Alors...
        if infiniteContinue > 0:
            #Assigner à infiniteContinue la valeur 1
            infiniteContinue = 1
        #Sinon : infiniteContinue est égal ou inférieur à 0, Alors...
        else:
            #Assigner à infiniteContinue la valeur 0
            infiniteContinue = 0
    #Afficher le retour au menu principale
    print("\nretour au menu")
    print("retour au menu.")
    print("retour au menu..")
    print("retour au menu...\n")
    #Éxecuter la fonction shifumiMenu
    shifumiMenu()




#------------------------------------------PLAYER VS CPU----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Définir la fonction playerVersusCpuGameMode qui permet de jouer au shifumi contre l'ordinateur en fonction de set ou et de points
def playerVersusCpuGameMode():
    #Initialiser la variable scorePlayer à 0
    playerScore = 0
    #Initialiser la variable scoreCpu à 0
    cpuScore = 0
    #Initialiser la variable setPlayer à 0
    setPlayer = 0
    #Initialiser la variable setCpu à 0
    setCpu = 0
    #Initialiser la variable playerChoice à None
    playerChoice = None
    #Initialiser la variable cpuChoice à None
    cpuChoice = None
    #Initialiser une varialbe turnResult à None
    turnResult = None
    #Tant que setPlayer < 2 et setCpu < 2, Alors...
    while setPlayer < 2 and setCpu < 2:
        #Assigner à cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [1 , 3]
        cpuChoice = randint(1, 3)
        #Assigner à playerChoice avec comme valeur le retour de l'éxecution de la fonction input("1 pour pierre, 2 pour feuille ou 3 pour ciseaux: ")
        playerChoice = int(input("\n1 pour pierre, 2 pour feuille ou 3 pour ciseaux "))
        #Assigner à turnResult le retour de l'appel de shifumiTurn(playerChoice, cpuChoice)
        turnResult = shifumiTurn(playerChoice, cpuChoice)
        #Si turnResult est égal à 0, Alors...
        if turnResult == 0:
            #Afficher "Score inchangé..."
            print("Égalité !")
            print("Score Inchangé...")
        #Sinon Si turnResult est égal à 1, Alors...
        elif turnResult == 1:
            #Incrémenter playerScore de 1
            playerScore = playerScore + 1
            #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
            print("---=<( Vous - Ordi )>=---")
            print("        " + str(playerScore) + " -  " + str(cpuScore))
            print("---=<( SCORE  ACTU )>=---")
        #Sinon Si turnResult est égal à 2, Alors...
        elif turnResult == 2:
            #Incrémenter cpuScore de 1
            cpuScore = cpuScore + 1
            #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
            print("---=<( Vous - Ordi )>=---")
            print("        " + str(playerScore) + " -  " + str(cpuScore))
            print("---=<( SCORE  ACTU )>=---")
        #Sinon : le retour de la fonction shifumiTurn est différente de 0, 1 ou 2, Alors...
        else:
            #Afficher une erreur de saisie
            print("\n!!! CHOIX INVALIDE !!!")
        #Si playerScore est égal à 5, Alors...
        if playerScore == 5:
            #Assigner à playerScore la valeur 0
            playerScore = 0
            #Assigner à cpuScore la valeur 0
            cpuScore = 0
            #Incrémenter setPlayer de 1
            setPlayer = setPlayer + 1
            #Afficher les set actuels
            print("\n!!! LA PARTIE REBOOT !!!")
            print("Set du joueur - Set de l'ordinateur")
            print(str(setPlayer) + " - " + str(setCpu))
        #Si cpuScore est égal à 5, Alors...
        if cpuScore == 5:
            #Vider le contenu de la console
            clear()
            #Assigner à playerScore la valeur 0
            playerScore = 0
            #Assigner à cpuScore la valeur 0
            cpuScore = 0
            #Incrémenter setCpu de 1
            setCpu = setCpu + 1
            #Afficher les set actuels
            print("\n!!! LA PARTIE REBOOT !!!")
            print("Set du joueur - Set de l'ordinateur")
            print(str(setPlayer) + " - " + str(setCpu))
    #Afficher le retour au menu principale
    print("\nretour au menu")
    print("retour au menu.")
    print("retour au menu..")
    print("retour au menu...\n")
    #Éxecuter la fonction shifumiMenu
    shifumiMenu()




#------------------------------------------PLAYER VS PLAYER----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Définir la fonction playerVersusPlayerGameMode qui permet de jouer au shifumi contre l'ordinateur en fonction de set ou et de points
def playerVersusPlayerGameMode():
    #Initialiser la variable scorePlayer1 à 0
    playerScore1 = 0
    #Initialiser la variable scorePlayer2 à 0
    playerScore2 = 0
    #Initialiser la variable setPlayer1 à 0
    setPlayer1 = 0
    #Initialiser la variable setPlayer2 à 0
    setPlayer2 = 0
    #Initialiser la variable playerChoice1 à None
    playerChoice1 = None
    #Initialiser la variable playerChoice2 à None
    playerChoice2 = None
    #Initialiser une varialbe turnResult à None
    turnResult = None
    #Tant que setPlayer1 < 2 et setPlayer2 < 2, Alors...
    while setPlayer1 < 2 and setPlayer2 < 2:
        #Assigner à playerChoice1 la valeur le retour de l'éxecution de la fonction input("1 pour pierre, 2 pour feuille ou 3 pour ciseaux: ")
        playerChoice1 = int(input("\n1 pour pierre, 2 pour feuille ou 3 pour ciseaux: "))
        #Vider le contenu de la console
        clear()
        #Assigner à playerChoice2 la valeur le retour de l'éxecution de la fonction input("1 pour pierre, 2 pour feuille ou 3 pour ciseaux: ")
        playerChoice2 = int(input("1 pour pierre, 2 pour feuille ou 3 pour ciseaux: "))
        #Assigner à turnResult le retour de l'appel de shifumiTurn(playerChoice1, playerChoice2)
        turnResult = shifumiTurn(playerChoice1, playerChoice2)
        #Si turnResult est égal à 0, Alors...
        if turnResult == 0:
            #Afficher "Score inchangé..."
            print("Égalité !")
            print("Score Inchangé...")
        #Sinon Si turnResult est égal à 1, Alors...
        elif turnResult == 1:
            #Incrémenter playerScore1 de 1
            playerScore1 = playerScore1 + 1
            #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
            print("---=<( Vous - Ordi )>=---")
            print("        " + str(playerScore1) + " -  " + str(playerScore2))
            print("---=<( SCORE  ACTU )>=---")
        #Sinon Si turnResult est égal à 2, Alors...
        elif turnResult == 2:
            #Incrémenter playerScore2 de 1
            playerScore2 = playerScore2 + 1
            #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
            print("---=<( Vous - Ordi )>=---")
            print("        " + str(playerScore1) + " -  " + str(playerScore2))
            print("---=<( SCORE  ACTU )>=---")
        #Sinon : le retour de la fonction shifumiTurn est différente de 0, 1 ou 2, Alors...
        else:
            #Afficher une erreur de saisie
            print("\n!!! CHOIX INVALIDE !!!")
        #Si playerScore1 est égal à 5, Alors...
        if playerScore1 == 5:
            #Assigner à playerScore1 la valeur 0
            playerScore1 = 0
            #Assigner à playerScore2 la valeur 0
            playerScore2 = 0
            #Incrémenter setPlayer1 de 1
            setPlayer1 = setPlayer1 + 1
            #Afficher les set actuels
            print("\n!!! LA PARTIE REBOOT !!!")
            print("Set du joueur 1 - Set du joueur 2")
            print(str(setPlayer1) + " - " + str(setPlayer2))
        #Si playerScore2 est égal à 5, Alors...
        if playerScore2 == 5:
            #Vider le contenu de la console
            clear()
            #Assigner à playerScore1 la valeur 0
            playerScore1 = 0
            #Assigner à playerScore2 la valeur 0
            playerScore2 = 0
            #Incrémenter setPlayer2 de 1
            setPlayer2 = setPlayer2 + 1
            #Afficher les set actuels
            print("\n!!! LA PARTIE REBOOT !!!")
            print("Set du joueur - Set de l'ordinateur")
            print(str(setPlayer1) + " - " + str(setPlayer2))
    #Afficher le retour au menu principale
    print("\nretour au menu")
    print("retour au menu.")
    print("retour au menu..")
    print("retour au menu...\n")
    #Éxecuter la fonction shifumiMenu
    shifumiMenu()




#------------------------------------------SPOKE----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Définir la fonction spokeGameMode qui permet de jouer au shifumi avec les règles avancés
def spokeGameMode():
    #Vider le contenu de la console
    clear()
    #Afficher un message de bienvenue
    print("Vous êtes arrivé dans le mode de jeu cacher, ici il y a 2 choix suplémentaire. Bonne chance !")
    #Initialiser une variable cpuChoice à None
    cpuChoice = None
    #Initialiser une variable playerChoice à None
    playerChoice = None
    #Initialiser une variable cpuScore à 0
    cpuScore = 0
    #Initialiser une variable playerScore à 0
    playerScore = 0
    #Tant que infiniteContinue est égale à 1
    while playerScore < 5 and cpuScore < 5:
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [1 , 5]
        cpuChoice = randint(1, 5)
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction float(input("1 pour pierre, 2 pour feuille, 3 pour ciseaux, 4 pour lézard ou 5 pour spoke: "))
        print(" ")
        playerChoice = float(input("1 pour pierre, 2 pour feuille, 3 pour ciseaux, 4 pour lézard ou 5 pour spoke: "))
        #Si playerChoice est égale à cpuChoice
        if playerChoice == cpuChoice:
            #Afficher "Score inchangé..."
            print("Égalité !")
            print("Score Inchangé...")
        #Sinon si playerChoice égale à 1
        elif playerChoice == 1:
            #Si cpuChoice égale à 3 ou à 4
            if cpuChoice == 3 or cpuChoice == 4:
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
            #Sinon
            else:
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
        #Sinon si playerChoice égale à 2
        elif playerChoice == 2:
            #Si cpuChoice égale à 1 ou à 5
            if cpuChoice == 1 or cpuChoice == 5:
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
            #Sinon
            else:
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
        #Sinon si playerChoice égale à 3
        elif playerChoice == 3:
            #Si cpuChoice égale de 2 ou à 4
            if cpuChoice == 2 or cpuChoice == 4:
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
            #Sinon
            else:
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
        #Sinon si playerChoice égale à 4
        elif playerChoice == 4:
            #Si cpuChoice égale de 2 ou à 5
            if cpuChoice == 2 or cpuChoice == 5:
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
            #Sinon
            else:
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
        #Sinon si playerChoice égale à 5
        elif playerChoice == 5:
            #Si cpuChoice égale de 1 ou à 3
            if cpuChoice == 1 or cpuChoice == 3:
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
            #Sinon
            else:
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
                #Afficher les set actuels
                print("---=<( Vous - Ordi )>=---")
                print("        " + str(playerScore) + " -  " + str(cpuScore))
                print("---=<( SCORE  ACTU )>=---")
        #Sinon : playerChoice ne renvoi à aucun élément du tableau game
        else:
            #Afficher une erreur de saisie
            print("\n!!! CHOIX INVALIDE !!!")
    #Afficher les scores de la partie à partir de playerScore et cpuScore 
    print("---=<( Vous - Ordi )>=---")
    print("        " + str(playerScore) + " -  " + str(cpuScore))
    print("---=<( SCORE  FINAL )>=---")
    #Afficher le retour au menu principale
    print("\nretour au menu")
    print("retour au menu.")
    print("retour au menu..")
    print("retour au menu...\n")
    #Éxecuter la fonction shifumiMenu
    shifumiMenu()




#------------------------------------------MENU----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Définir une fonction shifumiMenu qui permet d'appeler les fonctions de jeux selon les préférences du ou des joueurs
def shifumiMenu():
    #Initialiser une variable gameMode à None
    gameMode = None
    #Appeler print("--------- MENU SHIFUMI ----")
    print("--------- MENU SHIFUMI ----")
    #Appeler print("0 - Quitter")
    print("0 - Quitter")
    #Appeler print("1 - Mode Infini")
    print("1 - Mode Infini")
    #Appeler print("2 - Mode Joueur vs Ordi")
    print("2 - Mode Joueur vs Ordi")
    #Appeler print("3 - Mode Joueur vs Joueur")
    print("3 - Mode Joueur vs Joueur")
    #Appeler print("---------------------------")
    print("---------------------------")
    #Définir la variable gameMode avec comme valeur le retour de l'éxecution de la fonction float(input("Mode de jeu : "))
    gameMode = float(input("Mode de jeu : "))


    #Si le gameMode est égale à 1
    if gameMode == 1:
        #Executer la fonction infiniteGameMode
        infiniteGameMode()
    #Sinon si le gameMode est égale à 2
    elif gameMode == 2:
        #Executer la fonction playerVersusCpuGameMode
        playerVersusCpuGameMode()
    #Sinon si le gameMode est égale à 3
    elif gameMode == 3:
        #Executer la fonction playerVersusPlayerGameMode
        playerVersusPlayerGameMode()
    #Sinon si le gameMode est égale à 0
    elif gameMode == 0:
        #Afficher "arret du jeu"
        print(" ")
        print("arrêt du jeu")
        print("arrêt du jeu.")
        print("arrêt du jeu..")
        print("arrêt du jeu...")
        #retourner
        return
    #Sinon si le gameMode est égale à 3.14
    elif gameMode == 3.14:
        #Executer la fonction spokeGameMode
        spokeGameMode()

#Executer la fonction shifumiMenu
shifumiMenu()

#FIN