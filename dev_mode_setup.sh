#!/bin/bash
# initialize conda 
source ~/anaconda3/etc/profile.d/conda.sh 

echo "Select environment to setup for development mode [1-3]: 1. py38 2. py39 3. py310:"
read input
if [[ $input == "1" ]]; then
        conda create --name py38grama python=3.8
        conda activate py38grama
elif [[ $input == "2" ]]; then
        conda create --name py39grama python=3.9
        conda activate py39grama
elif [[ $input == "3" ]]; then
        conda create --name py10grama python=3.10
        conda activate py310grama
else
        echo "Selection not in range"
        return
fi
pip uninstall py_grama # make sure grama upstream is removed

# activate local pkg version 
(cd ~/Documents/github/summer2022/py_grama_fork && python setup.py develop)
echo -e "\nDevelopment mode should now be active.\nIf you are not within conda environment try running with <source SCRIPT_NAME>"