import os;
import re;
import mido;
from music21 import *;
from conversion import note_to_number;
from csv_convert import write_to_csv;

sample = [[53, 44, 37, 25], [56, 36, 39, 32], [46, 49, 41, 22], [61, 54, 34, 30]];

note_mapping = {
        'C0': 1, 'C#0': 2, 'Db0': 2, 'D0': 3, 'D#0': 4, 'Eb0': 4,
        'E0': 5, 'Fb0': 5, 'E#0': 6, 'F0': 6, 'F#0': 7, 'Gb0': 7,
        'G0': 8, 'G#0': 9, 'Ab1': 9, 'A1': 10, 'A#1': 11, 'Bb1': 11, 'B1': 12,
        
        'C1': 13, 'C#1': 14, 'Db1': 14, 'D1': 15, 'D#1': 16, 'Eb1': 16,
        'E1': 17, 'Fb1': 17, 'E#1': 18, 'F1': 18, 'F#1': 19, 'Gb1': 19,
        'G1': 20, 'G#1': 21, 'Ab2': 21, 'A2': 22, 'A#2': 23, 'Bb2': 23, 'B2': 24,
        
        'C2': 25, 'C#2': 26, 'Db2': 26, 'D2': 27, 'D#2': 28, 'Eb2': 28,
        'E2': 29, 'Fb2': 29, 'E#2': 30, 'F2': 30, 'F#2': 31, 'Gb2': 31,
        'G2': 32, 'G#2': 33, 'Ab3': 33, 'A3': 34, 'A#3': 35, 'Bb3': 35, 'B3': 36,
        
        'C3': 37, 'C#3': 38, 'Db3': 38, 'D3': 39, 'D#3': 40, 'Eb3': 40,
        'E3': 41, 'Fb3': 41, 'E#3': 42, 'F3': 42, 'F#3': 43, 'Gb3': 43,
        'G3': 44, 'G#3': 45, 'Ab4': 45, 'A4': 46, 'A#4': 47, 'Bb4': 47, 'B4': 48,
        
        'C4': 49, 'C#4': 50, 'Db4': 50, 'D4': 51, 'D#4': 52, 'Eb4': 52,
        'E4': 53, 'Fb4': 53, 'E#4': 54, 'F4': 54, 'F#4': 55, 'Gb4': 55,
        'G4': 56, 'G#4': 57, 'Ab5': 57, 'A5': 58, 'A#5': 59, 'Bb5': 59, 'B5': 60,
        
        'C5': 61, 'C#5': 62, 'Db5': 62, 'D5': 63, 'D#5': 64, 'Eb5': 64,
        'E5': 65, 'Fb5': 65, 'E#5': 66, 'F5': 66, 'F#5': 67, 'Gb5': 67,
        'G5': 68, 'G#5': 69, 'Ab6': 69, 'A6': 70, 'A#6': 71, 'Bb6': 71, 'B6': 72
    }


reverse_map = {v: k for k, v in note_mapping.items()}

mapped = [[reverse_map.get(number, number) for number in sub_array] for sub_array in sample];

print(mapped);













##################################################################
s = stream.Stream()

# Set time signature to 4/4
s.append(meter.TimeSignature('4/4'))

# Iterate over the nested arrays
for chord_notes in mapped:
    # Create a music21 chord from the note names
    c = chord.Chord(chord_notes)
    # Set the duration of the chord to a whole note (1 bar in 4/4 time)
    c.duration.type = 'whole'
    # Add the chord to the stream
    s.append(c)

# Export the stream to a MIDI file
s.write('midi', fp="output.mid");