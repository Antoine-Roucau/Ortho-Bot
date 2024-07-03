import openai
import pyperclip
from playsound import playsound
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

texteACorriger = pyperclip.paste()

openai.api_key = "xxxx"#Changer clé

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system", "content": """Vous êtes un correcteur orthographique expert. Votre tâche est de :
            1. Corriger les fautes d'orthographe.
            2. Ajuster les mots existants si leur forme ne convient pas au contexte (temps, accord, etc.).
            3. Ne pas modifier le sens général, la structure des phrases ou le vocabulaire choisi.
            4. Ne pas ajouter, supprimer ou remplacer des mots, sauf si c'est nécessaire pour la correction orthographique.
            5. Comparer le sens du texte original à celui du texte corrigé. 
            6. Ajuster en fonction de la comparaison de sens pour être au plus proche du texte original
            Présentez uniquement le texte corrigé sans explications."""
        },
        
        {
            "role": "user", "content": "Corrigez l'orthographe et les formes inappropriées dans ce texte : " + texteACorriger +""
        }
    ]
)

texteCorriger = response.choices[0].message.content

pyperclip.copy(texteCorriger)

path_sound = BASE_DIR + "\correct.mp3"

playsound(path_sound.encode('unicode-escape').decode())

