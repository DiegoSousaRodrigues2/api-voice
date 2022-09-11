import speech_recognition as sr

r = sr.Recognizer()


def speeach_to_texto(path):
    with sr.AudioFile(path) as source:
        audio = r.record(source)
        return r.recognize_google(audio, language="pt-BR")
