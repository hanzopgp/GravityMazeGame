from Labyrinthe import *
from GenLabyrinthe import *

tableau=randomize(tailleTab())
main(tableau)
class Labyrinthe(object):
    def __init__(self,dimension):
        self.dimension=dimension
        self.tab=[[1 for i in range(self.dimension)]for j in range(self.dimension)]
        

    def randomize(self):
        coord=randint(0,len(self.tab)-1)
        self.tab[0][coord]=2
        for i in range(1,len(self.tab)):
            coord2= randint(0,len(self.tab)-1)
            if(coord<coord2):
                for j in range(coord,coord2):
                    self.tab[i][j]=0
            if(coord2<coord):
                for j in range(coord2,coord):
                    self.tab[i][j]=0
        
            self.tab[i][coord2]=0
            self.tab[i][coord]=0
        
            coord=coord2
        self.tab[-1][coord2]=3

        line=[]

        for i in range(len(self.tab)):
            line.append(1)
        self.tab.append(line)

        for i in range(len(self.tab)):
            self.tab[i].append(1)
            self.tab[i][0]=1

        tab2=[]
        tab2.append(line)
        for i in range(0,len(self.tab)):
            tab2.append(self.tab[i])
        return tab2

    def grav(self):#appliquer la gravité
        X=0
        test=0
        test2=0
        gravité=1
        if(gravité==1):#gravité vers le bas
            while(test==0):
                X=X+1
                test=self.tab[X].count(2)
            
            Y=self.tab[X].index(2)
        
            while(self.tab[X+1][Y]==0):
                self.tab[X][Y]=0
                self.tab[X+1][Y]=2
                X=X+1
        return(self.tab)

    def affiche(self):
        for i in range(len(self.tab)):
            print(self.tab[i])
            print(end="")

    def turn_plat_droite(self):#tourner le plateau vers la droite
        tab2=[]
        line=[]
        t_line=len(self.tab[0])
        for j in range(t_line):
            for i in range(t_line):
                line.append(self.tab[i][j])
            line.reverse()
            tab2.append(line)
            line=[]
    
        return(tab2)

    def turn_plat_gauche(self):#tourner le plateau vers la gauche
        tab2=[]
        line=[]
        t_line=len(self.tab[0])

        for j in range(t_line):
            for i in range(t_line):
                line.append(self.tab[i][-j])
            tab2.append(line)
            line=[]

        tab2.append(tab2[0])
        del tab2[0]
        return(tab2)

    def victoire(self):#Savoir si le joueur a gagné
        test=0
        essai=0
        X=0
        while(test==0):#Boucle
            X=X+1#pour
            test=self.tab[X].count(2)#trouver
                #la position
        Y=self.tab[X].index(2)#de la boule

        if(self.tab[X+1][Y]==3):
            essai=1
        if(self.tab[X-1][Y]==3):
            essai=1
        if(self.tab[X][Y+1]==3):
            essai=1
        if(self.tab[X][Y-1]==3):
            essai=1
        return(essai)

    def main(self):
        jeu="ON"
        test_victoire=0
        while(jeu=="ON"):
            affiche(self.tab)
            print("Appuie sur 'Q' pour tourner le tableau vers la gauche, appuie sur 'D' pour tourner le tableau vers la droite")
            bind=input()
            if(bind=="Q"):
                tab=turn_plat_gauche(self.tab)
                affiche(self.tab)
                print("Application de la gravité...")
                self.tab=grav(self.tab)
                test_victoire=victoire(self.tab)
                if(test_victoire==1):
                    print("Vous avez gagné")
                    jeu="OFF"
                    
            if(bind=="D"):
                self.tab=turn_plat_droite(self.tab)
                affiche(self.tab)
                print("Application de la gravité...")
                self.tab=grav(self.tab)
                if(test_victoire==1):
                    print("Vous avez gagné")
                    jeu="OFF"
                    
            if(bind=="O"):
                jeu="OFF"

            
l1=Labyrinthe(10)

#class Mouvement(object):
 #   def __init__(self):
        
#print(l1.main())

