import speech_recognition as sr
from unidecode import unidecode

r = sr.Recognizer()

# Para Entrega dentro do prazo e ter mais tempo para esquematizar a IA optei por deixar as opções fixas somente para
# entrega da sprint 3

five = ['otimo', 'otima', 'perfeito', 'perfeita', 5, 'cinco']
four = ['bom', 'boa', 'ok', 'satisfatoria', 'legal', 4, 'quatro']
three = ['mais', 'menos', 'mediana', 3, 'tres']
two = ['ruim', 'não foi boa', 'chata', 'chato', 2, 'dois']
one = ['pessimo', 'pessima', 'horrivel', 'odiei', 1, 'um']
stars = (one, two, three, four, five)


def speeach_to_texto(path):
    with sr.AudioFile(path) as source:
        audio = r.record(source)
        stt = r.recognize_google(audio, language="pt-BR")
        rate = rating(stt)
        if rate != 'error':
            return rate, stt


# for para pegar os dados da tupla "stars" e outro for para pegar os dados das listas que tem as palavras chave
# dentro da tupla
def rating(stt):
    for key in stars:
        for value in key:
            if value in unidecode(stt):
                return stars.index(key) + 1
    return "error"

