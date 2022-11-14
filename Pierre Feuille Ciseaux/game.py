#DEBUT

#On admet la fonction input() qui renvoit la valeur donner par le player
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe

#Définir une fonction pierreFeuilleCiseaux qui permet au joueur de faire son choix
    #Écrire les règles du jeu
    #Créer un tableau game = ["pierre","feuille","ciseaux"]
    #Initialiser une variable cpuChoice à None
    #Initialiser une variable playerChoice à None
    #Initialiser une variable scorePlayer à 0
    #Initialiser une variable scoreCpu à 0
    #---------------------------------------Initialiser une variable playAgain à 'y'
        #Tant que scorePlayer < 2 ou scoreCpu < 2
            #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction random()
            #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Que faites-vous ce tour ? ")
            #Si playerChoice est égale à cpuChoice
                #Alors écrire "Egalité!"
            #Sinon si playerChoice égale à 0
                #Si cpuChoice égale à 2
                    #Alors écrire "Vous avez gagné!"
                    #Incrémenter scorePlayer de 1
                #Sinon 
                    #Alors, écrire "Vous avez Perdu!"
                    #Incrémenter scoreCpu de 1
            #Sinon si playerChoice égale à 1
                #Si cpuChoice égale à 0
                    #Alors écrire "Vous avez gagné!"
                    #Incrémenter scorePlayer de 1
                #Sinon 
                    #Alors, écrire "Vous avez Perdu!"
                    #Incrémenter scoreCpu à 1
            #Sinon si playerChoice égale à 2
                #Si cpuChoice égale de 1
                    #Alors écrire "Vous avez gagné!"
                    #Incrémenter scorePlayer de 1
                #Sinon
                    #Alors écrire "Vous avez Perdu!"
                    #Incrémenter scoreCpu de 1
            #Sinon : playerChoice ne renvoi à aucun élément du tableau game
                #Alors écrire "Choix impossible!"
            #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
        #Retourner

            #------------------------BONUS PEUT-ÊTRE FINI (à valider)------------------------
            #Tant que playAgain est différent 'y' ou 'n'
                #Assigner la résultante de l'appel d'input("Voulez vous rejouer (y/n) ? ") à la variable playAgain
                #Si playAgain différent de 'y' ou 'n'
                    #Alors afficher un message d'erreur

#FIN