def validity_function(base_notes, chord_progression):
    validity_array = []
    base_multiple_array = []
    for i in range(4):
        for j in range(4):
            if (abs(base_notes[i] - chord_progression[i][j]) % 7 == 0 or 
                abs(base_notes[i] - chord_progression[i][j]) % 7 == 2 or 
                abs(base_notes[i] - chord_progression[i][j]) % 7 == 4):
                validity_array.append(True)
            else:
                validity_array.append(False)
            if (abs(base_notes[i] - chord_progression[i][j]) % 7 == 0):
                base_multiple_array.append(True)
            else:
                base_multiple_array.append(False)
    if (False in validity_array):
        return False
    elif (True in base_multiple_array):
        return True
    else:
        return False
    


    

