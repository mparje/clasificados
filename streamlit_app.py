import streamlit as st
import requests
from bs4 import BeautifulSoup

def buscar_clasificados(palabra_clave):
    url = 'https://www.clasificadospl.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    resultados = []

    for anuncio in soup.find_all('div', class_='c1_adunit'):
        titulo = anuncio.find('div', class_='c1_title').text
        if palabra_clave.lower() in titulo.lower():
            enlace = anuncio.find('a')['href']
            resultados.append({'titulo': titulo, 'enlace': enlace})

    return resultados

st.title('Buscador de Clasificados en Prensa Libre Guatemala')
palabra_clave = st.text_input('Palabra clave')

if st.button('Buscar'):
    resultados = buscar_clasificados(palabra_clave)

    if resultados:
        for resultado in resultados:
            st.write(f"[{resultado['titulo']}]({resultado['enlace']})")
    else:
        st.write('No se encontraron resultados.')
