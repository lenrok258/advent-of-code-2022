#!/bin/bash

function print_help {
    printf "\n[ERROR] Wrong usage\n\n"
    printf "Usage:\n"
    printf "  ./run script_number input_file [enable_profiling]\n\n"
    printf "  - script number: '1', '2'...\n"
    printf "  - input_file: 'input_test.txt' or 'input.txt'\n"
    printf "  - enable profiling: -p\n"
    printf "\n"
    printf "Examples:\n"
    printf "  ./run.sh 1 input_test.txt\n"
    printf "  ./run.sh 2 input.txt -p\n"
    printf "\n"
    exit -1
}

if [ "$#" -lt 2 ]; then
    print_help
fi; 

script_number=$1
script_file="script${script_number}.py"
input_file=$2

if [ ! -f "${script_file}" ]; then
    printf "[ERROR] Script file '${script_file}' does not exist\n"
    exit -2
fi; 

if [ ! -f "${input_file}" ]; then
    printf "[ERROR] Input file '${input_file}' does not exist\n"
    exit -2
fi; 

python_exec="python3"
if [ "$3" = "-p" ]; then
    python_exec="time python3 -m cProfile";
fi;

clear
${python_exec} "${script_file}" "${input_file}"