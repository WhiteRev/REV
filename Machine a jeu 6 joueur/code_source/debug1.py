import random
import time
import webbrowser
import urllib 

#Affichage
def  FT_Affichage_StandBY():
    print("Lance video")

def  FT_Affichage_Jeu():
    print("Lance Affichage de la salle de jeu")

def  FT_Affichage_Bonus():
    print("Lance affichage BONUS") 

def  FT_Affichage_Tilt():
    print("Lance affichage Tilt") 


#TOOL Rasberry
def  Ft_Fermeture_trappe():
    print("Fermeture Trappe")
def Ft_Ouverture_Trappe():
    print("Ouverture Trappe")

def FT_capteur_jetons():
    print("tu captes")

def FT_Distributeur_Points():
    print("Tiens bro un point")

def FT_Distributeur_Jetons(gain):
    tour=0
    while tour < gain:
        print("Glin")
        tour+=1
     
#TOOL


def Ft_Detection(capte_jetons):
    FT_capteur_jetons()
    capte_jetons=int(input("Insere un jetons\n"))
    capte_jetons=int(capte_jetons)
    return capte_jetons



def Ft_Sleep_Timer(timer):
    time.sleep(0.3)
    timer+=1
    if timer==6000:
        timer="sleep"    
        print("Sleep too much and i Stand by ")
    return timer


def FT_Trappe(mode_jeu):

    if mode_jeu==1 or mode_jeu==4:
        Ft_Fermeture_trappe()
    if mode==2:
        Ft_Ouverture_Trappe()

def FT_Affichage(mode_jeu):

    if mode_jeu==1:
        print("Je suis jolie ! Viens jouer avec moi")
        FT_Affichage_StandBY()
    if mode_jeu==2:
        print("C'est bien joue ")
        FT_Affichage_Jeu()
    if mode_jeu==3:
        print("Je fais de toi un heureux gagnant")
        FT_Affichage_Bonus()
    if mode_jeu==4:
        print("T'es vraiment une pute!")
        FT_Affichage_Tilt()

def FT_Led_carousel(mode_jeu):

    if mode_jeu==1:
        print("Je suis jolie ! Viens jouer avec moi")
    if mode_jeu==2:
        print("C'est bien joue ")
    if mode_jeu==3:
        print("Je fais de toi un heureux gagnant")
    if mode==4:
        print("T'es vraiment une pute!")

def Ft_Son(mode_jeu):

    if mode_jeu==0:
        print("Bim bim ")
    if mode_jeu==3:
        print("Trin trin trin trin")
    if mode_jeu==4:
        print("ahahahahha Vous etes un connard!")

def FT_Tilt(mode_jeu):
    #Check tilt
    Tilt=0
    if Tilt==1:
        mode_jeu =4
    return mode_jeu


#Write txt > SQL
def Ft_New_Player(mode_player):
    prochaincode="0"
    with open ("Banque/nombre_joueur.txt","a")as nombre_joueur:
        nombre_joueur.write("")
    with open ("Banque/nombre_joueur.txt","r")as nombre_joueur:
        for i in nombre_joueur:
            mode_player=i.rstrip('\n')
            print("Vous etes le joueur {}".format(mode_player))
            mode_player=int(mode_player)
            prochaincode=mode_player+1
            prochaincode=str(prochaincode)
    with open ("Banque/nombre_joueur.txt","w")as nombre_joueur:
        nombre_joueur.write(prochaincode)
    return mode_player
    


def FT_Base_StandBy():
    print("Int game")
    with open ("Banque/nb_bonus1.txt","w")as nb_bonus1_txt:
        nb_bonus1_txt.write("0")

        with open ("Banque/nb_bonus2.txt","w")as nb_bonus2_txt:
            nb_bonus2_txt.write("0")

            with open ("Banque/nb_bonus3.txt","w")as nb_bonus3_txt:
                nb_bonus3_txt.write("0")
                with open ("Banque/nombre_joueur.txt","w")as nombre_joueur:
                    nombre_joueur.write("1")
                    with open ("Banque/active_bonus.txt","w")as active_bonus:
                        active_bonus.write("0")

