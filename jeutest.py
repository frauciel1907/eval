#Module test   
import unittest
import doctest
import jeu

if __name__ == "__main__":
    unittest.main(exit=False)
    doctest.testmod(jeu)


if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)

