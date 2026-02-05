#!/bin/bash
# scripts/spacer.sh - 在每行前后添加空行

if [ -z "$1" ]; then
    echo "Usage: spacer.sh <file>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File not found: $1"
    exit 1
fi

sed -i -e 's/^/\n/' -e 's/$/\n/' "$1"
echo "Done: $1"
