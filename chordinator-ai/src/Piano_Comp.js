import React, { useState, useEffect } from 'react';
import { Piano, MidiNumbers } from 'react-piano';
import 'react-piano/dist/styles.css';
import Soundfont from 'soundfont-player';

const Piano_Comp = () => {
  const [playedNotes, setPlayedNotes] = useState([]);
  const [disabledNotes, setDisabledNotes] = useState([]);
  const [isPianoDisabled, setIsPianoDisabled] = useState(true);
  const [audioContext, setAudioContext] = useState(null);

  const firstNote = MidiNumbers.fromNote('c3');
  const lastNote = MidiNumbers.fromNote('b4');

  let restrictedNotes = [];

  useEffect(() => {
    // Initialize the audio context when the component mounts
    const context = new AudioContext();
    setAudioContext(context);

    // Cleanup: Close the audio context when the component unmounts
    return () => {
      if (context.state !== 'closed') {
        context.close();
      }
    };
  }, []);

  const onPlayNote = (midiNumber) => {
    if (!isPianoDisabled && playedNotes.length < 4 && !disabledNotes.includes(midiNumber)) {
      // if (restrictedNotes.includes(midiNumber)) {
      //   // Handle the restricted note (e.g., show a message, ignore it, etc.)
      //   return;
      // }

      setPlayedNotes((prevNotes) => [...prevNotes, midiNumber]);

      if (audioContext) {
        Soundfont.instrument(audioContext, 'acoustic_grand_piano').then(function (piano) {
          piano.play(MidiNumbers.getAttributes(midiNumber).note);
        });
      }

      if (playedNotes.length === 3) {
        setIsPianoDisabled(true);
      }
    }
  };

  const handleGenerateChords = () => {
    setDisabledNotes([]);
    restrictedNotes = [];
    setIsPianoDisabled(false);
    setPlayedNotes([]);
  };

  const disableNote = (midiNumber) => {
    setDisabledNotes((prevDisabledNotes) => [...prevDisabledNotes, midiNumber]);
  };

  const renderNoteLabel = ({ keyboardShortcut, midiNumber, isActive }) => {
    const isDisabled = disabledNotes.includes(midiNumber) || (isPianoDisabled && !playedNotes.includes(midiNumber));

    return (
      <div
        style={{
          backgroundColor: isDisabled ? 'grey' : 'transparent',
          pointerEvents: isDisabled ? 'none' : 'auto',
          color: isActive ? 'blue' : 'black',
        }}
      >
        {keyboardShortcut}
      </div>
    );
  };

  // document.getElementsByClassName("ReactPiano__Key")[0].style.backgroundColor = "red";


  const scales = {
    "C Major":        [49, 51, 54, 56, 58, 61, 63, 66, 68, 70],
    "Db (C#) Major":  [50, 52, 55, 57, 59, 62, 64, 67, 69, 71],
    "D Major":        [49, 51, 53, 56, 58, 60, 63, 65, 68, 70],
    "Eb Major":       [49, 52, 54, 57, 59, 61, 64, 66, 69, 71],
    "E Major":        [48, 50, 53, 55, 58, 60, 62, 65, 67, 70],
    "F Major":        [49, 51, 54, 56, 59, 61, 63, 66, 68, 71],
    "Gb (F#) Major":  [48, 50, 52, 55, 57, 60, 62, 64, 67, 69],
    "G Major":        [49, 51, 53, 56, 58, 61, 63, 65, 68, 70],
    "Ab Major":       [50, 52, 54, 57, 59, 62, 64, 66, 69, 71],
    "A Major":        [48, 51, 53, 55, 58, 60, 63, 65, 67, 70],
    "Bb Major":       [49, 52, 54, 56, 59, 61, 64, 66, 68, 71],
    "B (Cb) Major":   [48, 50, 53, 55, 57, 60, 62, 65, 67, 69]  }

  const [selectedOption, setSelectedOption] = useState('');

  const handleSelectChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const resetKeyboardColors = () => {
    const whiteKeys = document.getElementsByClassName("ReactPiano__Key--natural");
    const blackKeys = document.getElementsByClassName("ReactPiano__Key--accidental");

    for (let i = 0; i < whiteKeys.length; i++) {
      whiteKeys[i].style.backgroundColor = '#f6f5f3';
    }

    for (let i = 0; i < blackKeys.length; i++) {
      blackKeys[i].style.backgroundColor = '#555';
    }
  }

  useEffect(() => {
    if (selectedOption.length > 1) {
      setIsPianoDisabled(false);
      resetKeyboardColors();
      setDisabledNotes([]);
      restrictedNotes = [];

      for (let i = 0; i < 10; i++) {
        disableNote(scales[selectedOption][i])
        document.getElementsByClassName("ReactPiano__Key")[scales[selectedOption][i] - 48].style.backgroundColor = "#ff7f7f";
      }
    }
  }, [selectedOption]);

  return (
    <div>
      <div>
        <label htmlFor="dropdown">Select an option:</label>
        <select id="dropdown" value={selectedOption} onChange={handleSelectChange}>
          <option value="">-- Select --</option>
          <option value="C Major">C Major</option>
          <option value="G Major">G Major</option>
          <option value="D Major">D Major</option>
          <option value="A Major">A Major</option>
          <option value="E Major">E Major</option>
          <option value="B (Cb) Major">B (Cb) Major</option>
          <option value="F# (Gb) Major">F# (Gb) Major</option>
          <option value="Db (C#) Major">Db (C#) Major</option>
          <option value="Ab Major">Ab Major</option>
          <option value="Eb Major">Eb Major</option>
          <option value="Bb Major">Bb Major</option>
          <option value="F Major">F Major</option>
        </select>

        {selectedOption && <p>You selected: {selectedOption}</p>}
      </div>
      <Piano
        noteRange={{ first: firstNote, last: lastNote }}
        playNote={(midiNumber) => onPlayNote(midiNumber)}
        stopNote={() => {
          // Implement if needed
        }}
        width={1000}
        keyboardShortcuts={null}
        renderNoteLabel={renderNoteLabel}
      />
      <div>
        <p>Played Notes: {playedNotes.map((midiNumber) => MidiNumbers.getAttributes(midiNumber).note.replace(/\d/g, '') + " ")}</p>
        <button onClick={handleGenerateChords}>Generate Chords</button>
        {/* Add more buttons to disable other notes */}
      </div>
    </div>
  );
};

export default Piano_Comp;
