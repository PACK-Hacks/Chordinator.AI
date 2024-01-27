import mido;
from music21 import *;

print ('asdf');
# Read the MIDI file
midi = converter.parse('midi/test.mid');

chords = []
for element in midi.recurse():
    if isinstance(element, chord.Chord):
        chords.append(element);


for chord in chords:
    ()    

print(chords);
print(chords[0][0].nameWithOctave);