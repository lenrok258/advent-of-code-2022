#!/bin/bash

if [ $# != 1 ]; then
    printf "Missing parameter:\n  - task [1 or 2]\n"
    printf "Example:\n  ./run.sh 1\n"
    exit -1
fi; 

if [ $1 != 1 ] && [ $1 != 2 ]; then
    printf "Wrong parameter:\n  - task [1 or 2]\n"
    printf "Example:\n  ./run.sh 1\n"
    exit -1
fi; 

task_nr=$1

clear
python3 "script${task_nr}.py"