def FT_Set_Niveau_Bonus(liste_niveau_jetons):
#Bonus 1 curseur
    with open ("Banque/nb_bonus1.txt","r")as nb_bonus1_txt:
        for i in nb_bonus1_txt:
            niveau_jetons1=i.rstrip('\n')
            niveau_jetons1=int(niveau_jetons1)
            niveau_jetons1=niveau_jetons1+1
            niveau_jetons1=str(niveau_jetons1)
    with open ("Banque/nb_bonus1.txt","w")as nb_bonus1_txt:
        nb_bonus1_txt.write(niveau_jetons1)
        niveau_jetons1=int(niveau_jetons1)
#Bonus 2 curseur
    with open ("Banque/nb_bonus2.txt","r")as nb_bonus2_txt:
        for i in nb_bonus2_txt:
            niveau_jetons2=i.rstrip('\n')
            niveau_jetons2=int(niveau_jetons2)
            niveau_jetons2=niveau_jetons2+1
            niveau_jetons2=str(niveau_jetons2)
    with open ("Banque/nb_bonus2.txt","w")as nb_bonus2_txt:
        nb_bonus2_txt.write(niveau_jetons2)
        niveau_jetons2=int(niveau_jetons2)
#Bonus 3 curseur
    with open ("Banque/nb_bonus3.txt","r")as nb_bonus3_txt:
        for i in nb_bonus3_txt:
            niveau_jetons3=i.rstrip('\n')
            niveau_jetons3=int(niveau_jetons3)
            niveau_jetons3=niveau_jetons3+1
            niveau_jetons3=str(niveau_jetons3)
    with open ("Banque/nb_bonus3.txt","w")as nb_bonus3_txt:
        nb_bonus3_txt.write(niveau_jetons3)
        niveau_jetons3=int(niveau_jetons3)
    liste_niveau_jetons.append(niveau_jetons1)
    liste_niveau_jetons.append(niveau_jetons2)
    liste_niveau_jetons.append(niveau_jetons3)
    return liste_niveau_jetons

def Ft_Active_Bonus(active_bonus):
    with open ("Banque/active_bonus.txt","w")as active_bonus_txt:
        active_bonus_txt.write("{}\n".format(active_bonus))

def Ft_Need_Jetons_Bonus(liste_jetons_bonus):
#Int game
    #Je veux connnaitre le nombre de jetons requis pour gagner chaque bonus
    #Ici le Bonus 1
    tour=0
    with open ("Banque/bonus_1.txt","r")as bonus_1_txt:
      for i in bonus_1_txt:
            if tour==0:
                jetons_bonus1=i.rstrip('\n')
                jetons_bonus1=int(jetons_bonus1)
            else:
                if "POINTS" in i:
                    jetons_bonus_gain1=1
                else:
                    jetons_bonus_gain1=i.rstrip('\n')
                    jetons_bonus_gain1=int(jetons_bonus_gain1)
            tour+=1
    tour=0
    #Ici le Bonus 2
    with open ("Banque/bonus_2.txt","r")as bonus_2_txt:
      for i in bonus_2_txt:
            if tour==0:
                jetons_bonus2=i.rstrip('\n')
                jetons_bonus2=int(jetons_bonus2)
            else:
                if "POINTS" in i:
                    jetons_bonus_gain2=1
                else:
                    jetons_bonus_gain2=i.rstrip('\n')
                    jetons_bonus_gain2=int(jetons_bonus_gain1)
            tour+=1
    tour=0  
    #Ici le Bonus 3    
    with open ("Banque/bonus_3.txt","r")as bonus_3_txt:
      for i in bonus_3_txt:
        if tour==0:
            jetons_bonus3=i.rstrip('\n')
            jetons_bonus3=int(jetons_bonus3)
        else:
            if "POINTS" in i:
                jetons_bonus_gain3=1
            else:
                jetons_bonus_gain3=i.rstrip('\n')
                jetons_bonus_gain3=int(jetons_bonus_gain1)
        tour+=1
    tour=0
    print(jetons_bonus1,jetons_bonus2,jetons_bonus3)
    liste_jetons_bonus.append(jetons_bonus1)
    liste_jetons_bonus.append(jetons_bonus2)
    liste_jetons_bonus.append(jetons_bonus3)
    liste_jetons_bonus.append(jetons_bonus_gain1)
    liste_jetons_bonus.append(jetons_bonus_gain2)
    liste_jetons_bonus.append(jetons_bonus_gain3)
    return liste_jetons_bonus














