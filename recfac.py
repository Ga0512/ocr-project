
# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
import pytesseract
import cv2
import pyttsx3

# passo 1: ler a imagem
imagem = cv2.imread("")

caminho = r""
# pedir para tesseract extrair o texto da imagem

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-1].id)

texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)
engine.say(texto)
engine.runAndWait()
