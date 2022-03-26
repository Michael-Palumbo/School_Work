#!/bin/bash
# func.bash - Example of functions
#
# Kurt Schmidt
#	1/04
# 
# Platform: Linux 2.6.18.6 
# 
# EDITOR: tabstop=2, cols=80
# 
# KEYWORDS:  function, recursion, return
#


function hello
{
	local blah="What Is, and What Should Never Be"
	echo "\$blah is: $blah"

	echo "hello $1"
	if [[ -n "$2" && "$2" -gt 1 ]] ; then
		hello $1 $(($2-1))
	fi
}

also()
{
	echo "I'm a function, too"

	return ${1:-0}
}

hello Vera 12
hello Heather

echo "\$blah is: $blah"

if also 3 ; then
	echo "That's weird"
fi

if also ; then
	echo "That's better"
fi

if also 0 ; then
	echo "That, too"
fi
