import re
file = open("sample.txt", "r")
data = file.read()
emails = re.findall(r'\S+@\S+', data)
output = open("emails.txt", "w")
for i in emails:
    output.write(i + "\n")
output.close()
print("Emails Extracted Successfully")
for i in emails:
    print(i)