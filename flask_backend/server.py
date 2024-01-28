from flask import Flask, request, jsonify, send_file
from validity_function import validity_function as vf
from rng_good import output_good_midi as midi_generator
from note_to_num import note_to_num
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)




@app.route('/')
def home():
    return "hello world"



@app.route('/api/notes', methods=['POST'])
def notes():
    print('Request received')
    data = request.get_json()
    note1 = data.get('note1')
    note2 = data.get('note2')
    note3 = data.get('note3')
    note4 = data.get('note4')
    note_array = [note1,note2,note3,note4]
    note_array = note_to_num(note_array)
    midi_generator(note_array)
    # print('running send file command')
    # return send_file(midi, as_attachment=True, download_name='output.mid')

    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, use_reloader=True)

