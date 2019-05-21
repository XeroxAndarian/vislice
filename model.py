import random

# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10


PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'w'
PORAZ = 'L'
ZAČETEK = 'B'


# if crka == '+':
#     ...
# spremenimo v boljšo verzijo, saj se tukaj 
# if crka == model.PRAVILNA_CRKA:
#     ...


# Definiramo logični model igre

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() #list
        self.crke = crke #list
        return

    def napacne_crke(self):
        napacne = []
        for i in self.crke:
            if i in self.geslo:
                pass
            else:
                napacne.append(i)
        return napacne

    def pravilne_crke(self):
        pravilne = []
        for i in self.crke:
            if i in self.geslo:
                pravilne.append(i)
            else:
                pass
        return pravilne

    def stevilo_napak(self):        
        return len(self.napacne_crke())


    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
            
        
            

    def zmaga(self):
        for i in self.geslo:
            if i not in self.crke:
                return False
        return True
        
  
        
    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += ' ' + crka
            else:
                niz += ' _'
        niz = niz.strip() #počistimo odvečne presledke 
        return niz

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
        return 

# izluščimo vse slovenske besede

bazen_besed = []

with open("besede.txt", "r", encoding='utf-8') as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)


# Funkcija za generiranje igre
def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])

class Vislice:

    def __init__(self):
        # v slovarju igre ima vsaka igra svoj ID, ki je celo št.
        self.igre = {} 
        return 

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            #preverjamo za keteo od prvih 'n+1' števil še ni uporabljno za ID 'n' iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i

    def nova_igra(self):
        # naredi novo igro z naključnim geslom
        igra = nova_igra()
        nov_id = self.prost_id_igre()

        # shrani v slovar z novim ID
        self.igre[nov_id] = (igra, ZAČETEK)     
        return nov_id

    def ugibaj(self, id_igre, crka):
        # Pridobi igro
        (igra, _ ) = self.igre[id_igre]
        #Ugibaj
        nov_poskus = igra.ugibaj(crka)
        #Shrani rezultat poskusa v slovar
        self.igre[id_igre] = (igra, nov_poskus)
        return
    
