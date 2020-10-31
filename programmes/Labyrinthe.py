
tableau=[[1,1,1,1,1,1,1,1],[1,1,1,0,0,0,2,1],[1,1,0,0,0,0,0,1],[1,0,0,0,1,0,0,1],[1,0,1,0,1,0,0,1],[1,0,1,0,0,0,0,1],[1,3,0,0,1,1,0,1],[1,1,1,1,1,1,1,1]]


def affiche(tab):
    for i in range(len(tab)):
        print(tab[i])
        print(end="")

def grav(tab):#appliquer la gravité
    X=0
    test=0
    test2=0
    gravité=1
    if(gravité==1):#gravité vers le bas
        while(test==0):
            X=X+1
            test=tab[X].count(2)
            
        Y=tab[X].index(2)
        
        while(tab[X+1][Y]==0):
            tab[X][Y]=0
            tab[X+1][Y]=2
            X=X+1

    if(gravité==3):#gravité vers le haut
        while(test==0):
            X=X+1
            test=tab[X].count(2)
            
        Y=tab[X].index(2)
        
        while(tab[X-1][Y]==0):
            tab[X][Y]=0
            tab[X-1][Y]=2
            X=X-1



    if(gravité==2):#gravité vers la gauche
        while(test==0):
            X=X+1
            test=tab[X].count(2)
            
        Y=tab[X].index(2)
        
        while(tab[X][Y-1]==0):
            tab[X][Y]=0
            tab[X][Y-1]=2
            Y=Y-1

    if(gravité==4):#gravité vers la droite
        while(test==0):
            X=X+1
            test=tab[X].count(2)
            
        Y=tab[X].index(2)
        
        while(tab[X][Y+1]==0):
            tab[X][Y]=0
            tab[X][Y+1]=2
            Y=Y+1
    return(tab)


def turn_plat_droite(tab):#tourner le plateau vers la droite
    tab2=[]
    line=[]
    t_line=len(tab[0])
    for j in range(t_line):
        for i in range(t_line):
            line.append(tab[i][j])
        line.reverse()
        tab2.append(line)
        line=[]
    
    return(tab2)

def turn_plat_gauche(tab):#tourner le plateau vers la gauche
    tab2=[]
    line=[]
    t_line=len(tab[0])

    for j in range(t_line):
        for i in range(t_line):
            line.append(tab[i][-j])
        tab2.append(line)
        line=[]

    tab2.append(tab2[0])
    del tab2[0]
    return(tab2)

def victoire(tab):#Savoir si le joueur a gagné
    test=0
    essai=0
    X=0
    while(test==0):
        X=X+1
        test=tab[X].count(2)
            
    Y=tab[X].index(2)

    if(tab[X+1][Y]==3):
        essai=1
    if(tab[X-1][Y]==3):
        essai=1
    if(tab[X][Y+1]==3):
        essai=1
    if(tab[X][Y-1]==3):
        essai=1
    return(essai)
    

def main(tab):
    jeu="ON"
    test_victoire=0
    while(jeu=="ON"):
        affiche(tab)
        print("Appuie sur 'Q' pour tourner le tableau vers la gauche, appuie sur 'D' pour tourner le tableau vers la droite")
        bind=input()
        if(bind=="Q"):
            tab=turn_plat_gauche(tab)
            affiche(tab)
            print("Application de la gravité...")
            tab=grav(tab)
            test_victoire=victoire(tab)
            if(test_victoire==1):
                print("Vous avez gagné")
                jeu="OFF"
                
        if(bind=="D"):
            tab=turn_plat_droite(tab)
            affiche(tab)
            print("Application de la gravité...")
            tab=grav(tab)
            if(test_victoire==1):
                print("Vous avez gagné")
                jeu="OFF"
                
        if(bind=="O"):
            jeu="OFF"

