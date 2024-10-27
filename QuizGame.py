def ask_question(question, options, answer):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_answer = int(input("Your answer (1-4): "))
            if 1 <= user_answer <= 4:
                break
            else:
                print("Invalid input. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if user_answer == answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {options[answer - 1]}.")
        return False

def run_quiz():
    quiz_data = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Venus", "Mars", "Jupiter"],
            "answer": 3
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["Oxygen", "Gold", "Osmium", "Helium"],
            "answer": 1
        }
    ]
    
    score = 0
    total_questions = len(quiz_data)

    for item in quiz_data:
        correct = ask_question(item["question"], item["options"], item["answer"])
        if correct:
            score += 1

    print("\nQuiz Over!")
    print(f"Your final score is {score}/{total_questions}.")

if __name__ == "__main__":
    run_quiz()
