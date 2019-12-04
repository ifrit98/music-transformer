% Load midi struct
midi = readmidi('blackmass.mid');

% Get note sequence information
notes = midiInfo(midi);

% Load piano roll with velocity information
[PR,t,nn] = piano_roll(notes,1);

figure(1);
imagesc(t,nn,PR);
axis xy;
xlabel('time (sec)');
ylabel('note (int)');
