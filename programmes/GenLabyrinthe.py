from random import *



def tailleTab(): # créé un tableau rempli de murs d'une taille demandée
    print("Taille du tableau?")
    taille=int(input())
    line=[]
    tableau=[]
    case_mur=1
    for i in range (taille):
        for j in range(taille):
            line.append(case_mur)
        tableau.append(line)
        line=[]
    return(tableau)
            
def randomize(tab): #créé le chemin random du labyrinthe
    coord=randint(0,len(tab)-1)
    tab[0][coord]=2
    for i in range(1,len(tab)):
        coord2= randint(0,len(tab)-1)
        tab[i][coord2]=0
        tab[i][coord]=0
        if(coord<coord2):
            for j in range(coord,coord2):
                tab[i][j]=0
        if(coord2<coord):
            for j in range(coord2,coord):
                tab[i][j]=0
        coord=coord2
    tab[-1][coord2]=3
    return(tab)

def place_bordure(tab):
    newTab=[]
    newLine=[]
    for i in range(len(tab)):#place bordure à gauche
        newLine.append(1)
        for j in range(len(tab)):
            newLine.append(tab[i][j])
        newTab.append(newLine)
        newLine=[]
    for i in range(len(tab)):#place bordure à droite
        newTab[i].append(1)

    newTab2=[]
    newLine2=[]

    for i in range(len(newTab[0])):
        newLine2.append(1)

    newTab2.append(newLine2)

    for i in range(len(newTab)):
        newTab2.append(newTab[i])

    newTab2.append(newLine2)
    
    return(newTab2)


    
