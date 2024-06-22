import re

email = input("What's your email?: ").strip()

#username, domain = email.split("@")

'''if username and domain.endswith(".edu"):
    print("valid")
else:
    print("Invalid")'''


#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#This can also be writtern as
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
