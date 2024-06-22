def count(s):
    # Split the input text into words
    words = s.split()

    # Initialize counter
    um_count = 0

    # Iterate through each word
    for word in words:
        # Check if the word is "um" (case insensitive)
        if word.lower() == "um":
            um_count += 1

    return um_count

# Test the count function with user input
def main():
    text = input("Text: ")
    print(count(text))

if __name__ == "__main__":
    main()
