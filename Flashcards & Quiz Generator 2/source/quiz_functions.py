import random as rn
from file_manager import save_quiz_result

def quiz_multiple_choice(flashcards):
    """
    Multiple-choice quiz based on the flashcards dictionary.
    """
    if not flashcards:
        print("No flashcards available. Please add flashcards first to start the quiz.")
        return

    questions = list(flashcards.keys())
    rn.shuffle(questions)

    score = 0
    total_score = len(questions)

    for question in questions:
        correct_answer = flashcards[question]
        wrong_answers = [flashcards[q] for q in questions if q != question]
      
        if len(wrong_answers) >= 3:
            choices = rn.sample(wrong_answers, 3)
        else:
            choices = wrong_answers.copy()

        choices.append(correct_answer)
        rn.shuffle(choices)

        print(f"\nWhat is the definition of '{question}'?")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")

        answer = input(f"Your answer (1-{len(choices)}): ").strip()

        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= len(choices) and choices[answer - 1] == correct_answer:
                print("Correct! Good job.")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
        else:
            print(f"Invalid input! Please enter a number between 1 and {len(choices)}.")

    print(f"\nQuiz completed! Your final score is {score} out of {total_score}.")
    save_quiz_result(score, total_score)

def quiz_open_answer(flashcards):
    """
    Open-answer quiz: user types the definition.
    """
    if not flashcards:
        print("No flashcards available. Please add flashcards first to start the quiz.")
        return

    questions = list(flashcards.keys())
    rn.shuffle(questions)

    score = 0
    total_score = len(questions)

    for question in questions:
        correct_answer = flashcards[question].strip().lower()
        user_answer = input(f"\nWhat is the definition of '{question}'? ").strip().lower()

        if user_answer == correct_answer:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {flashcards[question]}")

    print(f"\nQuiz completed! Your final score is {score} out of {total_score}.")
    save_quiz_result(score, total_score)