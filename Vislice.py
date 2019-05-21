import bottle
import model

vislice = model.Vislice()


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

@bottle.post('/igra/')
def nova_igra():
    #naredi novo igro
    id_igre = vislice.nova_igra()
    # Preusmeri na nalsov za iranje nove igre
    (nova_igra, poskus) = vislice.igre[id_igre]
    bottle.redirect('/igra/{}/'.format(id_igre))
    return bottle.template('igra.tpl', igra=nova_igra)



@bottle.get('/igra/<id_igre:int>/')
def prikazi_igro(id_igre):
    (igra, poskus ) = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, id_igre=id_igre, poskus=poskus)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj_crko(id_igre):
    crka = bottle.request.forms.getunicode('poskus')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))


bottle.run(debug=True, reloader=True)