note_mapping = {
            "C0" : 1, "D0" : 2, "E0" : 3, "F0" : 4, "G0" : 5, "A1" : 6, "B1" : 7,
        }

def note_to_num(note_array):
    num_array = [note_mapping[x] for x in note_array]
    return num_array
        