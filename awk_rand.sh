#!/bin/sh

awk -v loop=10 -v range=100 'BEGIN{
  srand()
  do {
    numb = 1 + int(rand() * range)
    if (!(numb in prev)) {
       print numb
       prev[numb] = 1
       count++
    }
  } while (count<loop)
}'

# Get Random number generator working without replacement for train/val/test split
# Convert train/val/test split data to NoteSequence tfrecord using dir2NS.sh
# Convert NoteSequence tfrecords to Performance encoding using datagen_test.sh in cf
# Get model training on the server with your data!
# Train additional models with different datasets (Experiments)