#Mode 3 Bonus

def FT_Bonus(mode_jeu,mode_player):
    print("Bonus")
    active_bonus=1
    print("\nBONUS\n")
    liste_jetons_bonus=[]
    with open ("Banque/active_bonus.txt","w")as active_bonus_txt:
        active_bonus_txt.write("{}\n".format(active_bonus))
        active_bonus=0
    liste_jetons_bonus=Ft_Need_Jetons_Bonus(liste_jetons_bonus)
    gain=liste_jetons_bonus[mode_jeu]
    if gain>1:
        print("Gagne {} Jetons".format(gain))
        FT_Distributeur_Jetons(gain)
    else:
        FT_Distributeur_Points()
        print("Gagne 1 points")
    active_bonus=0
    with open ("Banque/active_bonus.txt","w")as active_bonus_txt:
        active_bonus_txt.write("{}\n".format(active_bonus))




    mode_jeu=2
    return mode_jeu + mode_player

#Mode 2 Play
def FT_Play(mode_jeu,mode_player,timer):
    print("PLAY {}".format(mode_player))
    active_bonus=0
    capte_jetons=0
    liste_niveau_jetons=[]
    liste_jetons_bonus=[]
    capte_jetons=Ft_Detection(capte_jetons)
    if capte_jetons==1:
        #Relance timer =0
        timer=0
        #Recup les stats jetons_bonus !
        print("detecte niveau jetons")
        liste_jetons_bonus=Ft_Need_Jetons_Bonus(liste_jetons_bonus)
        print(liste_jetons_bonus)
        #Remet a niveau l'affichage bonus
        liste_niveau_jetons=FT_Set_Niveau_Bonus(liste_niveau_jetons)
        #Check si un bonus est accomplie
        with open ("Banque/active_bonus.txt","r")as active_bonus_txt:
            for i in active_bonus_txt:
                active_bonus=i.rstrip('\n')
                active_bonus=int(active_bonus)
        if liste_niveau_jetons[0] >= liste_jetons_bonus[0] and active_bonus==0:
            mode_jeu=3
        if liste_niveau_jetons[1] >= liste_jetons_bonus[1] and active_bonus==0:
            mode_jeu=4
        if liste_niveau_jetons[2] >= liste_jetons_bonus[2] and active_bonus==0:
            mode_jeu=5
        capte_jetons = 0
        active_bonus=0
    else:
        timer=Ft_Sleep_Timer(timer)
        if timer=="sleep": 
            mode_jeu=1
    return mode_jeu + mode_player + timer

#Mode 1
def FT_StandBY(mode_jeu,mode_player):
    print("Stand BY")
    FT_Base_StandBy()
    capte_jetons=0
    capte_jetons = Ft_Detection(capte_jetons)
    mode_player=0
    if capte_jetons==1:
        #Lance un joueur( lance une boucle de partie)
        Ft_New_Player(mode_player)
        mode_jeu=2
        #Mode jeu
        print('New player !! ')
        print(mode_player)
    return mode_jeu + mode_player



#Moi je renvoie le mode de jeu, mode = 0  Stand fro play, mode = 1 Play ! , mode = 2 BONUS , mode = 3 Il TILT ce CLIENT  
def FT_Tool(mode_jeu):
    #Sans moi le joueur ne gagnera jamais de jetons!
    FT_Trappe(mode_jeu)
    #C'est ici que QT Python affiche TV
    FT_Affichage(mode_jeu)
    #Je scintille
    FT_Led_carousel(mode_jeu)
    #J'ambiance
    Ft_Son(mode_jeu)
    #Je je maintiens l'ordre
    FT_Tilt(mode_jeu)
    return mode_jeu


#Je suis simplement l'instance de jeu
def FT_Start():
    mode_jeu=1
    mode_player=0
    power=1
    timer=0
    while power==1:
        print("Start")
        print(mode_jeu)
        #En realite je controle la machine je fais juste en fonction des modes! 
        FT_Tool(mode_jeu)
        if mode_jeu==1:
            #Moi je ne sers a rien ! j'attend juste un joueur et je matte des videos 
            mode_jeu=FT_StandBY(mode_jeu,mode_player)
        elif mode_jeu==2:
            #Je compte juste les jetons ! Et j'appuie sur le Bonus quand c'est le moment !
            mode_jeu=FT_Play(mode_jeu,mode_player,timer)
        else:
            #Tout le programme n'existe rien que pour moi! JE distribue la bonne valeur au bon client ! 
            mode_jeu=FT_Bonus(mode_jeu,mode_player)




