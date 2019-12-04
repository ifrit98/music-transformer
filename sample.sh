DATA_DIR=/media/jason/models/maestro-tfr
HPARAMS_SET=transformer_base
MODEL=transformer
PROBLEM=score2perf_maestro_language_uncropped_aug
TRAIN_DIR=/media/jason/models/maestro-tfr/training

DECODE_HPARAMS=\
"alpha=0,"\
"beam_size=1,"\
"extra_length=2048"

t2t_decoder \
  --data_dir="${DATA_DIR}" \
  --decode_hparams="${DECODE_HPARAMS}" \
  --decode_interactive \
  --hparams="sampling_method=random" \
  --hparams_set=${HPARAMS_SET} \
  --model=${MODEL} \
  --problem=${PROBLEM} \
  --output_dir=${TRAIN_DIR}