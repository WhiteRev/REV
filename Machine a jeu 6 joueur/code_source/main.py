import random
import time
import webbrowser
import urllib 


#Int TOOL

def ft_init_joueur():
    with open ("banque/joueur/nombre_joueur.txt","w")as nombre_joueur:
        nombre_joueur.write("1\n")
def init():
    print("Init")
    ft_On_tapis()
    ft_init_joueur()

#TOOL

def ft_mode_bonus():
    pass

def ft_bonus1(bonus_1):
    print("Gagne {} Jetons".format(bonus_1))
def ft_bonus2(bonus_2):
    print("Gagne {} Jetons".format(bonus_2))
def ft_bonus3(bonus_3,mode_bonus3):
    if mode_bonus3==1:
        print("Gagne {} Jetons".format(bonus_3))
    else:
        print("Bonus plaquette")

def ft_led_jeu():
    print("Led jeu")
    pass


def ft_fin():
    print("Fin")


def ft_detection_jetons(detection):
    print("detection")
    detection=int(input("detect"))

def ft_tilt(jeu):
    tilt=0
    if tilt==1:
        print("TILT")

def ft_affichage_jeu():
    print("Affichage jeu")
    pass

def ft_trappe(ouverture):
    if ouverture == 1:
        print("Ouvre la trappe")
    else:
        print("Fermeture la trappe")


def ft_joueur(nb_joueur):#La fonction permet de compter le nombre de joueur pour compter le nombre de jetons de chacun
    with open ("banque/joueur/nombre_joueur.txt","r")as nombre_joueur:
      for i in nombre_joueur:
        nb_joueur=i.rstrip('\n')
        print("Vous etes le joueur {}".format(nb_joueur))
        nb_joueur=int(nb_joueur)
        prochaincode=nb_joueur+1
        prochaincode=str(prochaincode)
    with open ("banque/joueur/nombre_joueur.txt","w")as nombre_joueur:
        nombre_joueur.write(prochaincode)





def ft_lecture_bonus1(jetons_bonus1):
    with open ("banque/bonus/bonus_1.txt","r")as bonus_1_txt:
      for i in bonus_1_txt:
            jetons_bonus1=i.rstrip('\n')
            jetons_bonus1=int(jetons_bonus1)
def ft_lecture_bonus2(jetons_bonus2):
    with open ("banque/bonus/bonus_2.txt","r")as bonus_2_txt:
      for i in bonus_2_txt:
            jetons_bonus2=i.rstrip('\n')
            jetons_bonus2=int(jetons_bonus2)
def ft_lecture_bonus3(jetons_bonus3,mode_bonus3):
    with open ("banque/bonus/bonus_3.txt","r")as bonus_3_txt:
      for i in bonus_3_txt:
        if "jetons" in i:
            mode_bonus3=1
        elif mode_bonus3==1:
            jetons_bonus3=i.rstrip('\n')
            jetons_bonus3=int(jetons_bonus1)


def ft_affichage_clip():
    print("Affichage Clip")


def ft_carousel_led():
    if mode==1:
        print("led")
    if mode==2:
        print("led")

    if mode==3:
     print("Carousel led")

def ft_On_tapis():
    print("Activation tapis")

def ft_Off_Tapis():
    print("Desactivation tapis")

def Ft_detection(detection):
    detection=int(input("Insere un jetons\n"))

def ft_son_jetons():
    print("Son jetons")

#Mode 3 Bonus 


def FT_Bonus1():
    active_bonus1=1
if active_bonus==0:
    active_bonus=1
    print("\nBONUS\n")
    with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
        active_bonus_txt.write("{}\n".format(active_bonus))
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
    with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
        active_bonus_txt.write("{}\n".format(active_bonus))

def FT_Bonus2():
    active_bonus2=1
    if active_bonus==0:
        active_bonus=1
        print("\nBONUS\n")
        with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
            active_bonus_txt.write("{}\n".format(active_bonus))
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
        with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
            active_bonus_txt.write("{}\n".format(active_bonus))

def FT_Bonus3():
    active_bonus3=1
    print("\nBONUS\n")
    if active_bonus==0:
        active_bonus=1
        with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
            active_bonus_txt.write("{}\n".format(active_bonus))
        while active_bonus==1:
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
        with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
            active_bonus_txt.write("{}\n".format(active_bonus))


#Mode 2 Play

def FT_Play():
       while jeu==1:
                ft_tilt(jeu)#Le TILT qui bloque quand le joueur frappe la machine
                ft_affichage_jeu()#Lance l'affichage du jeu
                if detection == 1:
                    time1 = time.time()
                    print("Son jetons")
                    jetons=jetons+1
                    niveau_jetons1=niveau_jetons1+1
                    niveau_jetons2=niveau_jetons2+1      
                    with open ("banque/bonus/nb_bonus1.txt","w")as nb_bonus1_txt:
                        niveau_jetons1=str(niveau_jetons1)
                        nb_bonus1_txt.write(niveau_jetons1)
                        niveau_jetons1=int(niveau_jetons1)    
                    with open ("banque/bonus/nb_bonus2.txt","w")as nb_bonus2_txt:
                        niveau_jetons2=str(niveau_jetons2)
                        nb_bonus2_txt.write(niveau_jetons2)
                        niveau_jetons2=int(niveau_jetons2)                      
                    with open ("banque/bonus/nb_bonus3.txt","r")as nb_bonus3_txt:
                        for i in nb_bonus3_txt:
                            niveau_jetons3=i.rstrip('\n')
                            niveau_jetons3=int(niveau_jetons3)
                            niveau_jetons3=niveau_jetons3+1
                            niveau_jetons3=str(niveau_jetons3)
                    with open ("banque/bonus/nb_bonus3.txt","w")as nb_bonus3_txt:
                        nb_bonus3_txt.write(niveau_jetons3)
                        niveau_jetons3=int(niveau_jetons3)
                    with open ("banque/bonus/active_bonus.txt","r")as active_bonus_txt:
                      for i in active_bonus_txt:
                        active_bonus=i.rstrip('\n')
                        active_bonus=int(active_bonus)
                    webbrowser.open('file:///home/turinglinux/Bureau/Machine_Jeu/index.html') 
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
                time2 = time.time()
                print(time1)
                print(time2)
                time3=time2-time1
                print(time3)
                if time3>30:
                    print("Boum")
                    jeu=0
                detection=int(input("Insere un jetons\n"))
                ft_led_jeu()#Activation des leds en mode jeu
            ouverture = 0
            ft_trappe(ouverture)

