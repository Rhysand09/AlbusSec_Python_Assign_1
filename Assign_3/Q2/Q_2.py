import re

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'

with open('file.txt', 'r') as f:
    content = f.read()

emails = re.findall(email_pattern, content)
phone_numbers = re.findall(phone_pattern, content)

print('Emails:', emails)
print('Phone Numbers:', phone_numbers)
