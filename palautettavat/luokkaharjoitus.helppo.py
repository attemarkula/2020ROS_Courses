#! /usr/bin/python3
# -*- coding: utf-8 -*-
#Luokka harjoitus
"""
robootti ohjelma

sallitut komennot:
"help"   : näytä tämä aputieto
"uusi"   : lisää uusi robotti
"listaa" : listaa robotit
"vaihda" : vaihda ja valitse robotti
"tieto"  : näytä valitun robotin tietokentän sisältö
"lopeta" : sammuta robotit ja sulje ohjelma

Robotille sallitut ominaisuudet:
"valmistaja", "malli", "paino", "vapausasteet", "kaikki"

ohjelman tehtävä:
- lisaa ohjelmaan mahdollisuus kysya robotin yksittainen tieto, yksittaiselta robotilta

"""
class Robotti:
    def __init__(self, valmistaja, malli, paino, vapausasteet):
        self.valmistaja = valmistaja
        self.malli = malli
        self.paino = paino
        self.vapausasteet = vapausasteet

    def tulosta_ominaisuus(self, ominaisuus):
        print("req:"+str(ominaisuus))
        if ominaisuus == "valmistaja":
            print(self.valmistaja)
            retval=self.valmistaja
        elif ominaisuus == "malli":
            print(self.malli)
            retval=self.malli
        elif ominaisuus == "paino":
            print(self.paino)
            retval=self.paino
        elif ominaisuus == "vapausasteet":
            print(self.vapausasteet)
            retval=self.vapausasteet
        elif ominaisuus == "kaikki":
            print(self.valmistaja)
            print(self.malli)
            print(self.paino)
            print(self.vapausasteet)
            retval=[self.valmistaja,self.malli,self.paino,self.vapausasteet]
        else:
            print("ei kelvollinen ominaisuus")
            retval=False
        return retval

if __name__ == "__main__":
    print("aputiedot saa näkyviin komennolla help")

    robotit = {}
    robotit["robotti1"] = Robotti("Universal robots", "ur5", "20", "7")
    robotit["robotti2"] = Robotti("Global robots", "gb9", "50", "2")
    valittu_robootti=False

    while True:
        
        if (valittu_robootti==False):
            pass
        else:
            print("("+str(valittu_robootti)+")",end="")
        print("syötä komento: ",end="")
        action = input().lower()

        if action == "help":
            print(__doc__)
        elif action == "uusi":
            uusi_robotti_nimi = input("uuden robotin nimi: ")
            uusi_robotti_valmistaja = input("uuden robotin valmistaja: ")
            uusi_robotti_malli = input("uuden robotin malli: ")
            uusi_robotti_paino = input("uuden robotin paino: ")
            uusi_robotti_vapausateet = input("anna uuden robotin vapausasteet: ")
            robotit[uusi_robotti_nimi] = Robotti(uusi_robotti_valmistaja, uusi_robotti_malli, uusi_robotti_paino, uusi_robotti_vapausateet)

        elif action == "listaa":
            print("lista roboteista: ")
            for x in robotit:
                print(x)

        elif action == "vaihda":
            print("lista roboteista:")
            print("0: poista valinta")
            i=0
            for x in robotit:
                i+=1
                print(str(i),str(x),sep=": ")
            print("valitse robotti numerolla:")
            valittu_robootti=int(input())
            #ehkä tähän try catch

            if valittu_robootti==0:
                valittu_robootti=False
            else:
                valittu_robootti=str("robotti")+str(valittu_robootti)
            pass

        elif action == "tieto":
            if not valittu_robootti:
                print("valitse robotti ensin")
                continue
            i=0
            for x in ["valmistaja","malli","paino","vapausasteet"]:
                i+=1
                print (i,x,sep=": ")
            
            valittu_tietue = int(input("valitse mikä näytetään: "))
            if valittu_tietue == 1:
                tieto=robotit[valittu_robootti].tulosta_ominaisuus("valmistaja")
            elif valittu_tietue == 2:
                tieto=robotit[valittu_robootti].tulosta_ominaisuus("malli")
            elif valittu_tietue == 3:
                tieto=robotit[valittu_robootti].tulosta_ominaisuus("paino")
            elif valittu_tietue == 4:
                print(robotit[valittu_robootti].tulosta_ominaisuus("vapausasteet"))
            else:
                print("FIXME: tuntematon kenttätieto")
            
        elif action == "lopeta" or action == "lo":
            break
        else:
            print("komentoa ei loytynyt, kirjoita help")

    