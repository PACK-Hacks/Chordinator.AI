import os;
import mido;
from music21 import *;

print ('asdf');
# Read the MIDI file
midi = converter.parse('midi/test.mid');

chords = []
for element in midi.recurse():
    if isinstance(element, chord.Chord):
        chords.append(element);






pro_chords = [];

for i in range(len(chords)):
    pro_chord = [];
    
    for j in range(len(chords[i])):
        pro_chord.append(chords[i][j].nameWithOctave);
    
    pro_chords.append(pro_chord);


print(chords, "\n");
print(pro_chords)