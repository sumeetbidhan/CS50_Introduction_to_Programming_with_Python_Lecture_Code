def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length of the plate
    if not (2 <= len(s) <= 6):
        return False

    # Check that the plate starts with at least two letters
    if not s[:2].isalpha():
        return False

    # Check that there are no periods, spaces, or punctuation marks
    if not s.isalnum():
        return False

    # Check numbers are at the end and the first number is not '0'
    found_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            found_number = True
            # The first number cannot be '0'
            if s[i] == '0':
                return False
            # Ensure all characters after the first digit are also digits
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            break

    return True

if __name__ == '__main__':
    main()
