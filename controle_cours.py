import unittest
import doctest

def sup21(nombre):
  if nombre >= 21:
    return True
  else:
    return False

    >>> sup21(21)
    True
    >>> sup21(2)
    False

def pairs(liste):
  for i in range(liste):
    if (nombre%2) ==0 :
      print("{0} est paire".format(nombre))
    else :
      print("{0} est impaire".format(nombre))

    >>> pairs([1,2,3])
    [2]


def ajout4(liste):
  liste.append(4)
  return(liste)
    >>> ajout4([])
    [4]
    >>> ajout4([1,2,4])
    [1, 2, 4, 4]
    >>> l = [1,2,3]
    >>> _ = ajout4(l)
    >>> l
    [1, 2, 3]

def to_strings(dict):
  for k,v in dict.items():
    print("cles:{}-valeurs{}".format(k,v))

    >>> to_strings({1:2})
    ['1:2']
    >>> to_strings({})
    []
    >>> to_strings({1:2,3:4})
    ['1:2', '3:4']

def extremites(liste):
  return liste([1:2],[-2])

    >>> extremites(['a', 'b', 'c', 'd', 'e'])
    ['a', 'b', 'd', 'e']

def comptelettre(mot):
  num =()
  occurence_voulu = input()
  for occurence_voulu in mot:
    if occurence_voulu == "cara":
      num = num+1
      print(num) 
      
Class Mot:
  def occurences(self,caractère):
    self._comptelettre = comptelettre(caractère)

    >>> mot = Mot('Bonjour')
    >>> mot.mot
    'Bonjour'
    >>> mot.comptelettre('o')
    2
    >>> mot.comptelettre('B') == mot.comptelettre('b') == 1
    True
    

def tri_et_inverse(liste):
  sorted(liste,reverse=True)
  return(liste)

    >>> maliste = [4,7,6]
    >>> tri_et_inverse(maliste)
    ([4, 6, 7], [6, 7, 4])
    >>> maliste == [4,7,6]
    True

 
    def aller_a_paris()

    >>> class fake_input:
    ...     def __init__(self, saisies):
    ...         self._iter = iter(saisies)
    ...     def __call__(self, *args, **kwargs):
    ...         return next(self._iter)
    ...
    ...
    >>> list(aller_a_paris(input_call=fake_input(['Barcelone', "Madrid", "Paris"]))) 
    [3, 'Paris']
    >>> aller_a_paris(input_call=fake_input(['Barcelone', "paris"]))
    (2, 'Paris')

ville_nom_pays = {'Paris', 'Berlin', 'Madrid','Moscou}
    
    >>> 'Paris' in ville_nom_pays
    True
    >>> 'Espagne' in list(ville_nom_pays.values())
    True
    >>> to_strings(ville_nom_pays)
    ['Paris:France', 'Berlin:Allemagne', 'Madrid:Espagne', 'Moscou:Russie']

   
    >>> italie = Pays('Italie', False)
    >>> italie.visa
    False
    >>> italie.nom
    'Italie'
    
   

    >>> ville_pays['Moscou'].visa
    True
    >>> ville_pays['Berlin'].visa
    False
    
"""

def aller_a_paris(input_call=input):
    # code a remplir

    # quelque part dans le code de cette fonction: saisie = input_call('Question ')
    # en fonction de saisie on continue a demander ou on renvoie 'Paris'
    # Au lieu d'utiliser input comme en cours vous appelez input_call
    # par défaut elle vaut input donc vous pouvez appeller
    # aller_a_paris() pour tester a la main
    while True:
        return 0, 'Nulle Part'
      
if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)

