import random

# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10


PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '-'
NAPACNA_CRKA = 'o'
ZMAGA = 'w'
PORAZ = 'L'


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
        return self.stevilo_napak() < STEVILO_DOVOLJENIH_NAPAK
        
  
        
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

