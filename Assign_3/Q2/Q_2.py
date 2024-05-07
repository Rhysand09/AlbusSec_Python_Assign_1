import re

def extract_pattern(file_name, pattern):
    with open(file_name, 'r') as file:
        content = file.read()
    matches = re.findall(pattern, content)
    return matches
