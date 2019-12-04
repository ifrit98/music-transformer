from magenta.music import midi_io
from sys import argv
import glob
import logging
import json


def midi_file_to_notesequence(path):
    sequence = midi_io.midi_file_to_note_sequence(path)
    text_path = path[:-4] + '.txt'

    with open(text_path, 'w') as f:
        f.write(str(sequence))
    with open(text_path, 'r') as f:
        content = f.readlines()

    return sequence, content


def compute_statistics(sequences):
    # logging.info('Computing statistics...')
    P, Q = {}, {}
    note_sequence, vel_sequence = list(), list()

    for line in sequences:
        if 'pitch:' in line:
            pitch = line[9:-1]
            try:
                note = int(pitch)
            except ValueError:
                logging.warning('Invalid literal for int() with base 10:' + pitch[9:-1])
                logging.warning('Solution:' + pitch[-3:])
                note = int(pitch[-3:])
            note_sequence.append(note)
            if note not in P:
                P[note] = 1
            else:
                P[note] += 1
            continue
        elif 'velocity:' in line:
            velocity = line[12:-1]
            try:
                vel = int(velocity)
            except ValueError:
                logging.warning('Invalid literal for int() with base 10:' + velocity[12:-1])
                logging.warning('Solution:' + velocity[-3:])
                vel = int(velocity[-3:])
            vel_sequence.append(vel)
            if vel not in Q:
                Q[vel] = 1
            else:
                Q[vel] += 1
            continue

    return P, Q, note_sequence, vel_sequence


def read_midi(path_to_midi,fn='beethoven_test_log.txt'):
    statistics = {}
    _, content = midi_file_to_notesequence(path_to_midi)
    P, _, note_seq, _ = compute_statistics(content)

    Px, Qx = {}, {}
    for note, count in P.items():
        Px[note] = 1. / count

    note = lambda x: Px[x]
    notes = list(map(note, note_seq))

    event_probs = notes
    statistics[path_to_midi] = event_probs

    return event_probs


def read_midis(path_to_dir):
    logging.debug('Reading file-paths')
    path = path_to_dir + "/*.mid"
    # logging.debug('Path:' + path)
    file_paths = [fn for fn in glob.glob(path)]
    statistics = {}

    logging.debug('Converting midi files to note sequences...')
    for file in file_paths:
        seq, content = midi_file_to_notesequence(file)
        P, _, note_seq, _ = compute_statistics(content)

        Px, Qx = {}, {}
        for note, count in P.items():
            Px[note] = 1./count
        # for vel, count in Q.items():
        #     Qx[vel] = 1./count

        note = lambda x: Px[x]
        # vel = lambda y:  Qx[y]
        notes = list(map(note, note_seq))
        # vels = list(map(vel, vel_seq))
        # e_seq = list(zip(notes, vels))
        # event_probs = [elt for sublist in e_seq for elt in sublist]

        event_probs = notes

        statistics[file] = event_probs
        fn = 'beethoven_test_log.txt'
        with open(fn, 'a') as f:
            f.write(json.dumps(statistics))
        break

    return statistics


def main():
    if len(argv) > 1:
        path = argv[1]
    else:
        path = '/home/jason/magenta/piano_training/Classical/A/Beethoven/Daniel Barenboim - Beethoven Complete Piano Sonatas (1966)'

    logging.basicConfig(level=logging.DEBUG)
#     logging.basicConfig(filename='midi2ns.log',filemode='w',format='%(name)s - %(levelname)s - %(message)s')

    seq_stats = read_midis(path)
    print(seq_stats.values())

    logging.info('Completed converting midi files')
    exit(0)


if __name__ == "__main__":
   main()
