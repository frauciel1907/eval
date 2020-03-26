#Maintenant dans ce module on s'intéresse seulement à la probabilité d'avoir deux "pile"

import random


def jeu(nbessai):
  gagne = 0 
  nbessai = int(input("Veuillez saisir le nombre de fois où vous voulez jouer :"))
  graphe ={'debut':['P','F'],'P':['PP','F']}
  fin=['PP','F']
  for n in range (nbessai) :
    position ='debut'
    while position not in fin:
      position = random.choice(graphe[position])
      if position==fin[0]:gagne+=1
return(gagne/nbessai)

if __name__ == "__main__":
    resultat = jeu(5000)
    print(resultat)
    pass