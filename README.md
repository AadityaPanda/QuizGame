# Python Quiz Game 🧠

Welcome to the **Python Quiz Game**, a simple and interactive multiple-choice quiz application built to test general knowledge while reinforcing Python programming skills. This project is designed for beginners and those looking to practice Python fundamentals, including data structures, control flow, and error handling. The game is modular, customizable, and user-friendly!

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Customization](#customization)
- [Code Structure](#code-structure)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Multiple-Choice Questions**: Each question presents four answer choices. Customize your questions and options easily.
- **Scoring System**: Tracks the user’s correct answers and displays a final score at the end.
- **User Input Validation**: Ensures that users only provide valid answers, with error handling for smooth gameplay.
- **Real-Time Feedback**: Displays whether the user’s answer is correct or incorrect, and shows the correct answer if they’re wrong.
- **Modular Code Structure**: Organized with functions, making the code easy to read, extend, and maintain.

---

## Getting Started

### Prerequisites

- **Python 3.11**: Make sure Python 3.11 is installed on your machine. You can download it [here](https://www.python.org/downloads/release/python-3110/).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/quiz-game.git
   cd quiz-game
   ```

2. **Run the quiz game**:
   ```bash
   python quiz_game.py
   ```

---

## Customization

The quiz game is easily customizable. To add or modify questions, simply edit the `quiz_data` list in the code:

```python
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_option": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "correct_option": 3
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Osmium", "Helium"],
        "correct_option": 1
    }
]
```

Each entry in `quiz_data` is a dictionary containing:
- **`"question"`**: The question text.
- **`"options"`**: A list of four answer choices.
- **`"correct_option"`**: An integer (1-4) representing the correct option's position.

---

## Code Structure

- **`ask_question(question, options, correct_option)`**: Function to display a question and its options, take user input, and check if it’s correct.
- **`run_quiz()`**: Main function that loops through the list of questions, tracks the score, and displays feedback.
- **`if __name__ == "__main__":`**: Ensures that `run_quiz()` only executes if the script is run directly, allowing future import and integration into larger projects.

---

## Example Usage

Here’s what an example game session might look like:

```plaintext
What is the capital of France?
1. Berlin
2. Madrid
3. Paris
4. Rome
Your answer (1-4): 2
Incorrect! The correct answer was Paris.

Which planet is known as the Red Planet?
1. Earth
2. Venus
3. Mars
4. Jupiter
Your answer (1-4): 3
Correct!

Quiz Over!
Your final score is 1/2.
```

---

## Contributing

Contributions are welcome! If you’d like to suggest improvements, add new features, or fix issues:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute this software as you see fit.

---

Enjoy the quiz, and happy coding! 🎉
