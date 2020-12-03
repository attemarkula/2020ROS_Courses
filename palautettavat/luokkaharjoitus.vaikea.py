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
"moduuli": hallitse robotin moduuleja
"lopeta" : sammuta robotit ja sulje ohjelma
("testit" : aja esivalitut testit)

Robotille sallitut ominaisuudet:
"valmistaja", "malli", "paino", "vapausasteet", "kaikki"

ohjelman tehtävä:
- lisaksi luokkaan tieto tarttujasta, tee myos muuten tarvittavat muutokset etta voit lisata uuden robotin tarttujalla.
huomio:
- lisätty tarttuja "moduulina", jotta mahdollista useampaan.
"""

import random
class Robotti:
    def __init__(self, valmistaja, malli, paino, vapausasteet):
        self.valmistaja = valmistaja
        self.malli = malli
        self.paino = paino
        self.vapausasteet = vapausasteet
        self.moduulit = []

    def teeuusi(self):
        #tää tekee uuden robon ja syöttää sen robottien kirjastoon
        uusi_robotti_nimi = input("syötä tunniste nimi tai enter :")
        if len(uusi_robotti_nimi) == 0:
            uusi_robotti_nimi = ["robo","ruoste","kevlar","hopea","amalgaami"][random.randint(0,4)]+str(random.randint(1,99))
        uusi_robotti_valmistaja = input("uuden robotin valmistaja: ")
        if len(uusi_robotti_valmistaja) == 0:
            uusi_robotti_valmistaja = ["robotron","ruostemaja","kevlarkylä","hopeakulma","amalgaaminatiooni"][random.randint(0,4)]
        uusi_robotti_malli = input("uuden robotin malli: ")
        if len(uusi_robotti_malli) == 0:
            uusi_robotti_malli = ["RS","RR","KV","HK","ALI"][random.randint(0,4)]+str(random.randint(1,9))
        uusi_robotti_paino = input("uuden robotin paino: ")
        if len(uusi_robotti_paino) == 0:
            uusi_robotti_paino = str(random.randint(1,99))
        uusi_robotti_vapausateet = input("anna uuden robotin vapausasteet: ")
        if len(uusi_robotti_vapausateet) == 0:
            uusi_robotti_vapausateet = random.randint(1,10)
        robotit[uusi_robotti_nimi] = Robotti(uusi_robotti_valmistaja, uusi_robotti_malli, uusi_robotti_paino, uusi_robotti_vapausateet)
    #def teeuusi

    def tulosta_ominaisuus(self, ominaisuus):
        print("tietokenttä:"+str(ominaisuus))
        if ominaisuus == "valmistaja":
            print(str(ominaisuus)+"sisältö on "+str(self.valmistaja))
            retval=self.valmistaja
        elif ominaisuus == "malli":
            print(str(ominaisuus)+"sisältö on "+str(self.malli))
            retval=self.malli
        elif ominaisuus == "paino":
            print(str(ominaisuus)+"sisältö on "+str(self.paino))
            retval=self.paino
        elif ominaisuus == "vapausasteet":
            print(str(ominaisuus)+"sisältö on "+str(self.vapausasteet))
            retval=self.vapausasteet
        elif ominaisuus == "kaikki":
            print("kaikki kentät ovat:")
            print(self.valmistaja)
            print(self.malli)
            print(self.paino)
            print(self.vapausasteet)
            retval=[self.valmistaja,self.malli,self.paino,self.vapausasteet]
        else:
            print("ei kelvollinen ominaisuus")
            retval=False
        return retval

    def tulosta_tunniste(self,tulostus=True):
        if tulostus:
            print ("robotin id:",end="")
        for robonavain in robotit:
            if robotit[robonavain] == self:
                break
        return str(robonavain)

    def moduuli(self, operaatio="noop", optiot=False):
        """
        lisää moduuli, esimerkkinä tarttujan lisääminen
        """
        #print("debug moduuli ",operaatio, optiot ,sep=", ")
        robokoukku=self.tulosta_tunniste(False)
        if operaatio == "add":
            #tyyppi=input("minkä tyyppinen lisälaite:",end="")
            if not optiot:
                tyyppi="tarttuja"
            else:
                tyyppi=str(optiot)
            print("moduuli "+str(tyyppi)+" lisätty.")
            self.moduulit.append(tyyppi)
            pass
        elif operaatio == "del":
            if type(optiot) == type(1):
                valittu=optiot
            else:
                self.moduuli_lista()
                input("mikä laite poistetaan:")
            #print("poistetaan moduuli", self.moduulit[valittu-1], "numero:"+str(valittu), sep=" , ")
            print("moduuli "+str(self.moduulit[valittu-1])+" poistettu.")
            self.moduulit.remove(self.moduulit[valittu-1])
        elif operaatio == "list":
            i=0
            for target_list in self.moduulit:
                i += 1
                print(i,str(target_list),sep=": ")

        elif operaatio == "noop":
            print("no operation")
            pass
        else:
            print("FIXME: operaatio "+str(operaatio)+" ei ole tunettu")
            return False

    def moduuli_lista(self,tulosta=True):
        if len(self.moduulit) > 0:
            for target_list in self.moduulit:
                if tulosta: 
                    print("löytyi osuma",end="")
                    print(str(target_list))
            #FIXME Päätä ehkä str() vai oikeen pointteritko? emt.
            return str(self.moduulit)
        else:
            print("lista on tyhjä")
            return False
        pass

if __name__ == "__main__":
    print("aputiedot saa näkyviin komennolla help")

    robotit = {}
    robotit["robotti1"] = Robotti("Universal robots", "ur5", "20", "7")
    robotit["robotti2"] = Robotti("Global robots", "gb9", "50", "2")
    #robotit["robotti2"].moduuli("add","laskija i5")
    #kommentoitu, koska lisääminen aiheuttaa ilmoituksen.
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
            Robotti.teeuusi(True)
        elif action == "listaa":
            print("lista roboteista: ")
            for x in robotit:
                print(x)

        elif action == "vaihda" or action == "valitse":
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
                i=0
                for robonavain in robotit:
                    i+=1
                    if valittu_robootti == i:
                        valittu_robootti = robotit[robonavain]
                        break
                #print("löysin että i="+str(i)+" ja että robotti on "+str(valittu_robootti.tulosta_tunniste(False)))
                valittu_robootti=valittu_robootti.tulosta_tunniste(False)
        elif action == "tieto":
            if not valittu_robootti:
                print("valitse robotti ensin")
                continue
            i=0
            for x in ["kaikki","valmistaja","malli","paino","vapausasteet"]:
                print (i,x,sep=": ")
                i+=1                
            
            valittu_tietue = int(input("valitse mikä näytetään: "))
            if valittu_tietue == 0:
                tieto=robotit[valittu_robootti].tulosta_ominaisuus("kaikki")
            elif valittu_tietue == 1:
                tieto=robotit[valittu_robootti].tulosta_ominaisuus("valmistaja")
            elif valittu_tietue == 2:
                tieto=robotit[valittu_robootti].tulosta_ominaisuus("malli")
            elif valittu_tietue == 3:
                tieto=robotit[valittu_robootti].tulosta_ominaisuus("paino")
            elif valittu_tietue == 4:
                print(robotit[valittu_robootti].tulosta_ominaisuus("vapausasteet"))
            else:
                print("FIXME: tuntematon kenttätieto")
        elif action == "moduuli":
            if not valittu_robootti:
                print("valitse robotti ensin")
                continue
            
            print("enter: poistuu päävalikkoon")
            print("0: lisää uusi moduuli")
            robotit[valittu_robootti].moduuli("list", True)
            valittu_robootti
            operaatio=input("valitse moduulinumero: ")
            #enter pois
            #0 lisää
            #numero kohd moduuliin
            if len(operaatio) == 0:
                continue
                pass
            elif operaatio == "0":
                osan_nimi=str(input("liitettävän osan nimi: "))
                if len(osan_nimi) == 0:
                    osan_nimi = str("virtuaalinen osa")+str(random.randint(10,99))
                robotit[valittu_robootti].moduuli("add", osan_nimi)
            elif 0 < int(operaatio) < len(robotit[valittu_robootti].moduulit):
                #yhdellä vertailulla, suurempi kuin nolla, pienempi kuin moduulimäärä
                #Thanks LexFridman
                valittu_osa=operaatio
                print("valittu moduuli, valitse mitä tehdään sille.")
                print("FIXME, moduulihallinta")
                pass
            else:
                print("Tuntematon kenttätieto: ",str(operaatio))
        elif action == "testit":
            #aja jonkinnäköiset testit
            print("luettele robotit:")
            i = 0
            for x in robotit:
                i+=1
                print(str(i),str(x),sep=": ")
            print("lista loppui")
            print("poista robotit")
            robotit = {}
            print("luettele robotit:")
            i = 0
            for x in robotit:
                i+=1
                print(str(i),str(x),sep=": ")
            print("lista loppui")

            robotit['testi1robotti'] = Robotti("Testi1robotti", "a1", "10", "1")
            robotit['testi2robotti'] = Robotti("Testi2robotti", "a2", "20", "2")
            robotit['testi3robotti'] = Robotti("Testi3robotti", "z3", "99", "0")
            print("luettele robotit:")
            i = 0
            for x in robotit:
                i+=1
                print(str(i),str(x),sep=": ")

            valittu = robotit['testi2robotti']
            print("listaa moduulit robotista "+str(valittu.tulosta_tunniste(False)))
            valittu.moduuli("add", "tarttuja")
            valittu.moduuli("add", "vilkkuja")
            valittu.moduuli("add", "röhkijä")

            print("listaa moduulit robotista "+str(valittu.tulosta_tunniste(False)))
            valittu.moduuli("list", True)
            valittu.moduuli("del", 2)
            
            print("listaa moduulit robotista "+str(valittu.tulosta_tunniste(False)))
            valittu.moduuli("list", True)
   
            print ("testit ajettu loppuun, huomaa että robotit jätetään listaan.")
        elif action == "lopeta" or action == "lo":
            break
        else:
            print("komentoa '"+str(action)+"' ei tunnettu, kirjoita help")

"""
helppo: lisaa ohjelmaan mahdollisuus kysya robotin
 yksittainen tieto, yksittaiselta robotilta

normaali: sama kuin helppo, 
lisaksi luokkaan tieto tarttujasta, 
tee myos muuten tarvittavat muutokset
etta voit lisata uuden robotin tarttujalla.

Vaikea: lisaa mahdollisuus tallentaa kaikki robotit, 
ja niiden tiedot tietokanta.csv tiedostoon. 
Ja kun ohjelma kaynnistetaan ladataan 
tasta tiedostosta robotit ohjelmaan.

"""