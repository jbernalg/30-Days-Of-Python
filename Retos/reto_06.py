'''
 Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
'''
from PIL import Image
import requests, math
from io import BytesIO

def get_aspect_ratio(image_url):
    img_content = requests.get(image_url).content
    try:
        image = Image.open(BytesIO(img_content)) # creamos un objeto image de la imagen de la URL
        width, height = image.size  # obtenemos el ancho y alto del objeto image
        greatest_common_division = math.gcd(width,height)   # obtenemos el maximo comun divisor de ambos valores
        pct_height = height/greatest_common_division    # obtenemos la proporcion de la altura
        pct_width = width/greatest_common_division      # obtenemos la proporcion del ancho
        print(f'La relacion de la imagen es {round(pct_height)}:{round(pct_width)}')
        
    except Exception:
        print('La URL no tiene una imagen valida') 

get_aspect_ratio('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')
