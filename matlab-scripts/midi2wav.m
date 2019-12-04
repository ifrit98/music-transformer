midi = readmidi('gaspard1.mid');

% [x, fs] = midi2audio(midi);

% Paramaterize midi read
y = midi2audio(midi, 44100, 'sine');

% Normalize and write to file
y = .95.*y./max(abs(y));
audiowrite('gaspard1.wav',y,44100);

