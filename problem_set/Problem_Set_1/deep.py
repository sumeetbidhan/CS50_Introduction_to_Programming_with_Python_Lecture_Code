def main():
    question = input("What is the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if is_great_question(question):
        print("Yes")
    else:
        print("No")

def is_great_question(question):
    normalized_question = question.replace("-", " ").replace(" ", "")
    acceptable_answer = ["42", "fortytwo"]
    return normalized_question in acceptable_answer

main()
