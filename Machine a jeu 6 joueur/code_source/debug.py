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

#TOOL


def Ft_detection(detection):
    detection=int(input("Insere un jetons\n"))

def  Ft_Ouverture_trappe():
    print("Ouverture de la trappe")

def  Ft_Fermeture_trappe():
    print("Ouverture de la trappe")

def Ft_Sleep_Timer():
    print("Sleep too much and i Stand by ")



#Write txt > SQL
def Ft_New_Player():
        with open ("banque/joueur/nombre_joueur.txt","r")as nombre_joueur:
            for i in nombre_joueur:
                nb_joueur=i.rstrip('\n')
                print("Vous etes le joueur {}".format(nb_joueur))
                nb_joueur=int(nb_joueur)
                prochaincode=nb_joueur+1
                prochaincode=str(prochaincode)
        with open ("banque/joueur/nombre_joueur.txt","w")as nombre_joueur:
            nombre_joueur.write(prochaincode)

def FT_Niveau_Bonus(niveau_jetons1,niveau_jetons2,niveau_jetons3):
    #Bonus 1 curseur
        with open ("banque/bonus/nb_bonus1.txt","r")as nb_bonus1_txt:
            for i in nb_bonus1_txt:
                niveau_jetons1=i.rstrip('\n')
                niveau_jetons1=int(niveau_jetons1)
                niveau_jetons1=niveau_jetons1+1
                niveau_jetons1=str(niveau_jetons1)
        with open ("banque/bonus/nb_bonus1.txt","w")as nb_bonus1_txt:
            nb_bonus1_txt.write(niveau_jetons1)
            niveau_jetons1=int(niveau_jetons1)
    #Bonus 2 curseur
        with open ("banque/bonus/nb_bonus2.txt","r")as nb_bonus2_txt:
            for i in nb_bonus2_txt:
                niveau_jetons2=i.rstrip('\n')
                niveau_jetons2=int(niveau_jetons2)
                niveau_jetons2=niveau_jetons2+1
                niveau_jetons2=str(niveau_jetons2)
        with open ("banque/bonus/nb_bonus2.txt","w")as nb_bonus2_txt:
            nb_bonus2_txt.write(niveau_jetons2)
            niveau_jetons2=int(niveau_jetons2)
    #Bonus 3 curseur
        with open ("banque/bonus/nb_bonus3.txt","r")as nb_bonus3_txt:
            for i in nb_bonus3_txt:
                niveau_jetons3=i.rstrip('\n')
                niveau_jetons3=int(niveau_jetons3)
                niveau_jetons3=niveau_jetons3+1
                niveau_jetons3=str(niveau_jetons3)
        with open ("banque/bonus/nb_bonus3.txt","w")as nb_bonus3_txt:
            nb_bonus3_txt.write(niveau_jetons3)
            niveau_jetons3=int(niveau_jetons3)

def Ft_Active_Bonus(active_bonus):
    with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
        active_bonus_txt.write("{}\n".format(active_bonus))


#Mode 3 Bonus

def FT_Bonus1():
    debug=0
    if debug==0:
        return
    active_bonus1=1
    if active_bonus==0:
        active_bonus=1
        print("\nBONUS\n")
        Ft_Active_Bonus(active_bonus)
        while active_bonus==1:
            active_bonus=0
            niveau_jetons1=0
            gain=jetons_bonus_gain1
            if mode_quitte_double1==0:
                quitte_double=1
            else:
                quitte_double=int(input("Mode quitte = 1 ou double =2?"))
            if quitte_double==2:
                de=random.random() * 100
                print("Le de a fait {} sur 100".format(de))
                if de>50:
                    gain=gain*2
                    victoire=victoire+1
                    if victoire<3:
                        active_bonus=int(input("Vous avez gagner voulez vous rejouer? 1=Oui 0=Non"))
                    if active_bonus==0:
                        if gain>0:
                            print("Gagne {} Jetons".format(gain))
                        if points_bonus_gain1==1:
                            victoire=victoire*2
                            print("Gagne {} points".format(victoire))
                        victoire=0
                elif de==50:
                    active_bonus=int(input("Ressayer? 1=oui, 2=non"))
                else:
                    print("Vous avez perdu")
            else:
                if jetons_bonus_gain1>0:
                    print("Gagne {} Jetons".format(jetons_bonus_gain1))
                if points_bonus_gain1==1:
                    print("Gagne 1 points")
        active_bonus1=0
        active_bonus=0
        Ft_Active_Bonus(active_bonus)

