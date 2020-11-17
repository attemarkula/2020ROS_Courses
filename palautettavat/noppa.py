#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

if False:
    noppa_d100 =[i for i in range(1, 101)]
    print(noppa_d100)
    print(random.choice(noppa_d100))
    print(noppa_d100[random.randrange(100)])

def nopantahot(tahomaara=0):
    """ palauta tahomäärän mukaiset nopan silmäluvut listana """
    #print("nopantahot("+str(tahomaara)+")")
    lista=[]

    for target_list in range(tahomaara):
        lista.append(1+target_list)
    #print(lista)
    return lista

def noppa(tahomaara):
    """
    palauta satunnainen nopan silmäluku
    """
    #print("noppa("+str(tahomaara)+"):",end="")
    
    vastaus=1+random.randrange(tahomaara)
    #print(vastaus)
    return vastaus









def helppo(mode="print"):
    if mode=="print":
        print("""
        helppo:
        Kysy kauttajalta kuinka monta tahoista noppaa kayttaja haluaa heittaa.
        Tee funtio joka ottaa sisaansa tahojen lukumaaran ja palauttaa listan jossa on nopan silmaluvut.
        Anna satunnainen nopantulos printtaamalla se kayttajalle.
        """)
    tahot=int(input('Montako tahoa nopassa:'))
    #tahot=6
    tahot_lista=nopantahot(tahot)
    np=noppa(tahot)
    #print ("lista silmäluvuista:"+str(tahot_lista))
    #kommentoitu, koska ei pyydetty tulostamaan
    print ("nopan tulos:"+str(np))
#def helppo(mode) ends












def normaali(mode="print"):
    if mode=="print":
        print ("""
        normaali
        sama kuin normaali, mutta kysy kuinka monta noppaa kayttaja haluaa heittaa, ja printtaa
        noppien tulos erikseen ja summana
        """)
    
    nopatlkm=int(input('Montako noppaa:'))
    #nopatlkm=15
    tahot=int(input('Montako tahoa nopassa:'))
    #tahot=100

    lista=[]
    summa=0

    for i in range(nopatlkm):
        lista.append(noppa(tahot))
        summa+=lista[i]

    print("summa:"+str(summa)+", silmäluvut: ",end="")
    print (lista)
#def normaali(mode) ends









#Huom: Vaikea halutaan toteuttaa luokkien avulla
def vaikea(mode="print"):
    if mode=="print":
        print("""
#vaikea
Sama kuin normaali, mutta tuloksen jalkeen kysy kayttajalta halutaanko heittaa uudelleen.
entterilla uusi heitto
muuta noppa kysyy uudelleen tahot
muuta noppien lukumaara kysyy noppaluvun uudelleen
lopeta lopettaa ohjelman
""")

    loop=True
    loopcounter=0
    nopatlkm=0
    vaihda_tahot=True
    vaihda_nopat=True
    komento=False
    uusikierros=False

    while loop:
        loop=False
        loopcounter+=1
        if loopcounter>20:
            print("liian monta yritystä, pakollinen interventio")
            loop=False
            break

        if vaihda_tahot:
            tahot=int(input('Montako tahoa nopassa:'))
            #tahot=20

        if vaihda_nopat:
            nopatlkm=int(input('Montako noppaa:'))
            #nopatlkm=5

        if vaihda_tahot or vaihda_nopat or uusikierros:
            komento=False
            vaihda_nopat=False
            vaihda_tahot=False
            uusikierros=False
            noppalistaolio = noppalistaluokka()
            for var in range(nopatlkm):
                noppalistaolio.sido(noppaluokka(tahot))
            for var in range(1,noppalistaolio.count+1):
                print(var,noppalistaolio.showone(var-1).katso(), sep=":", end=" ")
            print("")

        # Hymmm. jos komento on "entteri", niin se ei ole False.
        if komento==False:
            print("heitetäänkö uudelleen tai muutetaanko (taho/lukumäärä/lopeta/uudelleen) :",end="")
            komento=input()
            if komento=="": komento="uudelleen"

        if komento:
            komento=komento.lower()
            if (komento=="lopeta"):
                loop=False
                komento=False
            elif (komento=="lukumaara") or (komento=="lukumäärä") or komento=="muuta noppien lukumaara":
                vaihda_nopat=True
                loop=True
                komento=False
            elif (komento=="taho" or komento=="tahot" or komento=="muuta noppa"):
                vaihda_tahot=True
                loop=True
                komento=False
            elif (komento=="uudelleen"):
                loop=True
                vaihda_tahot=False
                vaihda_nopat=False
                uusikierros=True
                komento=False
            else:
                print("komento "+str(komento)+" ei ole tuttu, tarkasta kirjoitusmuoto")
                loop=True
                komento=False
        pass
    pass

        

#def vaikea(mode) ends

class noppaluokka(object):
    """
    luokka mallintaa rajatun sivumäärän nopan
    """
    def __init__(self,tahot):
        """
        constructor
        """
        #print("noppaluokka::__init__(",end="")
        self.tahot = tahot
        self.arvo=1+random.randrange(tahot)
        #print(str(tahot)+")")

    def pudota(self):
        """
        pudota ja näytä silmäluku
        """
        self.arvo = 1+random.randrange(self.tahot)
        #print("pudota:"+str(self.arvo))

    def __del__(self):
        """
        destructor
        """
        #print("noppaluokka::__del__ noppa oli:"+str(self.arvo)+"/"+str(self.tahot))

    def katso(self):
        """
        tulosta nopan arvo
        """
        #print("katso: "+str(self.arvo))
        return self.arvo
    
    def kysy(self, parameter_list):
        """
        kysy tahojen määrä
        """
        self.tahot = int(input('Montako tahoa nopassa:'))
    
    def muutatahot(self,tahot):
        """
        muuta tahojen määrä
        """
        self.tahot = tahot
        return self.tahot
    pass
#class noppaluokka(object)

class noppalistaluokka(object):
    """
    lista useasta nopasta
    """
    def __init__(self):
        """
        luo ja nollaa
        """
        self.count=0
        self.noppalista=[]

    def sido(self,noppa):
        """
        lisää noppa listaan
        """
        self.noppalista.append(noppa)
        self.count+=1
        #print(self.count)

    def vapauta(self,noppaindex):
        """
        free certain noppa from list
        """
        print("vapauta("+str(noppaindex+1)+"/"+str(self.count)+")")
        poisnoppa = self.noppalista.pop(noppaindex)
        self.count-=1

        #huom: noppa tuhoutuu kun ei enää käytössä.
        return poisnoppa

    def showone(self,num):
        """
        palauta pointteri yhteen lueteltuun noppa objektiin
        """
        return self.noppalista[num]
    pass
#class noppalistaluokka(object) ends

def cls():
    """
    tyhjennä terminaali tekstistä
    """
    print(chr(27) + "[2J")
    #escape sequence stringit, eivät ehkä ole ROS1/2 yhteensopivia, mutta ovat noppa yhteensopivia

if __name__ == "__main__":
    cls()    
    print ("")
    #helppo("print")
    #normaali("print")
    vaikea("print")
