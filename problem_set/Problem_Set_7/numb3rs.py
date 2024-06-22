import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    if not re.match(pattern, ip):
        return False

    parts = ip.split(".")

    for part in parts:
        if not 0 <= int(part) <= 255:
            return False

    return True

if __name__ == '__main__':
    main()