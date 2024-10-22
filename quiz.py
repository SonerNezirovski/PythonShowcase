import random
import time
def quiz_interactive():
    total_score = 0

    questions = [
        {
            "question": "How much is 5+5?",
            "options": ["1. 10", "2. 2", "3. 6", "4. 20"],
            "correct": 1
        },
        {
            "question": "What is the formula of water?",
            "options": ["1. CO2", "2. H2O", "3. NaCl", "4. O2"],
            "correct": 2
        },
        {
            "question": "How much is 7 + 8?",
            "options": ["1. 14", "2. 15", "3. 16", "4. 17"],
            "correct": 2
        }
    ]
    random.shuffle(questions)

    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        random_options = random.sample(question['options'], len(question['options']))  # Shuffle options
        for option in random_options:
            print(option)
        answer = int(input("Enter the number of your answer: "))
        if answer == question['correct']:
            print("Correct answer!")
            total_score += 1
        else:
            print(f"Wrong answer! The correct answer was option {question['correct']}.")

        time.sleep(1)

    print(f"\nYou completed the quiz! Your final score is {total_score} out of {len(questions)}.")
quiz_interactive()
