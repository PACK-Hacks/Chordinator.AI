import random;
from validity_function import valid_all;
from validity_function import validity_function;
from csv_convert import write_to_csv;
from csv_convert import write_to_csv_triple;

def gen1_7():
    return random.randint(1, 7);

def gen1_42():
    return random.randint(1, 42);

def gen_chord():
    chord = [];
    for i in range(4):
        chord.append(gen1_42());
    return chord;

def gen_chord_prog():
    chord_prog = [];
    for i in range(4):
        chord_prog.append(gen_chord());
    return chord_prog;

def gen_root_prog(): 
    root_prog = [];
    for i in range(4):
        root_prog.append(gen1_7());

    return root_prog;

def gen_list_progs(amount):
    list_root_progs = [];
    list_chord_progs = [];
    list_validations = [];
    for i in range(amount):
        temp_root_prog = gen_root_prog();
        temp_chord_prog = gen_chord_prog();

        list_root_progs.append(temp_root_prog);
        list_chord_progs.append(temp_chord_prog);
        list_validations.append(validity_function(temp_root_prog, temp_chord_prog)); 

    write_to_csv_triple(list_root_progs, list_chord_progs, list_validations, "rng_output.csv");
