# Harappan Civilization Quiz Game

def ask_question(question, options, answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    try:
        user_answer = int(input("Enter the number of your answer: "))
        if options[user_answer - 1] == answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    except (IndexError, ValueError):
        print("Invalid input. Please enter the number corresponding to your answer.")

def main():
    print("Welcome to the Harappan Civilization Quiz!")
    print("Let's test your knowledge.")
    
    questions = [
        {
            "question": "Which modern-day countries were part of the Harappan Civilization?",
            "options": ["India and Bangladesh", "India and Pakistan", "Pakistan and Afghanistan", "India and Sri Lanka"],
            "answer": "India and Pakistan"
        },
        {
            "question": "Which of the following was a major Harappan city?",
            "options": ["Harappa", "Delhi", "Lahore", "Karachi"],
            "answer": "Harappa"
        },
        {
            "question": "What is the main challenge in deciphering the Harappan writing system?",
            "options": ["Lack of inscriptions", "No bilingual texts", "Lack of physical artifacts", "Unclear script structure"],
            "answer": "No bilingual texts"
        }
    ]
    
    for q in questions:
        ask_question(q["question"], q["options"], q["answer"])

    print("Thank you for playing the quiz!")

if __name__ == "__main__":
    main()
