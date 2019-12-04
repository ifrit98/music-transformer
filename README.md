### Magenta
My first suggestion would be to go to the [onsets github](https://github.com/tensorflow/magenta/tree/master/magenta/models/onsets_frames_transcription) page and poke around at the [model](https://github.com/tensorflow/magenta/blob/master/magenta/models/onsets_frames_transcription/model.py) architecture.

To get going, read the manpage and look [here](https://github.com/tensorflow/magenta/blob/master/magenta/models/onsets_frames_transcription/onsets_frames_transcription_transcribe.py)  at the .py file that actually does the transcribing  given a trained Onsets model.

I strongly suggest reading the original [onsets](https://arxiv.org/pdf/1710.11153.pdf) paper and then the [transformer](https://arxiv.org/pdf/1706.03762.pdf) paper for the first two pieces (transcription, and generation).  [Wavenet](https://arxiv.org/pdf/1609.03499.pdf) is the last piece, and is how we synthesize the midi output of the transformer model  to sound like an acoustic piano.  To tie it all together, the [Music Transformer](https://arxiv.org/pdf/1809.04281.pdf) paper shows the overall architecture that I followed. Here's a good [Google blog post](https://magenta.tensorflow.org/music-transformer).


I'd also suggest getting your head around attention in general, from the original papers by [Luong](https://arxiv.org/pdf/1508.04025.pdf) and [Bahdanau](https://arxiv.org/pdf/1409.0473.pdf), to some good blogs that visualize the process [here](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/), and [here](http://jalammar.github.io/illustrated-transformer/). From there it may be helpful to study the transformer codebase in tensor2tensor, as well as the magenta music transformer (called [score2perf](https://github.com/tensorflow/magenta/tree/master/magenta/models/score2perf)).

Much of the headache is in using Google Cloud and Apache beam to preprocess the data, [here](https://github.com/tensorflow/magenta/blob/master/magenta/models/score2perf/datagen_beam.py).  Again the readmes for these (on the Magenta side) will be very useful.

Unfortunately, there is not  a complete codebase to give you, I essentially made little scripts for myself and did a lot at the terminal to use a pretrained onsets model to create my own dataset, curated it, and then trained several transformer models.

Much of the code I do have to give you is for analysis and plotting of results after training the models.  There are some tools in MATLAB (self-similarity matrices, midi2wav, etc), as well as some bash scripts to preprocess the datasets.  Feel free to poke around and email me with any questions.

Good luck getting started!
