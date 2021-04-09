"""
Piano = Multiple octaves
1 Octave = 7 White keys  + 5 Blck keys

White keys: C, D, E, F, G, A, B
Black Key: Flat(b), Sharp(#) {Realtive to white keys}

Understand waves: Mathematical aspect
y = A sin(wt - kx)
w = Angular frequency = 2.pi.f
k = Wave number = 2.pi./lamda

y = A sin (wt) 
y(f) = A sin(2.pi.f.t)

Equal Temperament System: note_freq = base_freq * 2 ** (n/12)
"""

import numpy as np #pip install numpy
from scipy.io.wavfile import write #pip install scipy

sample_rate = 44100 #Hz

def get_wave(freq, duration=0.5):
    amplitude = 4096
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave

def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 261.63

    note_freqs = {octave[i]:base_freq*pow(2, (i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0

    return note_freqs

def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)

    return song.astype(np.int16)


def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()

    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)

    chord_data = np.concatenate(chord_data, axis = 0)

    return chord_data.astype(np.int16)

if __name__ == '__main__':
    music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
    data = get_song_data(music_notes)
    data = data * (16300/np.max(data))

    write('song.wav', sample_rate, data.astype(np.int16))

    chords = 'EgB-DfA-AcE-BDf-gAcE-fAc'
    data = get_chord_data(chords)
    data = data * (16300/np.max(data))
    data = np.resize(data, (len(data)*5,))
    
    write('chords.wav', sample_rate, data.astype(np.int16))
