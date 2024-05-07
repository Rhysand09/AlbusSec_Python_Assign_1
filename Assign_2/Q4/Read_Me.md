# Default Gateway Extractor

This Python script extracts the default gateway address from the output of `ipconfig` (for Windows) or `route -n` (for Linux) and displays it to the user.

## Usage

Run the script in a Python environment. It does not require any arguments.
`python filename.py`

## Requirements

This script requires Python 3 and the following Python libraries installed:

- subprocess
- sys
- re
