from flask import Flask, request, jsonify, send_file
from validity_function import validity_function as vf
from rng_good import output_good_midi as midi_generator
from note_to_num import note_to_num
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins='http://127.0.0.1:3000')




@app.route('/')
def home():
    return "hello world"


note_mapping_12 = {
        1: 'C0', 2: 'C#0', 3: 'D0', 4: 'D#0', 5: 'E0',
        6: 'F0', 7: 'F#0', 8: 'G0', 9: 'G#0', 10: 'A1', 11: 'A#1', 12: 'B1',
        13: 'C1', 14: 'C#1', 15: 'D1', 16: 'D#1', 17: 'E1',
        18: 'F1', 19: 'F#1', 20: 'G1', 21: 'G#1', 22: 'A2', 23: 'A#2', 24: 'B2',
        25: 'C2', 26: 'C#2', 27: 'D2', 28: 'D#2', 29: 'E2',
        30: 'F2', 31: 'F#2', 32: 'G2', 33: 'G#2', 34: 'A3', 35: 'A#3', 36: 'B3',
        37: 'C3', 38: 'C#3', 39: 'D3', 40: 'D#3', 41: 'E3',
        42: 'F3', 43: 'F#3', 44: 'G3', 45: 'G#3', 46: 'A4', 47: 'A#4', 48: 'B4',
        49: 'C4', 50: 'C#4', 51: 'D4', 52: 'D#4', 53: 'E4',
        54: 'F4', 55: 'F#4', 56: 'G4', 57: 'G#4', 58: 'A5', 59: 'A#5', 60: 'B5',
        61: 'C5', 62: 'C#5', 63: 'D5', 64: 'D#5', 65: 'E5',
        66: 'F5', 67: 'F#5', 68: 'G5', 69: 'G#5', 70: 'A6', 71: 'A#6', 72: 'B6'
    }

note_mapping_7 = {
    "C0" : 1, "D0" : 2, "E0" : 3, "F0" : 4, "G0" : 5, "A1" : 6, "B1" : 7,
    "C1" : 8, "D1" : 9, "E1" : 10, "F1" : 11, "G1" : 12, "A2" : 13, "B2" : 14,
    "C2" : 15, "D2" : 16, "E2" : 17, "F2" : 18, "G2" : 19, "A3" : 20, "B3" : 21,
    "C3" : 22, "D3" : 23, "E3" : 24, "F3" : 25, "G3" : 26, "A4" : 27, "B4" : 28,
    "C4" : 29, "D4" : 30, "E4" : 31, "F4" : 32, "G4" : 33, "A5" : 34, "B5" : 35,
    "C5" : 36, "D5" : 37, "E5" : 38, "F5" : 39, "G5" : 40, "A6" : 41, "B6" : 42
}

def pitch_to_num(pitch):
    return note_mapping_7[pitch]

def num_to_pitch(num):
    return note_mapping_12[num]

def scale_data(old):
    return pitch_to_num(num_to_pitch(old))


@app.route('/api/notes', methods=['POST'])
def notes():
    print('Request received')
    data = request.get_json()
    print("here is data", data)
    note1 = data.get('note1')
    note2 = data.get('note2')
    note3 = data.get('note3')
    note4 = data.get('note4')
    note_array = [note1,note2,note3,note4]
    print('note_array loaded:', note_array)
    note_array = [scale_data(x-23)%7 for x in note_array]
    print("here is the real note array", note_array)
    midi_generator(note_array);
    midi = "Chordinator.AI/chordinator-ai/public/output2.mid"
    print(midi)
    print('running send file command')
    return send_file(midi, as_attachment=True, download_name='generated.mid')

    

if __name__ == '__main__':
    app.run(port=5000, debug=True, use_reloader=True)