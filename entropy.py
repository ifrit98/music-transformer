import numpy as np
import logging
import midi2ns
import glob

"""With precomputed event sequence probabilities as sequence X"""


def mutual_inf(X,Y):
    return entropy(X) - conditional_entropy(X,Y)


def conditional_entropy(X,Y):
    h = 0.
    for x in X:
        for y in Y:
            h += (x+y)*np.log2((x+y)/x)
    return -1.*h


def entropy(X):
    h = lambda xi: (xi*np.log2(xi))
    H = np.sum(list(map(h,X)))
    return -1.*H


def IR(X):
    IRs = list()
    for i in range(len(X)):
        IR = mutual_inf(X[:i+1],X[:i])
        IRs.append(IR)
    return np.sum(IRs) / float(len(IRs))


def dir_to_noteseq_stats(path):
    midi_statistics = midi2ns.read_midis(path)
    return midi_statistics


def compute_IR_midi(midi_statistics):
    rates = list()
    for file_path, seq in midi_statistics.items():
        rates.append(IR(seq))
    return rates


def read_midi_text_ns(path_to_file):
    with open(path_to_file, 'r') as f:
        content = f.readlines()
    return content


def cond_markov(X):
    # Computes H(Vn | Vn-1) using 1st order markov chain
    h = lambda x: 1./413.*x*(np.log2(x))
    H = np.sum(list(map(h,X)))
    return -1.*H


def fast_IR(X):
    return entropy(X) - cond_markov(X)


def norm(IR):
    normed = {}
    lo, hi = 99999., 0.

    for ir in IR.values():
        if ir < lo:
            lo = ir
        if ir > hi:
            hi = ir

    alpha = 1./(hi-lo)
    print(lo, hi, alpha)
    for fn, ir in IR.items():
        norm = ir*alpha
        normed[fn] = norm
    return normed


def sum_to_1(IRs):
    norm_IRs = {}
    alpha = 0.
    for ir in IRs.values():
        alpha += ir
    for fn,ir in IRs.items():
        norm_IRs[fn] = (1./alpha)*ir
    return norm_IRs


def compute_IR_dir_from_txt(file_paths):
    IR_calcs = {}

    for file in file_paths:
        content = read_midi_text_ns(file)
        logging.info('Content text file generated...')
        P, _, note_seq, _ = midi2ns.compute_statistics(content)
        Px = {}
        logging.info('Statistics computed...')

        for note, count in P.items():
            Px[note] = 1./count

        note = lambda x: Px[x]
        notes = list(map(note, note_seq))

        event_probs = notes
        logging.info('Computing IR...')
        logging.info(str(file))
        print('N:', len(event_probs))
        IR_calcs[file] = fast_IR(event_probs)
        print(file[-20:], IR_calcs[file])

    return norm(IR_calcs)


def compute_IR_dir_from_midi(file_paths):
    IR_calcs = {}

    for file in file_paths:
        event_probs = midi2ns.read_midi(file)
        logging.info('Statistics computed...')
        logging.info(str(file))
        logging.info('N: ' + str(len(event_probs)))
        logging.info('Computing IR...')
        IR_calcs[file] = fast_IR(event_probs)
        logging.info(str(IR_calcs[file]))

    return IR_calcs


def write_IR_to_txt(normed_IR,fn='out.txt'):
    logging.info('Writing results to' + fn)
    for file, norm_ir in normed_IR.items():
        with open(fn, 'a') as f:
            f.write(str({file: norm_ir})+'\n')


def main():
    logging.basicConfig(level=logging.DEBUG)
    # path = '/media/jason/MAGENTA/MIDI/midi-data/dataset-full/Jazz/Brad Mehldau/Brad Mehldau - 10 Years Solo Live'
    path = '/media/jason/MAGENTA/models/composers/bach/samples/best/'
    path = path + "/*.mid"
    files = [fn for fn in glob.glob(path)]
    information_rates = compute_IR_dir_from_midi(files)
    # normed_IR = norm(information_rates)
    normed_IR = information_rates
    inf_rates = list(normed_IR.values())
    # inf_rates /= np.max(np.abs(information_rates.values()), axis=0)

    avg = np.sum(inf_rates) / len(inf_rates)
    logging.info('Average IR: ' + str(avg))

    with open('./stats/bach-model_box_plt_u.txt', 'a') as f:
        for ir in inf_rates:
            f.write(str(ir)+'\n')
        f.write('Average IR:' + str(avg))


if __name__ == "__main__":
    main()
