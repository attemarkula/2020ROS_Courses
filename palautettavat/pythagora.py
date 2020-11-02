#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
"""
palautettava työ:

  kysy ensin kayttajalta halutaanko laskea hypotenuusa vai katetti sen 
  jälkeen kysy joko kaksi katettia tai kateetti ja hypotenuusa.
"""
global kateetti1
global kateetti2
global hypotenuusa

def helppo(mode="print"):
    if mode=="print":
      print ("""
      helppo: 
      kysy ensin kayttajalta halutaanko laskea hypotenuusa vai katetti sen 
      jälkeen kysy joko kaksi katettia tai kateetti ja hypotenuusa.
      """)

    poistu=False
    while (not poistu):
        print("Lasketaanko hypotenuusa (H) vai kateetti (K) :")
        op=input()
        if op  == "H" or op  == "h":
            kateetti1 = float(input("Anna ensimmäinen kateetti:"))
            kateetti2 = float(input("     Anna toinen kateetti:"))
            print("Hypotenuusa :"+str(math.sqrt(kateetti1**2 + kateetti2**2)))
            poistu=True
            pass
        elif op == "K" or op == "k":
            hypotenuusa = float(input("Anna hypotenuusa:"))
            kateetti1 = float(input("Anna ensimmäinen kateetti:"))
            kateetti2 = math.sqrt(hypotenuusa**2 - kateetti1**2)
            print("Toinen kateetti :"+str(kateetti2))
            poistu=True
            pass
        else:
            print("jotain ongelmaa syötteessä, koita uudelleen.")
            poistu=False
            pass
        return(kateetti1,kateetti2)
#def helppo(mode) ends

def normaali():
    print ("""
    normaali: 
    sama kuin helppo, 
    mutta kysytään myos haluaako kayttaja tietaa kolmion alan, 
    jos haluaa lasketaan myos se ja tulostetaan tulos
    """)

    (kateetti1,kateetti2)=helppo("noprint")
    op = input("Tulostetaanko kolmion ala (K/E):")
    if (op == "K" or op == "k"):
        print("Tulos :"+str((kateetti1 * kateetti2)/2))
    pass
#def normaali() ends

def vaikea():
    print (    """
    vaikea tehtävä:
    Koodi tarkastaa etta kayttaja on antanut oikean vastauksen, 
    mikali ei kysyy uudelleen saman kysymyksen
    """ )

    _MAXTRYLIMIT = 5 #counter max limit
    counter=0

    while (counter<_MAXTRYLIMIT):
        counter+=1
        print("Anna ensimmäinen kateetti:")
        num=input()
        try:
            kateetti1 = float(num)
        except NameError:
            print("NameError")
        except ValueError:
            print("ValueError")
        except TypeError:
            print("TypeError")
        else:
            #print("no errors value: "+str(num))
            counter=_MAXTRYLIMIT

    counter=0
    while (counter<_MAXTRYLIMIT):
        counter+=1
        print("     Anna toinen kateetti:")
        num=input()
        try:
            kateetti2 = float(num)
        except NameError:
            print("NameError")
        except ValueError:
            print("ValueError")
        except TypeError:
            print("TypeError")
        else:
            #print("no errors value: "+str(num))
            counter=_MAXTRYLIMIT
    hypotenuusa = math.sqrt(kateetti1**2 + kateetti2**2)
    print ("hypotenuusen pituus on = " , hypotenuusa)
    print("laskettu h=", hypotenuusa)
#def vaikea() ends

if __name__ == "__main__":
#    helppo()
    normaali()
#    vaikea()
