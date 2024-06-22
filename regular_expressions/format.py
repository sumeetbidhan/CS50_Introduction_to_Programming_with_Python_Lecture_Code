import re

name = input("What's your name?: ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(2)

''' 
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
#another way of doing
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"'''


print(f"hello, {name}")

