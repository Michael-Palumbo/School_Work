thisScript="$0"

dir="."

if [ -z "$1" ] ; then
	dir="$1"
fi

echo "This script is: $thisScript"

cd "$dir"

echo "We are in directory: $PWD"

ls -1 | while read f ; do
	if [ -f "$f" ] ; then
		echo "file: $f"
	elif [ -d "$f" ] ; then
		"$thisScript" "$f"
	fi
done
