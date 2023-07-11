#! /bin/bash
#PBS -N DATA_HISTOIMGAN
#PBS -l host=compute3
#PBS -o /home/rintu.kutum/stats/out.log
#PBS -e /home/rintu.kutum/stats/err.log
#PBS -q gpu

module load compiler/anaconda3

conda init

source ~/.bashrc

conda activate histoimgan
# python3 /home/rintu.kutum/stats/walker.py
python3 /home/rintu.kutum/stats/statgen.py