def FT_Bonus2():
    active_bonus2=1
    if active_bonus==0:
        active_bonus=1
        print("\nBONUS\n")
        Ft_Active_Bonus(active_bonus)
        while active_bonus==1:
            active_bonus=0
            niveau_jetons2=0
            if mode_quitte_double2==0:
                quitte_double=1
            else:
                quitte_double=int(input("Mode quitte = 1 ou double =2?"))
            if quitte_double==2:
                de=random.random() * 100
                print("Le de a fait {} sur 100".format(de))
                if de>50:
                    gain=jetons_bonus_gain2*2
                    if gain>0:
                        print("Gagne {} Jetons".format(gain))
                    if points_bonus_gain2==1:
                        print("Gagne 2 points")
                elif de==50:
                    active_bonus=int(input("Ressayer? 1=oui, 2=non"))
                else:
                    print("Vous avez perdu")
            else:
                if jetons_bonus_gain2>0:
                    print("Gagne {} Jetons".format(jetons_bonus_gain2))
                if points_bonus_gain2==1:
                    print("Gagne 1 points")
        active_bonus2=0
        active_bonus=0
        Ft_Active_Bonus(active_bonus)

def FT_Bonus3():
    active_bonus3=1
    print("\nBONUS\n")
    if active_bonus==0:
        active_bonus=1
        FT_Niveau_Bonus(niveau_jetons1,niveau_jetons2,niveau_jetons3)
        Ft_Active_Bonus(active_bonus)
        
    active_bonus==1:
    active_bonus=0
    niveau_jetons3=0
    if mode_quitte_double3==0:
        quitte_double=1
    else:
        quitte_double=int(input("Mode quitte = 1 ou double =2?"))
    if quitte_double==2:
        de=random.random() * 100
        print("Le de a fait {} sur 100".format(de))
        if de>50:
            gain=jetons_bonus_gain3*2
            if gain>0:
                print("Gagne {} Jetons".format(gain))
                
            if points_bonus_gain3==1:
                print("Gagne 2 points")
        elif de==50:
            active_bonus=int(input("Ressayer? 1=oui, 2=non"))
        else:
            print("Vous avez perdu")
    else:
        if jetons_bonus_gain3>0:
            print("Gagne {} Jetons".format(jetons_bonus_gain3))
        if points_bonus_gain3==1:
            print("Gagne 1 points")
active_bonus3=0
active_bonus=0
Ft_Active_Bonus(active_bonus)



#Mode 2 Play
def FT_Play(mode_jeu):
    niveau_jetons1=0
    niveau_jetons2=0
    niveau_jetons3=0
    active_bonus=0
    detection=0
    Ft_detection(detection)
    if detection==1:
        jetons=jetons+1
        FT_Niveau_Bonus(niveau_jetons1,niveau_jetons2,niveau_jetons3)
        with open ("banque/bonus/active_bonus.txt","r")as active_bonus_txt:
            for i in active_bonus_txt:
                active_bonus=i.rstrip('\n')
                active_bonus=int(active_bonus)
        if niveau_jetons1 == jetons_bonus1 or active_bonus1==1:
            FT_Bonus1()
        if niveau_jetons2 == jetons_bonus2 or active_bonus2==1:
            FT_Bonus2()
        if niveau_jetons3 == jetons_bonus3 or active_bonus3==1:
            FT_Bonus3()
        niveau_bonus1=niveau_jetons1*100/jetons_bonus1  
        niveau_bonus2=niveau_jetons2*100/jetons_bonus2
        niveau_bonus3=niveau_jetons3*100/jetons_bonus3
        print("Barre bonus 1 {}\nBarre bonus 2 {}\nBarre bonus 3 {}\n".format(niveau_bonus1,niveau_bonus2,niveau_bonus3))
        detection = 0
        active_bonus=0
    else:
        Ft_Sleep_Timer()

