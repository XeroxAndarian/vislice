import bottle
import model
SKRIVNI_KLJUC = 'Geslo'
vislice = model.Vislice('stanje.json')


# # TA ira je namenjen atestiranju:
# id_testne_igre = vislice.nova_igra()
# (testna_igra, poskus) = vislice.igre[id_testne_igre]
# 
# #dodajmo teste v testno igro:
# vislice.ugibaj(id_testne_igre, 'A')
# vislice.ugibaj(id_testne_igre, 'B')
# vislice.ugibaj(id_testne_igre, 'C')

@bottle.get('/')
def prva_stran():
    return bottle.template('zacetna_stran.tpl')


# @bottle.post('/igra/')
# def prikaz_testne_igre1():
#     return bottle.template('igra.tpl', igra=testna_igra)
# 

# @bottle.get('/igra/')
# def prikaz_testne_igre():
#     return bottle.template('igra.tpl', igra=testna_igra)
# 
# @bottle.get('/igra/<id_igre>/')
# def nova_igra(id_igre):
#     return bottle.template('igra.tpl', id_igre=id_igre)

@bottle.post('/nova_igra/')
def nova_igra():
    #naredi novo igro
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, secret=SKRIVNI_KLJUC, path='/')
    # Preusmeri na nalsov za iranje nove igre
    (nova_igra, poskus) = vislice.igre[id_igre]
    bottle.redirect('/igra/')
    return



@bottle.get('/igra/')
def prikazi_igro():
    id_igre = bottle.request.get_cookie('id_igre',  secret=SKRIVNI_KLJUC)
    (igra, poskus ) = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, id_igre=id_igre, poskus=poskus)

@bottle.post('/igra/')
def ugibaj_crko():
    crka = bottle.request.forms.getunicode('poskus')
    id_igre = bottle.request.get_cookie('id_igre',  secret=SKRIVNI_KLJUC)

    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')

@bottle.post('/odpri_igra/')
def povrni_igro(): 
    zeljeni_id = int(bottle.request.forms.getunicode('id_igre'))
    bottle.response.set_cookie('id_igre', zeljeni_id, secret=SKRIVNI_KLJUC, path='/')
    vislice.nalozi_igre_iz_datoteke()
    bottle.redirect('/igra/')
    return
    




bottle.run(debug=True, reloader=True)