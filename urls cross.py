# -*- encode: utf-8 -*-
import urllib2 as url
# from bs4 import BeautifulSoup as bs
from pyquery import PyQuery as pq
import sys

hed = {'User-Agent': 'Mozilla/23.0'}

sitio1 = "http://en.wikipedia.org/wiki/Category:Turn-based_tactics_video_games"
# sitio2 = "http://www.wikipedia.org/wiki/List_of_PlayStation_games"
sitio3 = "http://en.wikipedia.org/wiki/Category:Turn-based_strategy_video_games"
sitio4 = "http://en.wikipedia.org/wiki/Category:Tactical_role-playing_video_games"
sitio5 = "http://en.wikipedia.org/wiki/Category:PlayStation_games"
sitio6 = "http://en.wikipedia.org/wiki/Category:Role-playing_video_games"
sitio7 = "http://en.wikipedia.org/wiki/Category:PlayStation_2_games"
sitio8 = "http://en.wikipedia.org/wiki/Category:Windows_games"

def Conectar(pagina):
    req = url.Request(pagina, headers=hed)
    pagina = url.urlopen(req)
    pagina = pagina.read()
    # return bs(pagina,"html5lib")
    pagina = pq(pagina)
    # print(pagina)
    # sys.exit()
    return pagina


def Categoria(sitio1):

    pagina = Conectar(sitio1)

    next = False

    try:
        # next = pagina.find('div','mw-content-ltr')
        next = pq('div.mw-content-ltr',pagina)('a')
        
        # next = next.find_all('a')
        nxt = []
        for item in next:
            nxt.append(item)
        i = nxt.pop()
        # print i.text()
        # sys.exit()
        if(i.text().encode('utf-8') == 'next 200'):
            next = i.filter('href')
            next = "http://en.wikipedia.org" + next

    except:
        pass

    lista = pq('td',pagina)
    # print lista
    # sys.exit()
    lista_sitio = []

    for i in lista:
        sublista = pq('li',i)
        for h in sublista:
            try:
                lista_sitio.append(pq('a',h).text().encode('utf-8'))
            except:
                pass
    # print len(lista_sitio)
    if(next):
        try:
            lista_sitio.extend(Categoria(next))
        except: pass
    return lista_sitio

def Tabla(sitio2):

    pagina = Conectar(sitio2)

    lista = pagina.find('table','wikitable')
    lista = lista.find_all('tr')
    lista_sitio = []

    for i in lista:
        sublista = i.find_all('i')
        # print sublista
        for h in sublista:
            # print h.text.encode('utf-8')
            # print '...................'
            lista_sitio.append(h.text.encode('utf-8'))

    # print lista_sitio

    return lista_sitio

def CompararTyC(pag1, pag2):
    print "Cagando elementos" , "...."
    lista1 = Tabla(pag1)
    print ("La primer lista tiene", len(lista1), "elementos")
    lista2 = Categoria(pag2)
    print ("La segunda lista tiene",len(lista2), "elementos")

    print "Realizando comparacion","...."

    return Comparacion(lista1,lista2)

def CompararCyC(pag1, pag2):
    print "Cagando elementos","...."
    lista1 = Categoria(pag1)
    print("La primer lista tiene " + str(len(lista1)) + " elementos")
    # print lista1
    lista2 = Categoria(pag2)
    print("La segunda lista tiene " + str(len(lista2)) + " elementos")
    # print lista2
    print "Realizando comparacion", "....",

    return Comparacion(lista1,lista2)

def Comparacion(lista1 , lista2):
    respuesta = []
    for item in lista1:
        if(lista2.__contains__(item)):
            respuesta.append(item)
    print "Devolviendo resultado"
    return respuesta

# print CompararTyC(sitio2,sitio1)
# print CompararTyC(sitio2,sitio3)
# a = input("Presione una tecla para finalizar")
# print "holllaaaaa"
resultado = CompararCyC(sitio3,sitio4)
# print resultado
for item in resultado:
    print item
# print "hola"
# a = input("Presione una tecla para finalizar")
# print a
