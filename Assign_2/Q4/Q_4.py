import subprocess
import sys
import re

def get_default_gateway():
    if sys.platform == 'win32':
        command = 'ipconfig'
        pattern = r'Default Gateway . . . . . . . . . : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    else:
        command = 'route -n'
        pattern = r'0.0.0.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    output = subprocess.check_output(command, shell=True).decode()
    match = re.search(pattern, output)
    if match:
        return match.group(1)
    else:
        return None

print("Default Gateway: ", get_default_gateway())
