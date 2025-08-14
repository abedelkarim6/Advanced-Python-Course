from utils import get_answer, print_available_questions

qa_dict = {
    "What is the goal of the crash course?": "Experience hands-on how real AI models power applications, by building 5 practical tools in just 5 sessions.",
    "How many sessions are there?": "There are 5 sessions, each focused on a practical application of AI.",
    "What is covered in session 1?": "Session 1: Intro to AI – Explore AI fundamentals, its fields, industry applications, and research directions.",
    "What is covered in session 2?": "Session 2: Advanced Prompting – Learn techniques to get better and more reliable results from LLMs.",
    "What is covered in session 3?": "Session 3: RAG using Streamlit – Build a Retrieval-Augmented Generation chatbot as a web app.",
    "What is covered in session 4?": "Session 4: OpenCV Face Detection & Recognition – Implement real-time face detection and recognition.",
    "What is covered in session 5?": "Session 5: MediaPipe / DeepSort – Track and identify objects in videos using advanced tracking methods.",
    "What is covered in session 6?": "Session 6: Data Science & Machine Learning – Apply ML algorithms to real datasets for prediction and analysis.",
    "Do i need prior ai experience?": "Basic Python knowledge is enough; all models are pretrained and we focus on application.",
    "What tools will we use?": "We will use Python, OpenCV, Hugging Face, scikit-learn, MediaPipe, DeepSort, and Streamlit.",
    "Will there be a final project?": "Yes, after the sessions you will combine multiple techniques into 1 system as a final project.",
}


def main():
    print("=== AI Practical Crash Course Chatbot ===")
    print_available_questions(qa_dict)

    while True:
        user_input = input(
            "\nEnter your question or number (or type 'exit' to quit): "
        ).lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        answer = get_answer(user_input, qa_dict)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
