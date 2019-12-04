"""
Convert MIDI to synthesized waveform (sinusoidal, 1D tensor output out as .wav)
"""
from magenta.music import midi_io, midi_synth
from scipy.io.wavfile import write
from sys import argv
import glob

# assert len(argv) > 2, 'usage: midi_to_wav.py [path_to_midi] [out_fn] [path_to_sf]'
# args = [arg for arg in argv]

midi_dir_path = argv[1] if len(argv) > 1 else '/home/jason/midi-gen'
sample_rate = int(argv[2]) if len(argv) > 2 else 44100
print('Sample rate:',sample_rate)
print('Path:',midi_dir_path)

path = midi_dir_path + '/*.mid'
midi_files = [fn for fn in glob.glob(path)]

for midi in midi_files:
    note_seq = midi_io.midi_file_to_note_sequence(midi)
    wav = midi_synth.fluidsynth(note_seq, sample_rate)
    out_fn = midi[:-4] + '.wav' 
    print('Out file:',out_fn)
    write(out_fn, sample_rate, wav)


exit(0)
