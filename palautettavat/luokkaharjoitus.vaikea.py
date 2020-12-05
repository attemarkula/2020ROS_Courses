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
"moduuli": hallitse ja luo robotin moduuleja
"lopeta" : sammuta robotit ja sulje ohjelma
("testit" : poista robotit, luo testi-robotit ja aja esivalitut testit)

Robotille sallitut ominaisuudet:
"valmistaja", "malli", "paino", "vapausasteet", "kaikki"

ohjelman tehtävä:
- lisaa mahdollisuus tallentaa kaikki robotit, ja niiden tiedot tietokanta.csv tiedostoon. Ja kun ohjelma kaynnistetaan ladataan tasta tiedostosta robotit ohjelmaan.

huomio:
- toteutetaan tallennus ja lataus aina automaattisesti. 
- reset poistamalla tiedosto.
- ei ajeta sanity checkkiä tiedostoon.
"""

import random
class Robotti:
    def __init__(self, valmistaja, malli, paino, vapausasteet):
        self.valmistaja = valmistaja
        self.malli = malli
        self.paino = paino
        self.vapausasteet = vapausasteet
        self.moduulit = []
        print("valmistaja",valmistaja,"teki robotin")

    def teeuusi(self):
        #tää tekee uuden robon ja syöttää sen robottien kirjastoon
        uusi_robotti_nimi = input_unicodesafe("syötä tunniste nimi tai enter :")
        if len(uusi_robotti_nimi) == 0:
            uusi_robotti_nimi = ["robo","ruoste","kevlar","hopea","amalgaami"][random.randint(0,4)]+str(random.randint(1,99))
        uusi_robotti_valmistaja = input_unicodesafe("uuden robotin valmistaja tai enter : ")
        if len(uusi_robotti_valmistaja) == 0:
            uusi_robotti_valmistaja = ["robotron","ruostemaja","kevlarkylä","hopeakulma","amalgaaminatiooni"][random.randint(0,4)]
        uusi_robotti_malli = input_unicodesafe("uuden robotin malli tai enter : ")
        if len(uusi_robotti_malli) == 0:
            uusi_robotti_malli = ["RS","RR","KV","HK","ALI"][random.randint(0,4)]+str(random.randint(1,9))
        uusi_robotti_paino = input_unicodesafe("uuden robotin paino tai enter : ")
        if len(uusi_robotti_paino) == 0:
            uusi_robotti_paino = str(random.randint(1,99))
        uusi_robotti_vapausateet = input_unicodesafe("anna uuden robotin vapausasteet tai enter: ")
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
            print("valmistaja  \t:",self.valmistaja)
            print("malli       \t:",self.malli)
            print("paino       \t:",self.paino)
            print("vapausasteet\t:",self.vapausasteet)
            retval=[self.valmistaja,self.malli,self.paino,self.vapausasteet]
        else:
            print("ei kelvollinen ominaisuus")
            retval=False
        return retval

    def tulosta_tunniste(self,tulostus=True):
        for robonavain in robotit:
            #print("debug tulosta_tunniste:\n"+str(robotit[robonavain])+" ,self:"+str(self))
            if robotit[robonavain] == self:
                break
        if tulostus:
            print ("robotin id:"+robonavain)
        return str(robonavain)

    def moduuli(self, operaatio="noop", optiot=False):
        """
        Moduulien hallinta
        - esimerkkinä tarttujan lisääminen
        """
        robokoukku=self.tulosta_tunniste(False)

        if operaatio == "add":
            #tyyppi=input_unicodesafe("minkä tyyppinen lisälaite:",end="")
            if not optiot:
                tyyppi="tarttuja"
            else:
                tyyppi=str(optiot)
            print("moduuli "+str(tyyppi)+" lisätty.")
            self.moduulit.append(tyyppi)
        elif operaatio == "del":
            if type(optiot) == type(1):
                valittu=optiot
            else:
                self.moduuli_lista()
                input_unicodesafe("mikä laite poistetaan:")
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
        else:
            print("operaatio "+str(operaatio)+" ei ole tuettu")
            return False

    def moduuli_lista(self,tulosta=True):
        if len(self.moduulit) > 0:
            for target_list in self.moduulit:
                if tulosta: 
                    #print("löytyi osuma",end="")
                    print(str(target_list))
            #FIXME Päätä ehkä str() vai oikeen pointteritko? emt.
            return str(self.moduulit)
        else:
            print("lista on tyhjä")
            return False

def import_export_data(operaatio="import"):
    """
    lataa tai tallenna aikaisemmat tiedot
    """
    import csv
    import ast
    global robotit

    if operaatio=="import":
        # Huom. ei välitetä vielä aikaisemmasta datasta, 
        # oletetaan että sitä ei ole.
        robotit = {}

        #print("debug: import data")

        try:
            #lue tiedostoa
            with open('tietokanta.csv', 'r') as csvfile:
                #print("rivi: ",csvfile)
                csvstream=csv.reader(csvfile)
                #print(csvstream)
                
                i=j=0
                for target_item in csvstream:
                    i+=1
                    #print (target_item)
                    if i==1:
                        #expect header, maybe detect sequence
                        header=target_item
                        continue
                    else:
                        j+=1
                        (robotin_nimi,imp_valmistaja,imp_malli,imp_paino,imp_vapausasteet,imp_moduuli) = target_item
                        robotit[robotin_nimi] = Robotti(imp_valmistaja,imp_malli,imp_paino,imp_vapausasteet)

                        #imp_moduuli luetaan tiedostosta stringinä, muutetaan nyt listaksi.
                        imp_moduuli_str = imp_moduuli
                        imp_moduuli = ast.literal_eval(imp_moduuli_str)

                        k=0
                        for moduuli_item in imp_moduuli:
                            k+=1
                            #print("moduuli import, rivi "+str(k)+": \t"+str(type(moduuli_item))+" '"+str(moduuli_item)+"' len:"+str(len(moduuli_item)),end="")
                            str(moduuli_item)
                            if moduuli_item == '[' or moduuli_item == ']' or moduuli_item == "'":
                                continue
                            robotit[robotin_nimi].moduuli("add",moduuli_item)
        except FileNotFoundError as identifier:
            print("Tiedosto puuttuu, käynnistetään ohjelma ilman robotteja. Luo robotteja käsin, tai aja 'testit'")
            #print(identifier)
            #print("esiasetetaan dummy1 koska tiedostoa ei luettu.")
            #robotit["dummy1"] = Robotti("Dumdum Labs", "d01", "56.1", "0")
            #robotit["dummy1"].moduuli("add","laskija i5")
        else:
            i=j=0
            for robonavain in robotit:
                #print (str(robonavain))
                i+=1
                for moduulit_target in robotit[robonavain].moduulit:
                    #print ("löytyi ",end="")
                    #print (moduulit_target)
                    j+=1
            print("luettu sisään "+str(i)+" robottia ja "+str(j)+" moduulia")
        finally:
            #print("debug: lukeminen tiedostosta loppu.")
            pass
    elif operaatio == "export":
        #print("debug:export data")
        i=j=0
        for robonavain in robotit:
            i+=1
            #print ("robotti:"+str(robonavain))
            #robotit[robonavain].tulosta_tunniste()
            #print(str(i)+" Robootti löytyi.")
            for moduulit_target in robotit[robonavain].moduulit:
                #print ("moduuli: ",end="")
                #print (moduulit_target)
                j+=1
        
        if i==j==0:
            print("Ei löydetty robotteja, ei tallenneta tietokantaa.")
        else:
            print("tallennetaan yhteensä ",str(i)," roboottia ja ",str(j)," moduulia")

        #print(robotit[robonavain].moduuli_lista(False))
        with open('tietokanta.csv', 'w') as csvfile:
            fieldnames = ['robotti', 'valmistaja', 'malli', 'paino', 'vapausasteet', 'moduuli']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for exportrobotti in robotit:
                #print(exportrobotti+": ")
                #print(
                #    'robotti', str(robotit[exportrobotti].tulosta_tunniste(False)),
                #    'valmistaja', str(robotit[exportrobotti].valmistaja),
                #    'malli', str(robotit[exportrobotti].malli),
                #    'paino', str(robotit[exportrobotti].paino),
                #    'vapausasteet', str(robotit[exportrobotti].vapausasteet), 
                #    'moduuli', str(robotit[exportrobotti].moduulit),
                #    sep=", ")
                writer.writerow({
                    'robotti': str(robotit[exportrobotti].tulosta_tunniste(False)),
                    'valmistaja': str(robotit[exportrobotti].valmistaja),
                    'malli': str(robotit[exportrobotti].malli),
                    'paino': str(robotit[exportrobotti].paino),
                    'vapausasteet': str(robotit[exportrobotti].vapausasteet),
                    'moduuli': str(robotit[exportrobotti].moduulit)
                    })
        pass
    elif operaatio == "verify":
        #FIXME one day
        pass
    else:
        print("No tätä on vähän vaikea selittää, robokoira on syönyt datan")
    
def input_unicodesafe(kysymys="", forcetype=False):
    """ Lue ja korjaa yleiset pikkuvirheet.
    Tarkasta kysymyksen vastauksen tyyppi
    poista vastauksista UTF-8 kirjaimet, selkeyden vuoksi.
    """
    import unicodedata
    #vastaus="öäåÖÅÄ€"
    #vastaus=input()
    vastaus_ok=False
    while vastaus_ok == False:
        if forcetype=="string" or forcetype==False:
            try:
                vastaus=input(kysymys)
                vastaus=unicodedata.normalize('NFKD', vastaus).encode('ascii', 'ignore')
                vastaus=vastaus.decode("ascii")
            except ValueError as identifier:
                print("syöttövirhe")
            else:
                vastaus_ok=True
        elif(forcetype=="int"):
            try:
                vastaus=int(input(kysymys))
            except ValueError as identifier:
                print("syötevirhe")
            else:
                vastaus_ok=True
    return vastaus

if __name__ == "__main__":
    robotit = {} #oltava ensimmäinen
    #Tähän aikaisempien tietojen lataus
    import_export_data("import")

    valittu_robootti=False
    print(__doc__)
    print()
    print("aputiedot saa näkyviin komennolla help")

    while True:
        if (valittu_robootti==False):
            pass
        else:
            print("("+str(valittu_robootti)+")",end="")
        action = input_unicodesafe("syötä komento: ")
        action = action.lower()
        #print("syötä komento: ",end="")
        #action = input_unicodesafe("")

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
            # valittu_robootti = int(input())
            valittu_robootti = input_unicodesafe("","int")

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
            
            valittu_tietue = input_unicodesafe("valitse mikä näytetään: ","int")
            #int(input("valitse mikä näytetään: "))
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
            operaatio = input_unicodesafe("valitse moduulinumero: ")
            #operaatio=input("valitse moduulinumero: ")
            #enter pois
            #0 lisää
            #numero kohd moduuliin
            if len(operaatio) == 0:
                pass
                continue
            elif operaatio == "0":
                osan_nimi=str(input_unicodesafe("liitettävän osan nimi: "))
                if len(osan_nimi) == 0:
                    osan_nimi = str("virtuaalinen osa")+str(random.randint(10,99))
                robotit[valittu_robootti].moduuli("add", osan_nimi)
            elif 0 < int(operaatio) <= len(robotit[valittu_robootti].moduulit):
                #yhdellä vertailulla, suurempi kuin nolla, pienempi kuin moduulimäärä
                #Thanks LexFridman
                valittu_osa=operaatio
                print("valittu moduuli, valitse mitä tehdään sille.")
                print("FIXME, moduulihallinta")
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

            robotit['ruoste21'] = Robotti("hopeakulma", "RS8", "44", "9")
            robotit['hopea67'] = Robotti("kevlarkylä", "ALI5", "53", "6")
            robotit['kevlar57'] = Robotti("robotron", "ALI1", "99", "9")
            robotit['ruoste51'] = Robotti("ruostemaja", "HK9", "10", "3")

            print("luettele robotit:")
            i = 0
            for x in robotit:
                i+=1
                print(str(i),str(x),sep=": ")

            valittu = robotit['ruoste21']
            valittu.moduuli("add", "vilkkuja")
            print("listaa moduulit robotista "+str(valittu.tulosta_tunniste(False)))
            
            valittu = robotit['hopea67']
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
            #Eli tähän tallennus hook
            #FIXME
            import_export_data("export")
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