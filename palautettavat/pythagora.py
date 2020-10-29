#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
"""
palautettava työ:

Vaikea: Koodi tarkastaa etta kayttaja on antanut oikean vastauksen, 
mikali ei kysyy uudelleen saman kysymyksen

"""
_MAXTRYLIMIT = 5 #counter max limit
counter=0

while (counter<_MAXTRYLIMIT):
    counter+=1
    print("anna ensimmäinen kateetti:")
    num=input()
    try:
        kateetti1 = int(num)
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
    print("     anna toinen kateetti:")
    num=input()
    try:
        kateetti2 = int(num)
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

