import random

def jeu(nbessai):
  gagne = 0 
  nbessai = 5000
  graphe ={'debut':['P','F'],'P':['PP','F']}
  fin=['PP','F']
  for n in range (nbessai) :
    position ='debut'
    while position not in fin:
      position = random.choice(graphe[position])
      if position==fin[0]:gagne+=1
      s=(gagne/nbessai)
      return s

if __name__ == "__main__":
    resultat = jeu(5000)
    print(resultat)
    pass

 
import unittest
import doctest


if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)
