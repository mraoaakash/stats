#! /bin/bash
#PBS -N DATA_HISTOIMGAN
#PBS -l host=compute3
#PBS -o model_DATA_HISTOIMGAN_out.log
#PBS -e model_DATA_HISTOIMGAN_err.log
#PBS -q gpu

module load compiler/anaconda3

conda init

source ~/.bashrc

conda activate histoimgan
python3 walker.py