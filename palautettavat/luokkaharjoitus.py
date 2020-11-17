#! /usr/bin/python3
# -*- coding: utf-8 -*-
#Luokka harjoitus
"""

class Ensimmainen_luokkani:

    x = 2


luokka_objekti = Ensimmainen_luokkani()

print(luokka_objekti.x)

#print(dir(luokka_objekti))


luokka_objekti.x = 4


print(luokka_objekti.x)

"""

class Robotti:

    def __init__(self, valmistaja, malli, paino, vapausasteet):

        self.valmistaja = valmistaja

        self.malli = malli

        self.paino = paino

        self.vapausasteet = vapausasteet


    def tulosta_ominaisuus(self, ominaisuus):

        print(ominaisuus)

        if ominaisuus == "valmistaja":

            print(self.valmistaja)

        elif ominaisuus == "malli":

            print(self.malli)

        elif ominaisuus == "paino":

            print(self.paino)

        elif ominaisuus == "vapausasteet":

            print(self.vapausasteet)

        elif ominaisuus == "kaikki":

            print(self.valmistaja)

            print(self.malli)

            print(self.paino)

            print(self.vapausasteet)

        else:

            print("ei kelvollinen ominaisuus")


if __name__ == "__main__":

    robotit = {}


    robotit["robotti1"] = Robotti("Universal robots", "ur5", "20", "7")

    #robotit["robotti1"].tulosta_ominaisuus("valmistaja")


    while True:

        action = input("mita tehdaan ")


        if action == "uusi":

            uusi_robotti_nimi = input("uuden robotin nimi ")

            uusi_robotti_valmistaja = input("uuden robotin valmistaja ")

            uusi_robotti_malli = input("uuden robotin malli ")

            uusi_robotti_paino = input("uuden robotin paino ")

            uusi_robotti_vapausateet = input("anna uuden robotin vapausasteet ")

            robotit[uusi_robotti_nimi] = Robotti(uusi_robotti_valmistaja, uusi_robotti_malli, uusi_robotti_paino, uusi_robotti_vapausateet)


        elif action == "listaa":

            print("lista roboteista:")

            for x in robotit:

                print(x)


        elif action == "lopeta":

            break


        else:

            print("komentoa ei loytynyt")


"""

helppo: lisaa ohjelmaan mahdollisuus kysya robotin yksittainen tieto, yksittaiselta robotilta


normaali: sama kuin helppo, lisaksi luokkaan tieto tarttujasta, tee myos muuten tarvittavat muutokset

etta voit lisata uuden robotin tarttujalla.


Vaikea: lisaa mahdollisuus tallentaa kaikki robotit, ja niiden tiedot tietokanta.csv tiedostoon. 

Ja kun ohjelma kaynnistetaan ladataan tasta tiedostosta robotit ohjelmaan.


"""