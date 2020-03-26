#1
def sup21(x):
    return x>=21

#2
def pairs(nombre):
  return [i for i in nombre if i%2==0]
pairs([1,2,3])

#3 paris
class fake_input:
  def __init__(self, saisies):
    self._iter = iter(saisies)
         
    def __call__(self, *args, **kwargs):
        return next(self._iter)


def aller_a_paris(input_call=input):
  saisie = ''
  nb = 0
  while saisie.lower() != 'Paris':
    saisie = input_call('Entrez le mot Paris :')
    nb+=1
return nb,'Paris'


list(aller_a_paris(input_call=fake_input(['Barcelone', "Madrid", "Paris"]))) 
aller_a_paris(input_call=fake_input(['Barcelone', "Paris"]))


    
if __name__ == "__main__":
     import doctest

     doctest.testmod(verbose=True)