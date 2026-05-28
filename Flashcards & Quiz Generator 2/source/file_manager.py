import os
from datetime import datetime
flashcards_file = "data/flashcards.txt"
statistics_file = "data/quiz_stats.txt"

def loading_flashcards():
    """Function which loads flashcards from flashcards_file 
    return: a dictionary {term: definition}
    """
    
    flashcards = {}
    
    if not os.path.exists(flashcards_file):
        return flashcards
    
    with open(flashcards_file, "r", encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                term, definition = line.split(" | ", 1)
            except ValueError:
                continue
            term = term.strip()
            definition = definition.strip()
            if term:
                flashcards[term] = definition
        return flashcards

def save_flashcards(flashcards):
    """Function which saves user's cards dictionary to flashcards_file
    argument: flashcards(dict)
    return: None
    """
    os.makedirs(os.path.dirname(flashcards_file), exist_ok=True)
    with open(flashcards_file, "w", encoding = "utf-8") as f:
        for term, definition in flashcards.items():
            line = f"{term} | {definition}\n"
            f.write(line)
    print("Your flashcards have been saved!")

def save_quiz_result(score, total):
    """Function which records the result of a quiz attempt
    arguments: score(int) - number of correct answers, total(int) - total number of questions
    return: None"""
    
    if total <= 0:
        return
    percentage = round((score / total) * 100)
    timestamp = datetime.now().strftime("%D-%m-%y %H:%M")
    line = f"{score}/{total} | {percentage}% | {timestamp}\n"
    os.makedirs(os.path.dirname(statistics_file), exist_ok=True)
    with open(statistics_file, "a", encoding="utf-8") as f:
        f.write(line)

def show_quiz_results():
    """Function which prints all attempted quiz results"""
    
    if not os.path.exists(statistics_file):
        print("No quiz results are available yet.")
        return
    
    with open(statistics_file, "r", encoding = "utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        
        if not lines:
            print("No quiz results are available yet.")
            return
        print("Your Quiz History: ")
        for i, line in enumerate(lines, start = 1):
            print(f"{i}. {line}")

    
               
    

    