def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "B"
    },
    {
        "prompt": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Au", "C. Fe", "D.  Pb"],
        "answer": "B"
    },
    {
        "prompt": "Which country is hosting the 2024 Olympic Games?",
        "options": ["A. Japan", "B. USA", "C. France", "D. Germany"],
        "answer": "C"
    },
    {
        "prompt": "Which is the longest river in the world?",
        "options": ["A. Amazon", "B. Yangtze", "C. Mississippi", "D. Nile"],
        "answer": "D"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
{
        "prompt": "Which country gave the Statue of Liberty to the United States?",
        "options": ["A. Germany", "B. France", "C. United Kingdom", "D. Spain"],
        "answer": "B"
    }
]

# Run the quiz
run_quiz(questions)