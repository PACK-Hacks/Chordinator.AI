import React, { useState } from 'react';

const DropdownMenu = () => {
  const [selectedOption, setSelectedOption] = useState('');

  const handleSelectChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <label htmlFor="dropdown">Select an option:</label>
      <select id="dropdown" value={selectedOption} onChange={handleSelectChange}>
        <option value="">-- Select --</option>
        <option value="C Major">C Major</option>
        <option value="G Major">G Major</option>
        <option value="D Major">D Major</option>
        <option value="A Major">A Major</option>
        <option value="E Major">E Major</option>
        <option value="B Major">B Major</option>
        <option value="F# Major">F# Major</option>
        <option value="Db (C#) Major">Db (C#) Major</option>
        <option value="Ab Major">Ab Major</option>
        <option value="Eb Major">Eb Major</option>
        <option value="Bb Major">Bb Major</option>
        <option value="F Major">F Major</option>
      </select>

      {selectedOption && <p>You selected: {selectedOption}</p>}
    </div>
  );
};

export default DropdownMenu;