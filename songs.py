import os
import random
import speak
import editables

def play_english_song():
    path = editables.english_songs

    if not os.path.exists(path):
        speak.speak("The English songs folder does not exist.")
        return

    music = [file for file in os.listdir(path) if file.endswith(('.mp3', '.wav'))]

    if not music:
        speak.speak("No songs found in the English songs folder.")
        return

    song = random.choice(music)
    song_path = os.path.join(path, song)

    speak.speak(f"Playing {song}")
    os.startfile(song_path)

# import os
# import editables
# import random


# def play_song():
#     music = os.listdir(editables.songs)
#     no = random.randint(0, editables.songs_count - 1)
#     os.startfile(os.path.join(editables.songs, music[no]))


# def play_english_song():
#     music = os.listdir(editables.english_songs)
#     no = random.randint(0, editables.english_songs_count - 1)
#     os.startfile(os.path.join(editables.english_songs, music[no]))


# def play_sinhala_song():
#     music = os.listdir(editables.sinhala_songs)
#     no = random.randint(0, editables.sinhala_songs_count - 1)
#     os.startfile(os.path.join(editables.sinhala_songs, music[no]))
