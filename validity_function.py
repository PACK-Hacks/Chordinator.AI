def valid_all(data):
    for pair in range(len(data)):
        return validity_function(data[pair][0], data[pair][1], pair);



def validity_function(base_notes, chord_progression, acc = 0):
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
    sub1_1 = validity_array[0:4]
    sub1_2 = validity_array[4:8]
    sub1_3 = validity_array[8:12]
    sub1_4 = validity_array[12:16]
    sub2_1 = base_multiple_array[0:4]
    sub2_2 = base_multiple_array[4:8]
    sub2_3 = base_multiple_array[8:12]
    sub2_4 = base_multiple_array[12:16]
    if (False in sub1_1 or False in sub1_2 or False in sub1_3 or False in sub1_4):
        return False;
    elif (True in sub2_1 and True in sub2_2 and True in sub2_3 and True in sub2_4):
        return True;
    else:
        return False
    
    

# print(validity_function([1, 5, 4, 6], [[26, 24, 22, 15],[30, 21, 26, 19],[29, 20, 25, 18],[31, 29, 20, 13]]))
    

