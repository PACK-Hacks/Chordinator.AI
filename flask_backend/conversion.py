#note_num_conversion
def note_to_number(note):
    note_mapping = {
        "C0" : 1, "D0" : 2, "E0" : 3, "F0" : 4, "G0" : 5, "A1" : 6, "B1" : 7,
        "C1" : 8, "D1" : 9, "E1" : 10, "F1" : 11, "G1" : 12, "A2" : 13, "B2" : 14,
        "C2" : 15, "D2" : 16, "E2" : 17, "F2" : 18, "G2" : 19, "A3" : 20, "B3" : 21,
        "C3" : 22, "D3" : 23, "E3" : 24, "F3" : 25, "G3" : 26, "A4" : 27, "B4" : 28,
        "C4" : 29, "D4" : 30, "E4" : 31, "F4" : 32, "G4" : 33, "A5" : 34, "B5" : 35,
        "C5" : 36, "D5" : 37, "E5" : 38, "F5" : 39, "G5" : 40, "A6" : 41, "B6" : 42
        
    }

    # Convert the note to uppercase for case-insensitivity
    uppercase_note = note.upper()

    # Check if the note is in the mapping
    if uppercase_note in note_mapping:
        return note_mapping[uppercase_note]
    else:
        return None  # Return None for notes not in the mapping

# Example usage:

#note = 'C#'
#result = note_to_number(note)
#if result is not None:
#    print(f"The number corresponding to {note} is {result}.")
#else:
#    print(f"{note} is not a valid note.")
