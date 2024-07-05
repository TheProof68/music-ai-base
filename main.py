from transformers import pipeline
from music21 import stream, note
from pydub import AudioSegment
import random
import os

# Pipeline GPT pour l'analyse du texte
generator = pipeline('text-generation', model='gpt-3')

def generate_music_from_text(text):
    # Analyser le texte avec GPT
    analysis = generator(text, max_length=500)
    analyzed_text = analysis[0]['generated_text']

    # Transformer l'analyse en une liste de notes
    def text_to_notes(text_analysis):
        notes = []
        for word in text_analysis.split():
            if 'joy' in word:
                notes.append(note.Note('C4', quarterLength=1))
            elif 'sad' in word:
                notes.append(note.Note('A3', quarterLength=1))
            else:
                notes.append(note.Note(random.choice(['D4', 'E4', 'F4', 'G4', 'B3']), quarterLength=1))
        return notes

    # Créer une partition musicale
    part = stream.Part()
    part.append(text_to_notes(analyzed_text))

    # Exporter en fichier MIDI
    midi_path = 'output.mid'
    part.write('midi', fp=midi_path)

    # Convertir MIDI en audio (MP3)
    sound = AudioSegment.from_file(midi_path, format='mid')
    mp3_path = 'output.mp3'
    sound.export(mp3_path, format='mp3')

    return mp3_path

# Exemple d'utilisation
text = "La beauté du coucher de soleil était saisissante, teintant le ciel de nuances roses et oranges."
mp3_path = generate_music_from_text(text)
print(f"Le fichier MP3 généré se trouve à: {mp3_path}")