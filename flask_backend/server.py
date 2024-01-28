from flask import Flask, request, jsonify, send_file
from validity_function import validity_function as vf
from rng_good import utput_good_midi as midi_generator
from note_to_num import note_to_num

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"



@app.route('/notes', methods=['POST'])
def notes():
    data = request.get_json()
    note1 = data.get('note1')
    note2 = data.get('note2')
    note3 = data.get('note3')
    note4 = data.get('note4')
    note_array = [note1,note2,note3,note4]
    note_array = note_to_num(note_array)
    midi = midi_generator(note_array)
    return send_file(midi, as_attachment=True, download_name='output.mid')

    

if __name__ == '__main__':
    app.run(debug=True)

app.run(port=5000)
