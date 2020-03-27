import random
import os
import pickle

piece=random.randint(1,2)
if piece == 1:
    print("pile")
if piece == 2:
    print("face")

def initialiser_joueur():
    prenom = input("Veuillez saisir votre prenom: ")
    prenom = prenom.capitalize()
    if not prenom.isalnum() or len(prenom)<2:
        print("Erreur il faut resaisir un prenom valide ")
        return initialiser_joueur()
    else:
        return prenom