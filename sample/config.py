import numpy
import os
import sys

for line in open('params.txt'):
    if line.startswith('#'):
        continue

    if '=' in line:
        key, value = line.rstrip().split('=')
        key = key.trim()
        value = value.trim()

        if key == 'SRC':
            SRC = value
        elif key = 'TRG':
            TRG = value

# TODO: automatically figure out vocab size from prebuilt model

VOCAB_SIZE = 90000
DATA_DIR = "data/"

from nematus.nmt import train

if __name__ == '__main__':
    validerr = train(saveto='model/model.npz',
                    reload_=True,
                    dim_word=500,
                    dim=1024,
                    n_words=VOCAB_SIZE,
                    n_words_src=VOCAB_SIZE,
                    decay_c=0.,
                    clip_c=1.,
                    lrate=0.0001,
                    optimizer='adadelta',
                    maxlen=50,
                    batch_size=80,
                    valid_batch_size=80,
                    datasets=[DATA_DIR + '/corpus.bpe.' + SRC, DATA_DIR + '/corpus.bpe.' + TRG],
                    valid_datasets=[DATA_DIR + '/validate.bpe.' + SRC, DATA_DIR + '/validate.bpe.' + TRG],
                    dictionaries=[DATA_DIR + '/corpus.bpe.' + SRC + '.json',DATA_DIR + '/corpus.bpe.' + TRG + '.json'],
                    validFreq=10000,
                    dispFreq=1000,
                    saveFreq=30000,
                    sampleFreq=10000,
                    use_dropout=False,
                    dropout_embedding=0.2, # dropout for input embeddings (0: no dropout)
                    dropout_hidden=0.2, # dropout for hidden layers (0: no dropout)
                    dropout_source=0.1, # dropout source words (0: no dropout)
                    dropout_target=0.1, # dropout target words (0: no dropout)
                    overwrite=False,
                    external_validation_script='./validate.sh')
    print validerr
