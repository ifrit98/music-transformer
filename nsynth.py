import os
import numpy as np
import matplotlib.pyplot as plt
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
from IPython.display import Audio

def load_encoding(fname, sample_length=None, sr=16000, ckpt='model.ckpt-200000'):
    audio = utils.load_audio(fname, sample_length=sample_length, sr=sr)
    encoding = fastgen.encode(audio, ckpt, sample_length)
    return audio, encoding


def _crossfade(encoding1, encoding2):
    return fade(encoding1, 'out') + fade(encoding2, 'in')


def crossfade():
	return fastgen.synthesize(_crossfade(enc1, enc2), save_paths=['crossfade.wav'])

def interpolate():
	sample_length = 80000
	# from https://www.freesound.org/people/MustardPlug/sounds/395058/
	aud1, enc1 = load_encoding('395058__mustardplug__breakbeat-hiphop-a4-4bar-96bpm.wav', sample_length)
	# from https://www.freesound.org/people/xserra/sounds/176098/
	aud2, enc2 = load_encoding('176098__xserra__cello-cant-dels-ocells.wav', sample_length)
	enc_mix = (enc1 + enc2) / 2.0

	fig, axs = plt.subplots(3, 1, figsize=(10, 7))
	axs[0].plot(enc1[0]); 
	axs[0].set_title('Encoding 1')
	axs[1].plot(enc2[0]);
	axs[1].set_title('Encoding 2')
	axs[2].plot(enc_mix[0]);
	axs[2].set_title('Average')

	fastgen.synthesize(enc_mix, save_paths='mix.wav')


def encode():
	# from https://www.freesound.org/people/MustardPlug/sounds/395058/
	# fname = '395058__mustardplug__breakbeat-hiphop-a4-4bar-96bpm.wav'
	fname = './wav/mehldau-1.wav'
	sr = 44100
	audio = utils.load_audio(fname, sample_length=44100, sr=sr)
	sample_length = audio.shape[0]
	print('{} samples, {} seconds'.format(sample_length, sample_length / float(sr)))

	encoding = fastgen.encode(audio, './wavenet-ckpt/model.ckpt-200000', sample_length)

	print(encoding.shape)

	np.save(fname + '.npy', encoding)

	fig, axs = plt.subplots(2, 1, figsize=(10, 5))
	axs[0].plot(audio);
	axs[0].set_title('Audio Signal')
	axs[1].plot(encoding[0]);
	axs[1].set_title('NSynth Encoding')
	return encoding


def decode(fname, sample_length=44100, sr=16000):
	fastgen.synthesize(encoding, save_paths=['gen_' + fname], samples_per_save=sample_length)
	synthesis = utils.load_audio('gen_' + fname, sample_length=sample_length, sr=sr)
	return synthesis


def main():
	encoding = encode()


if __name__ == "__main__":
	main()