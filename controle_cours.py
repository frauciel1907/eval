import unittest
import doctest

def sup21(nombre):
  if nombre >= 21:
    return True
  else:
    return False

sup21(21)
    
sup21(2)
   

def pairs(x):
  return [i for i in x if i%2==0]

pairs([1,2,3])
    


def ajout4(liste):
  liste.append(4)
  return(liste)

ajout4([])
   
ajout4([1,2,4])
  
l = [1,2,3]
_ = ajout4(l)
l
   

def to_strings(x):
  return [str(i)+":"+str(j) for i,j in zip(x.keys(),x.values())]

to_strings({1:2})
  
to_strings({})
 
to_strings({1:2,3:4})


def extremites(liste):
  return liste[0:2]+liste[-2:]

extremites(['a', 'b', 'c', 'd', 'e'])
    

def comptelettre(mot):
  num =()
  occurence_voulu = input()
  for occurence_voulu in mot:
    if occurence_voulu == "cara":
      num = num+1
      print(num) 
      

    

def tri_et_inverse(liste):
  sorted(liste,reverse=True)
  return(liste)

maliste = [4,7,6]
tri_et_inverse(maliste)


     
"""
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
    


def aller_a_paris(input_call=input):
   
        return 0, 'Nulle Part'
      
if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)


"""