


def FT_read_titre():
    print("Read titre")





import webbrowser




import os
programme=1
import time
affichage="\n\n\n\n\n\n\n\n\n\n\n\n=>        ---Contre Moulinette activation\n\n\n"
#Exercice de test
a = 1
#Test tout exercice
c = 1
#INIT




init=0

nb_ex=0
pdf=""
consigne =""
Programme_titre=""
Programme_name=""
if init == 0:
    os.system("mkdir Banque")
    with open ("Banque/fiche_utilisateur.txt","w")as fiche_exercice:
        print("Init")
    

#Exercice Space
nb_ex=10
for init in range(0,nb_ex):
    os.system("mkdir Banque/space_{}".format(init,init))
    with open ("Banque/space_{}/fiche_exercice.txt_{}".format(init,init),"w")as fiche_exercice:
        print("Init")
    nb_ex = init


i = 0
w = 0

programme_sortie = ""
nb_titre=0
compte_rendu=[]
FT_read_titre()
for w in range(1,10):
    print(affichage)
    print("Try {}".format(w))
    for i in range(1,10):
        if c > 0:
            a = i
        if a == i:
            print('Exercice test {}'.format(i))
            print("Programme test name {}".format(Programme_titre))
            print('Exercice test {} pdf {}'.format(i,pdf))
            print("Exercice test {} consigne sortie {}".format(i,consigne))
            print("Programme test name {} sortie {}".format(Programme_titre,programme_sortie))
            consigne=programme_sortie
            if consigne == programme_sortie:
                print("WIN")
                os.system("mv Banque/space_{} Banque/WIN_space_{}".format(i,i))


        print("compte rendu {}".format(w))

    time.sleep(3)
    webbrowser.open('https://intra.etna-alternance.net/#/user/landau_s') 

