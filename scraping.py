import requests
from bs4 import BeautifulSoup  


#conexion con la url y obtencion de la informacion de la pagina
url="https://www.facebook.com/victorfcovillarrealatila/posts"
peticion=requests.get(url)
soup=BeautifulSoup(peticion.content,'lxml')


#TWITTER



#FACEBOOK


#obtener post de facebook de la primera pagina
cont=0
for post in soup.find_all('div',class_="_1dwg _1w_m _q7o"):
    print(post.text)
  
'''
#obtener las horas de las ultimas publicaciones
for horas_ultimas_publicaciones in soup.find_all('span',class_="timestampContent"):
    print(horas_ultimas_publicaciones.text)

#obtener nombre red social facebook
for nombre in soup.find_all('span',class_="_81gf"):
    print(nombre.text)


#obtener likes de pagina de facebook
for likes in soup.find_all('span',class_="_52id _50f5 _50f7"):
    print(likes.text)

#obtener pagina web de pagina de facebook
for web in soup.find('a',rel="nofollow"):
    print(web.text)

#obtener paginas relacionadas
for paginas in soup.find_all('',class_="profileLink"):
    print(paginas.text)
    '''


    