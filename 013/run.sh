#!/bin/bash

function print_help {
    printf "\n[ERROR] Wrong usage\n\n"
    printf "Usage:\n"
    printf "  ./run task input_file [enable_profiling]\n\n"
    printf "  - task: '1' or '2'\n"
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

if [ "$1" != 1 ] && [ "$1" != 2 ]; then
    print_help
fi; 

if [ ! -f "$2" ]; then
    printf "[ERROR] Input file $2 does not exist\n"
    exit -2
fi; 

python_exec="python3"
if [ "$3" = "-p" ]; then
    python_exec="time python3 -m cProfile";
fi;

task_nr=$1
input_file=$2

clear
${python_exec} "script${task_nr}.py" "${input_file}"