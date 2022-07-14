#!/bin/bash
# initialize conda 
source ~/anaconda3/etc/profile.d/conda.sh 

cd ~/Documents/github/summer2022/py_grama_fork
echo "Select python version to test within [1-3]: 1. py38 2. py39 3. py310:"
read input
if [[ $input == "1" ]]; then
        conda activate py38grama
elif [[ $input == "2" ]]; then
        conda activate py39grama
elif [[ $input == "3" ]]; then
        conda activate py310grama
else
        echo "Selection not in range"
        return
fi