#!/bin/bash

# Path to the Python decoder script
DECODER_SCRIPT="./decoder.py"

# Check if strings.txt exists
if [ ! -f strings.txt ]; then
    echo "strings.txt not found"
    exit 1
fi

# Read each line from strings.txt and pass it to the decoder
while IFS= read -r line
do
    python3 "$DECODER_SCRIPT" "$line"
done < "strings.txt"
