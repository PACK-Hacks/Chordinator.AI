import random;
from validity_function import valid_all;
from validity_function import validity_function;
from csv_convert import write_to_csv;
from csv_convert import write_to_csv_triple;
from backwards import output_midi;

I = [1, 6, 5, 4];
II = [3, 5, 6, 1];
III = [2, 4, 6, 5];
IV = [4, 3, 6, 5];
V = [1, 6, 3, 5];
VI = [6, 4, 5, 1];
VII = [4, 1, 6, 5]; 


def gen_note(root):
    return (root + random.choice([0, 2, 4]) + (7 * random.choice([3, 4])));


def gen_chord(root):
    chord = [root + 7 * 3]; 
    
    i = 0;
    while(i < 3):
        temp_note = gen_note(root);
        if (temp_note in chord or temp_note > 35):
            continue;        
        else:
            chord.append(temp_note);
            i+= 1;
    return chord;
        
def gen_chord_prog(root_prog):
    chord_prog = [];
    for i in range(4):
        chord_prog.append(gen_chord(root_prog[i]));
    return chord_prog;

# def gen_list_progs(amount, root_prog, filename):
#     list_root_progs = [];
#     list_chord_progs = [];
#     list_validations = [];
#     for i in range(amount):
#         temp_chord_prog = gen_chord_prog(root_prog);

#         list_root_progs.append(root_prog);
#         list_chord_progs.append(temp_chord_prog);
#         list_validations.append(validity_function(root_prog, temp_chord_prog)); 

#     write_to_csv_triple(list_root_progs, list_chord_progs, list_validations, filename);

def output_good_midi(root_prog):
    output_midi(gen_chord_prog(root_prog));

print('start');
output_good_midi(I); 
print('done');



