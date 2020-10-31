import pygame
from pygame.locals import *
import settings

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((settings.taille_fenetre, settings.taille_fenetre))
#Icone
icone = pygame.image.load(settings.image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(settings.titre_fenetre)

#Affichage du labyrinthe
with open(settings.levels[0], "r") as fichier:
    for ligne in fichier:
        for case in ligne:
            if case == "0" :
                fenetre.blit(settings.image_fond,())
            if case == "1" :
                fenetre.blit(settings.image_mur,())
            if case == "2" :
                fenetre.blit(settings.image_joueur,())
            if case == "3" :
                fenetre.blit(settings.image_arrivee,())
                
