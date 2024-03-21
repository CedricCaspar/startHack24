import json
import os

from openai import OpenAI


def create_advanced_chat(text):

    client = OpenAI(
        api_key='',  # OPENAI KEY
    )

    completion = client.chat.completions.create(

        messages=[
            {"role": "user",
             "content": "Ich möchte ein Elterngespräch vorbereiten. Angefügt findest du Lernziele und wie gut diese vom Kind erfüllt wurden zwischen 1-4: " + text},
            {"role": "assistant",
             "content": "Spannend, Ich habe erkannt, dass die Struktur der Lernziele wie folgt aussieht: Lernziel: Wert (1-4). Was soll ich damit machen?"},
            {"role": "user",
             "content": "Bereite einige Absätze als Vorbereitung für das Gespräch vor."
                        "Als erstes eine Zusammenfassung über was für Themengebiete das Kind in Deutsch und in Mathematik angeschaut hat"
                        "Als zweites erstelle eine Zusammenfassung wo es besonders erfolgreich war und hebe einige Höhepukte herbor"
                        "Als drittes erstelle eine Beschreibungen der Herausforderungen für das Kind und mache auch ein paar Vorschläge, wie wir gemeinsam mit den Eltern diese Themen verbessern könnten"
                        "Erstelle zudem einen Leitfaden Einen Ablauf für das Gespräch mit der Struktur: Einführung, Rückblick, Ausblick, Offene Fragen"}
        ],

        model="gpt-3.5-turbo",
        temperature=0.8
    )


    print(dict(completion).get('usage'))
    data = json.loads(completion.model_dump_json(indent=2))


    return data["choices"][0]["message"]['content']



