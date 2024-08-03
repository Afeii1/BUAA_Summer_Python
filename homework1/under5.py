all_messages = []
person_messages = []

while True:
    line = input()
    if line == "no new messages":
        break
    if "@all" in line:
        all_messages.append(line)
        continue
    if "@nyima" in line:
        person_messages.append(line)

all_messages.sort()
person_messages.sort(reverse=True)

for s in all_messages:
    print(s)

for ss in person_messages:
    print(ss)