#Mode 3 StandBY

def StandBY():
    detection=0
    Ft_detection(detection)
    if detection==1:
        #Lance un joueur( lance une boucle de partie)
        with open ("banque/joueur/nombre_joueur.txt","r")as nombre_joueur:
            for i in nombre_joueur:
            nb_joueur=i.rstrip('\n')
            print("Vous etes le joueur {}".format(nb_joueur))
            nb_joueur=int(nb_joueur)
            prochaincode=nb_joueur+1
            prochaincode=str(prochaincode)
        with open ("banque/joueur/nombre_joueur.txt","w")as nombre_joueur:
            nombre_joueur.write(prochaincode)
        ouverture = 1
        jeu=1
        ft_trappe(ouverture)#Ouvre la trappe
        #Mode jeu

def ft_start_int(data)
    data
    {

    detection = 0
    power = 1 
    ouverture = 0
    jeu = 0
    mode_bonus3=0
    nb_joueur=1
    jetons=0
    jetons_bonus1=0
    jetons_bonus2=0
    jetons_bonus3=0
    mode_bonus3=0
    tour=0
    active_bonus=0
    active_bonus1=0
    active_bonus2=0
    active_bonus3=0
    mode_quitte_double1=0
    mode_quitte_double2=0
    mode_quitte_double3=0
    points_bonus_gain1=0
    points_bonus_gain2=0
    points_bonus_gain3=0
    niveau_jetons1=0
    niveau_jetons2=0
    niveau_jetons3=0
    niveau_bonus1=0
    niveau_bonus2=0
    niveau_bonus3=0
    jetons_bonus_gain1=0
    jetons_bonus_gain2=0
    jetons_bonus_gain3=0
    victoire=0
    time1=0
    time2=0
    time3=0
    }
with open ("banque/joueur/nombre_joueur.txt","w")as nombre_joueur:
        nb_joueur=str(nb_joueur)
        nombre_joueur.write(nb_joueur)
        nb_joueur=int(nb_joueur)
    with open ("banque/bonus/quitte_ou_double.txt","r")as quitte_ou_double_txt:
        for i in quitte_ou_double_txt:
            numero_quitte_double=i.rstrip('\n')
            numero_quitte_double=int(numero_quitte_double)
            if numero_quitte_double==1:
                mode_quitte_double1=1
            elif numero_quitte_double==2:
                mode_quitte_double2=1
            elif numero_quitte_double==3:
                mode_quitte_double3=1
    with open ("banque/bonus/active_bonus.txt","w")as active_bonus_txt:
        active_bonus_txt.write("{}\n".format(active_bonus))
    with open ("banque/bonus/bonus_1.txt","r")as bonus_1_txt:
      for i in bonus_1_txt:
            if tour==0:
                jetons_bonus1=i.rstrip('\n')
                jetons_bonus1=int(jetons_bonus1)
            else:
                if "POINTS" in i:
                    points_bonus_gain1=1
                else:
                    jetons_bonus_gain1=i.rstrip('\n')
                    jetons_bonus_gain1=int(jetons_bonus_gain1)
            tour+=1
    tour=0
    with open ("banque/bonus/bonus_2.txt","r")as bonus_2_txt:
      for i in bonus_2_txt:
            if tour==0:
                jetons_bonus2=i.rstrip('\n')
                jetons_bonus2=int(jetons_bonus2)
            else:
                if "POINTS" in i:
                    points_bonus_gain2=1
                else:
                    jetons_bonus_gain2=i.rstrip('\n')
                    jetons_bonus_gain2=int(jetons_bonus_gain1)
            tour+=1
    tour=0      
    with open ("banque/bonus/bonus_3.txt","r")as bonus_3_txt:
      for i in bonus_3_txt:
        if tour==0:
            jetons_bonus3=i.rstrip('\n')
            jetons_bonus3=int(jetons_bonus3)
        else:
            if "POINTS" in i:
                points_bonus_gain3=1
            else:
                jetons_bonus_gain3=i.rstrip('\n')
                jetons_bonus_gain3=int(jetons_bonus_gain1)
        tour+=1
    tour=0
    with open ("banque/bonus/nb_bonus3.txt","w")as nb_bonus3_txt:
        niveau_jetons3=str(niveau_jetons3)
        nb_bonus3_txt.write(niveau_jetons3)   
    niveau_jetons3=int(niveau_jetons3) 


def ft_start():
    data={
    }
    ft_start_int(data)
    while power==1:
        FT_StandBY()
        FT_Play()
    
     
        ft_carousel_led()
        ft_affichage_clip()


def dev_bonus():
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