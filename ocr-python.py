# Importando a biblioteca de Manipulação de Imagens (Pillow) para abrir a imagem no script
from PIL import Image

# Módulo OCR
import pytesseract

# Define o local da instalação do Tesseract
ts = 'C:/Program Files/Tesseract-OCR/'

# Define executa o Tesseract
pytesseract.pytesseract.tesseract_cmd = ts + 'tesseract.exe'

# Obtem o texto da imagem (troque 'img.jpge' pelo nome e extensão da imagem que for usada)
texto = pytesseract.image_to_string('img.jpeg', lang='por')

# Obtendo o texto da imagem
print(texto)