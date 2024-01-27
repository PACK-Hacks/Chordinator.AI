import os;
import re;
import mido;
from music21 import *;
from conversion import note_to_number;
from csv_convert import write_to_csv;


def process_name(s):
    roman_numeral_pattern = r'[IV]+'
    matches = re.findall(roman_numeral_pattern, s)
    processed_string = ' '.join(matches)
    return processed_string

def roman_to_int(roman_string):
    # Dictionary mapping Roman numerals to their integer values
    roman_dict = {'I': 1, 'V': 5}

    # Split the string into individual Roman numerals
    roman_numerals = roman_string.split()

    # Convert Roman numerals to integers
    integer_values = []
    for numeral in roman_numerals:
        integer = 0
        prev_value = 0
        for letter in reversed(numeral):
            value = roman_dict[letter]
            if value < prev_value:
                integer -= value
            else:
                integer += value
            prev_value = value
        integer_values.append(integer)

    return integer_values

progressions = [];
progression_names = [];

for filename in os.listdir('midi'):
    if filename.endswith('.mid') or filename.endswith('.midi'):
        file_path = os.path.join('midi', filename)
        
        midi = converter.parse(file_path)


        ################
        chords = []
    
        for element in midi.recurse():
            if isinstance(element, chord.Chord):
                chords.append(element);


        ################
        if (len(chords) != 4):
            continue; 
        

        progression_names.append(roman_to_int(process_name(filename)));

        ################
        pro_chords = [];
        for i in range(len(chords)):
            pro_chord = [];
            
            for j in range(len(chords[i])):
                pro_chord.append(note_to_number(chords[i][j].nameWithOctave));
            
            pro_chords.append(pro_chord);
    
        progressions.append(pro_chords);

print(write_to_csv(progression_names, progressions, "output.csv"));
