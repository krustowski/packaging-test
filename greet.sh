#!/bin/sh

# green.sh
# Shell scripting test script
# by Krystof Sara / 26. 6. 2020

PRINT_N_TIMES=1
[[ $# -gt 0 && $1 -gt 0 ]] && PRINT_N_TIMES=$1 

WEEKDAYS=("Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday" "Sunday")

GREETING="Hello $USER! It is ${WEEKDAYS[$(date +%u)-1]} today."

# iterate over the $1 optional
for i in $(seq 1 $PRINT_N_TIMES); do
	echo ${GREETING};
done

