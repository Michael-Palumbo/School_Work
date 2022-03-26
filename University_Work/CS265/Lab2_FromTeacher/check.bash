#!/bin/bash

function honor
{
	n="$1"

	if [ -z $2 ] ; then
		c=100
	else
		c=$2
	fi

	for (( i=0; i<$c; ++i )) ; do
		echo -n "$n "
	done
	echo ""
}

for n in a b c ; do
	echo $n
done

ls

honor Jadwiga
