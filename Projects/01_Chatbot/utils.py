def get_answer(question, qa_dict):
    """
    Returns the answer to a given question if found, else a default message.
    """
    if question.isdigit():
        if int(question) < 1 or int(question) > len(qa_dict):
            return "Invalid question number. Please try again."

        # If the user input is a number, return the corresponding question
        question = list(qa_dict.keys())[int(question) - 1]
    question = question.strip().lower()
    return qa_dict.get(question, "Sorry, I don’t have an answer for that yet.")


def print_available_questions(qa_dict):
    """
    Prints all available questions from the dictionary.
    """
    print("\nAvailable Questions:")
    for idx, q in enumerate(qa_dict.keys(), 1):
        print(f"{idx}. {q}")
    print()
