import os
import re
import mido
from music21 import *
from conversion import note_to_number
from csv_convert import write_to_csv

def output_midi(midi):

    note_mapping = {
            "C0" : 1, "D0" : 2, "E0" : 3, "F0" : 4, "G0" : 5, "A1" : 6, "B1" : 7,
            "C1" : 8, "D1" : 9, "E1" : 10, "F1" : 11, "G1" : 12, "A2" : 13, "B2" : 14,
            "C2" : 15, "D2" : 16, "E2" : 17, "F2" : 18, "G2" : 19, "A3" : 34, "B3" : 35,
            "C3" : 22, "D3" : 23, "E3" : 24, "F3" : 25, "G3" : 26, "A4" : 27, "B4" : 28,
            "C4" : 29, "D4" : 30, "E4" : 31, "F4" : 32, "G4" : 33, 
            "C5" : 36, "D5" : 37, "E5" : 38, "F5" : 39, "G5" : 40, "A6" : 41, "B6" : 42
         
        }

    reverse_map = {v: k for k, v in note_mapping.items()}

    mapped = [[reverse_map.get(number, number) for number in sub_array] for sub_array in midi]

    print(mapped)

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
    s.write('midi', fp="Chordinator.AI/chordinator-ai/public/output2.mid")
    return s.write('midi');