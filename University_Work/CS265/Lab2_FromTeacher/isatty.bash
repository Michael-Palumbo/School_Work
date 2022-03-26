#!/bin/bash
# isatty - example of checking to see if input is a tty
#
# Kurt Schmidt
#	11/12
#
# KEYWORDS:  -t, tty, isatty
# 

if [ -n "$1" ] ; then
	echo "Input is from these files:"
	while [ -n "$1" ] ; do
		echo "  $1"
		shift
	done
elif [ -t 0 ] ; then  # if file desriptor 0 (stdin) is a tty
	read -p "May I help you? (y/n/[q]) > "
else
	echo "Input is from redirected stdin (not a tty)"
fi

