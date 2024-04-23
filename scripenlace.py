import requests
from bs4 import BeautifulSoup
import re

# Función para obtener el enlace "Plain Text UTF-8" de una página de Gutenberg
def obtener_enlace_texto(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscar el enlace que se llama "Plain Text UTF-8"
            enlace_texto = soup.find('a', text='Plain Text UTF-8')
            if enlace_texto:
                return enlace_texto['href']
            else:
                print(f"No se encontró el enlace 'Plain Text UTF-8' en {url}")
                return None
        else:
            print(f"Error al obtener la página: {url}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Función para descargar el archivo de texto de un enlace
def descargar_texto(url, nombre_archivo):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Guardar el archivo con el nombre adecuado
            with open(nombre_archivo + ".txt", 'wb') as f:
                f.write(response.content)
            print(f"Archivo descargado: {nombre_archivo}")
        else:
            print(f"Error al descargar el archivo: {url}")
    except Exception as e:
        print(f"Error: {e}")
# Lista de enlaces
enlaces = [
    "https://www.gutenberg.org/ebooks/84",
    "https://www.gutenberg.org/ebooks/1342",
    "https://www.gutenberg.org/ebooks/2701",
    "https://www.gutenberg.org/ebooks/1513",
    "https://www.gutenberg.org/ebooks/16594",
    "https://www.gutenberg.org/ebooks/145",
    "https://www.gutenberg.org/ebooks/21765",
    "https://www.gutenberg.org/ebooks/2542",
    "https://www.gutenberg.org/ebooks/844",
    "https://www.gutenberg.org/ebooks/2641",
    "https://www.gutenberg.org/ebooks/100",
    "https://www.gutenberg.org/ebooks/37106",
    "https://www.gutenberg.org/ebooks/11",
    "https://www.gutenberg.org/ebooks/2581",
    "https://www.gutenberg.org/ebooks/64317",
    "https://www.gutenberg.org/ebooks/16389",
    "https://www.gutenberg.org/ebooks/5200",
    "https://www.gutenberg.org/ebooks/67979",
    "https://www.gutenberg.org/ebooks/394",
    "https://www.gutenberg.org/ebooks/174",
    "https://www.gutenberg.org/ebooks/6761",
    "https://www.gutenberg.org/ebooks/2160",
    "https://www.gutenberg.org/ebooks/98",
    "https://www.gutenberg.org/ebooks/6593",
    "https://www.gutenberg.org/ebooks/4085",
    "https://www.gutenberg.org/ebooks/1259",
    "https://www.gutenberg.org/ebooks/5197",
    "https://www.gutenberg.org/ebooks/73442",
    "https://www.gutenberg.org/ebooks/1952",
    "https://www.gutenberg.org/ebooks/10681",
    "https://www.gutenberg.org/ebooks/2554",
    "https://www.gutenberg.org/ebooks/47629",
    "https://www.gutenberg.org/ebooks/345",
    "https://www.gutenberg.org/ebooks/1080",
    "https://www.gutenberg.org/ebooks/52862",
    "https://www.gutenberg.org/ebooks/20228",
    "https://www.gutenberg.org/ebooks/25344",
    "https://www.gutenberg.org/ebooks/43",
    "https://www.gutenberg.org/ebooks/73441",
    "https://www.gutenberg.org/ebooks/21700",
    "https://www.gutenberg.org/ebooks/1400",
    "https://www.gutenberg.org/ebooks/219",
    "https://www.gutenberg.org/ebooks/10676",
    "https://www.gutenberg.org/ebooks/19694",
    "https://www.gutenberg.org/ebooks/62091",
    "https://www.gutenberg.org/ebooks/408",
    "https://www.gutenberg.org/ebooks/28556",
    "https://www.gutenberg.org/ebooks/1260",
    "https://www.gutenberg.org/ebooks/38141",
    "https://www.gutenberg.org/ebooks/28054",
    "https://www.gutenberg.org/ebooks/76",
    "https://www.gutenberg.org/ebooks/40438",
    "https://www.gutenberg.org/ebooks/2591",
    "https://www.gutenberg.org/ebooks/46",
    "https://www.gutenberg.org/ebooks/1727",
    "https://www.gutenberg.org/ebooks/1661",
    "https://www.gutenberg.org/ebooks/42059",
    "https://www.gutenberg.org/ebooks/4300",
    "https://www.gutenberg.org/ebooks/2814",
    "https://www.gutenberg.org/ebooks/2000",
    "https://www.gutenberg.org/ebooks/1232",
    "https://www.gutenberg.org/ebooks/47475",
    "https://www.gutenberg.org/ebooks/6130",
    "https://www.gutenberg.org/ebooks/1998",
    "https://www.gutenberg.org/ebooks/768",
    "https://www.gutenberg.org/ebooks/29870",
    "https://www.gutenberg.org/ebooks/996",
    "https://www.gutenberg.org/ebooks/35899",
    "https://www.gutenberg.org/ebooks/2600",
    "https://www.gutenberg.org/ebooks/5740",
    "https://www.gutenberg.org/ebooks/39407",
    "https://www.gutenberg.org/ebooks/73447",
    "https://www.gutenberg.org/ebooks/120",
    "https://www.gutenberg.org/ebooks/62354",
    "https://www.gutenberg.org/ebooks/54023",
    "https://www.gutenberg.org/ebooks/1184",
    "https://www.gutenberg.org/ebooks/67098",
    "https://www.gutenberg.org/ebooks/45",
    "https://www.gutenberg.org/ebooks/3207",
    "https://www.gutenberg.org/ebooks/2852",
    "https://www.gutenberg.org/ebooks/5131",
    "https://www.gutenberg.org/ebooks/27827",
    "https://www.gutenberg.org/ebooks/55",
    "https://www.gutenberg.org/ebooks/16",
    "https://www.gutenberg.org/ebooks/74",
    "https://www.gutenberg.org/ebooks/244",
    "https://www.gutenberg.org/ebooks/24238",
    "https://www.gutenberg.org/ebooks/600",
    "https://www.gutenberg.org/ebooks/30254",
    "https://www.gutenberg.org/ebooks/205",
    "https://www.gutenberg.org/ebooks/23",
    "https://www.gutenberg.org/ebooks/514",
    "https://www.gutenberg.org/ebooks/7370",
    "https://www.gutenberg.org/ebooks/4363",
    "https://www.gutenberg.org/ebooks/33283",
    "https://www.gutenberg.org/ebooks/19926",
    "https://www.gutenberg.org/ebooks/73444",
    "https://www.gutenberg.org/ebooks/3825",
    "https://www.gutenberg.org/ebooks/41445",
    "https://www.gutenberg.org/ebooks/8800"
]

for enlace in enlaces:
    enlace_texto = obtener_enlace_texto(enlace)
    if enlace_texto:
        # Obtener el número de la obra desde la URL
        numero_obra = re.search(r'\d+', enlace).group()
        descargar_texto("https://www.gutenberg.org" + enlace_texto, f"pg{numero_obra}")