#Mode 1
def FT_StandBY(mode_jeu):
    detection=0
    Ft_detection(detection)
    if detection==1:
        #Lance un joueur( lance une boucle de partie)
        Ft_New_Player()
        ouverture = 1
        mode_jeu=1
        #Mode jeu




def FT_Trappe():
    debug=0
    if debug==0:
        return
    if mode==0 or mode==4:
        Ft_Fermeture_trappe
    if mode==1:
        Ouverture

def FT_Affichage(mode_jeu):
    debug=0
    if debug==0:
        return
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
    debug=0
    if debug==0:
        return
    if mode_jeu==1:
        print("Je suis jolie ! Viens jouer avec moi")
    if mode_jeu==2:
        print("C'est bien joue ")
    if mode_jeu==3:
        print("Je fais de toi un heureux gagnant")
    if mode==4:
        print("T'es vraiment une pute!")

def Ft_Son(mode_jeu):
    debug=0
    if debug==0:
        return
    if mode_jeu==0:
        print("Bim bim ")
    if mode_jeu==3:
        print("Trin trin trin trin")
    if mode_jeu==4:
        print("ahahahahha Vous etes un connard!")
def FT_Tilt(mode_jeu):
    debug=0
    if debug==0:
        return
    #Check tilt
    Tilt=0
    if Tilt==1:
        mode=4

def FT_Tool(mode_jeu):
    debug=0
    if debug==0:
        return
    #Moi je renvoie le mode de jeu, mode = 0  Stand fro play, mode = 1 Play ! , mode = 2 BONUS , mode = 3 Il TILT ce CLIENT  
        FT_Trappe(mode_jeu)
        FT_Affichage(mode_jeu)
        FT_Led_carousel(mode_jeu)
        Ft_Son(mode_jeu)
        FT_Tilt(mode_jeu)



def FT_start():
    debug=0
    if debug==0:
        return
    mode_jeu=0
    power=1
    while power==1:
        if mode==0:
            FT_StandBY(mode_jeu)
        else:
            FT_Play(mode_jeu)
        FT_Tool(mode_jeu)



#Dev part
def DEV_Bonus():
    debug=0
    if debug==0:
        return
    programme=1
    while programme==1:
        print("\n\n---Sélection:\nMode=1: Bonus 1\nMode=2: Bonus 2\nMode=3: Bonus 3\nMode = 4 quitte ou double\nMode =5 quitte le programme")
        mode=int(input("Choisi ton mode"))
        if mode==1:
            choix=int(input("Jetons=1 ou points=2 ou les deux=3"))
            nb_jetons=int(input("Combien de jetons pour gagner bonus?"))
            with open ("banque/bonus/bonus_1.txt","w")as bonus_1_txt:
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
            with open ("banque/bonus/bonus_2.txt","w")as bonus_2_txt:
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
            with open ("banque/bonus/bonus_3.txt","w")as bonus_3_txt:
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
            with open ("banque/bonus/quitte_ou_double.txt","w")as quitte_ou_double_txt:
                while choix<4:
                    choix=int(input("Numero du bonus\n qui possede le mode quitte ou double, 4= quitter"))
                    quitte_ou_double_txt.write("{}\n".format(choix))
        elif mode==5:
          print("Quitte le programme")
          programme=0



def ft_lancementdev():
    debug=0
    if debug==0:
        return
    print("lance Dev")
    programme=1
    while programme==1:
        print("\n\n---Sélection:\nMode=1: Dev Bonus\nMode = 2 quitte le programme")
        mode=int(input("Choisi ton mode"))
        if mode==1:
            dev_bonus()
        elif mode==2:
          print("Quitte le programme")
          programme=0

#Main menu
debug=0
if debug==0:
    return
programme=1
while programme==1:
    print("\n\n---Sélection:\nMode=1: jeu\n Mode=2: Dev\n Mode=3 quitte le programme")
    mode=int(input("Choisi ton mode"))
    if mode==1:
        ft_start()#ici que l'on lance la machine, pour qu'elle traduise
    elif mode==2:
        ft_lancementdev()#ici Que l'on lancement le mode devellopment
    elif mode==3: 
      print("Quitte le programme")
      programme=0 