#Dev part
def DEV_Bonus():
    programme=1
    while programme==1:
        print("\n\n---Sélection:\nMode=1: Bonus 1\nMode=2: Bonus 2\nMode=3: Bonus 3\nMode = 4 quitte ou double\nMode =5 quitte le programme")
        mode=int(input("Choisi ton mode"))
        if mode==1:
            choix=int(input("Jetons=1 ou points=2 ou les deux=3"))
            nb_jetons=int(input("Combien de jetons pour gagner bonus?"))
            with open ("Banque/bonus_1.txt","w")as bonus_1_txt:
                if choix==1:
                    nb_jetons_gain=int(input("Combien de jetons gagner avec bonus?"))
                    bonus_1_txt.write("{}\n{}\n".format(nb_jetons,nb_jetons_gain))
                elif choix==2:
                    bonus_1_txt.write("{}\nPOINTS\n".format(nb_jetons))
                else:
                    nb_jetons_gain=int(input("Combien de jetons gagner avec bonus?"))
                    bonus_1_txt.write("{}\nPOINTS\n{}\n".format(nb_jetons,nb_jetons_gain))
        if mode==2:
            choix=int(input("Jetons=1 ou points=2 ou les deux=3"))
            nb_jetons=int(input("Combien de jetons pour gagner bonus?"))
            with open ("Banque/bonus_2.txt","w")as bonus_2_txt:
                if choix==1:
                    nb_jetons_gain=int(input("Combien de jetons gagner avec bonus?"))
                    bonus_2_txt.write("{}\n{}\n".format(nb_jetons,nb_jetons_gain))
                elif choix==2:
                    bonus_2_txt.write("{}\nPOINTS\n".format(nb_jetons))
                else:
                    nb_jetons_gain=int(input("Combien de jetons gagner avec bonus?"))
                    bonus_2_txt.write("{}\nPOINTS\n{}\n".format(nb_jetons,nb_jetons_gain))
        if mode==3:
            choix=int(input("Jetons=1 ou points=2 ou les deux=3"))
            nb_jetons=int(input("Combien de jetons pour gagner bonus?"))
            with open ("Banque/bonus_3.txt","w")as bonus_3_txt:
                if choix==1:
                    nb_jetons_gain=int(input("Combien de jetons gagner avec bonus?"))
                    bonus_3_txt.write("{}\n{}\n".format(nb_jetons,nb_jetons_gain))
                elif choix==2:
                    bonus_3_txt.write("{}\nPOINTS\n".format(nb_jetons))
                else:
                    nb_jetons_gain=int(input("Combien de jetons gagner avec bonus?"))
                    bonus_3_txt.write("{}\nPOINTS\n{}\n".format(nb_jetons,nb_jetons_gain))
        if mode==4:
            choix=0
            with open ("Banque/quitte_ou_double.txt","w")as quitte_ou_double_txt:
                while choix<4:
                    choix=int(input("Numero du bonus\n qui possede le mode quitte ou double, 4= quitter"))
                    quitte_ou_double_txt.write("{}\n".format(choix))
        elif mode==5:
          print("Quitte le programme")
          programme=0



def ft_lancementdev():
    print("lance Dev")
    programme=1
    while programme==1:
        print("\n\n---Sélection:\nMode=1: Dev Bonus\nMode = 2 quitte le programme")
        mode=int(input("Choisi ton mode"))
        if mode==1:
            DEV_Bonus()
        elif mode==2:
          print("Quitte le programme")
          programme=0

#Main menu
programme=1
while programme==1:
    print("\n\n---Sélection:\nMode=1: jeu\n Mode=2: Dev\n Mode=3 quitte le programme")
    mode=int(input("Choisi ton mode"))
    if mode==1:
        FT_Start()#ici que l'on lance la machine, pour qu'elle traduise
    elif mode==2:
        ft_lancementdev()#ici Que l'on lancement le mode devellopment
    elif mode==3: 
      print("Quitte le programme")
      programme=0 