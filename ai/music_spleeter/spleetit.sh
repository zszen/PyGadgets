#!/bin/bash
conda activate py3
echo input mp3 path
read mp3
echo wait dealing
spleeter separate -i "$mp3" -p spleeter:2stems -o ~/Desktop/output
