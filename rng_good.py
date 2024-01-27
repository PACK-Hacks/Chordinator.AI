import random;
from validity_function import valid_all;
from validity_function import validity_function;
from csv_convert import write_to_csv;
from csv_convert import write_to_csv_triple;

I = [1, 6, 5, 4];

def gen_note(root):
    return (root + random.choice([0, 2, 4]) + 7 * random.choice([4]));

def gen_chord(root):
    chord = [];
    i = 0;
    while(i < 4):
        temp_note = gen_note(root);
        if (temp_note in chord):
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

def gen_list_progs(amount, root_prog, filename):
    list_root_progs = [];
    list_chord_progs = [];
    list_validations = [];
    for i in range(amount):
        temp_chord_prog = gen_chord_prog(root_prog);

        list_root_progs.append(root_prog);
        list_chord_progs.append(temp_chord_prog);
        list_validations.append(validity_function(root_prog, temp_chord_prog)); 

    write_to_csv_triple(list_root_progs, list_chord_progs, list_validations, filename);
print("Bruh")
gen_list_progs(10, I, "rng_good.csv");

