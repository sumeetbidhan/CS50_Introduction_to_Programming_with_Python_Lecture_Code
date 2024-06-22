def faces(input):
    # Normalize the input
    normalized_input = ' '.join(input.lower().split())

    # Define a dictionary for the mappings
    mappings = {
        "hello :)": "Hello 🙂",
        "goodbye :(": "Goodbye 🙁",
        "hello :) goodbye:(": "Hello 🙂 Goodbye 🙁"
    }

    # Return the corresponding value or a default message
    return mappings.get(normalized_input, "Enter a valid input")

greeting = input("Enter a greeting from 'Hello :)' or 'Goodbye :(' --> ")

result = faces(greeting)
print(result)