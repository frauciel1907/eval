import random
import doctest

gagne = 0 
nbessai = 5000

def jeu(nbessai):
  gagne = 0 
  nbessai = int(input("Veuillez saisir le nombre de fois où vous voulez jouer"))
graphe ={'debut':['P','F'],'P':['PP','F']}
fin=['PP','F']
for n in range (nbessai) :
  position ='debut'
  while position not in fin:
    position = random.choice(graphe[position])
    if position==fin[0]:gagne+=1
return(gagne/nbessai)

if __name__ == "__main__":
    unittest.main(exit=False)
    doctest.testmod(devine)