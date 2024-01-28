import React, { useState } from 'react';
import { Piano, KeyboardShortcuts, MidiNumbers } from 'react-piano';
import 'react-piano/dist/styles.css';
import DropdownMenu from './DropdownMenu';

const Piano_Comp = ({ onKeyPress }) => {
    const [playedNotes, setPlayedNotes] = useState([]);
    const [isPianoDisabled, setIsPianoDisabled] = useState(false);

    const firstNote = MidiNumbers.fromNote('c3');
    const lastNote = MidiNumbers.fromNote('b4');
    
    const onPlayNote = (midiNumber) => {
      if (!isPianoDisabled && playedNotes.length < 4) {
        setPlayedNotes((prevNotes) => [...prevNotes, midiNumber]);
  
        console.log(midiNumber)

        if (playedNotes.length === 3) {
          setIsPianoDisabled(true);
        }
      }
    };

    const handleGenerateChords = () => {
      setIsPianoDisabled(false);
      setPlayedNotes([]);
    };
   
    return (
      <div>
        <DropdownMenu />
        <Piano
          noteRange={{ first: firstNote, last: lastNote }}
          playNote={(midiNumber) => {
            onPlayNote(midiNumber)
          }}
          stopNote={(midiNumber) => {
            // Stop playing a given note - see notes below
          }}
          width={1000}
          keyboardShortcuts={null}
        />
        <div>
          <p>Played Notes: {playedNotes.map((midiNumber) => MidiNumbers.getAttributes(midiNumber).note.replace(/\d/g, ''))}</p>
          <button onClick={handleGenerateChords}>Generate Chords</button>
        </div>
      </div>
    );
};

export default Piano_Comp;