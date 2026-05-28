from file_manager import (
    loading_flashcards,
    save_flashcards,
    show_quiz_results
)
from flashcards_functions import (
    add_flashcard,
    edit_flashcard,
    delete_flashcard,
    list_flashcards
)
from quiz_functions import (
    quiz_multiple_choice,
    quiz_open_answer
)

def main_menu():
    """
    Main menu for the Flashcards & Quiz program.
    """
    flashcards = loading_flashcards()

    while True:
        print("\n=== Flashcards & Quiz Generator ===")
        print("1. Add flashcard")
        print("2. Edit flashcard")
        print("3. Delete flashcard")
        print("4. List flashcards")
        print("5. Quiz (multiple choice)")
        print("6. Quiz (open answer)")
        print("7. Show quiz history")
        print("8. Save and exit")

        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            edit_flashcard(flashcards)
        elif choice == "3":
            delete_flashcard(flashcards)
        elif choice == "4":
            list_flashcards(flashcards)
        elif choice == "5":
            quiz_multiple_choice(flashcards)
        elif choice == "6":
            quiz_open_answer(flashcards)
        elif choice == "7":
            show_quiz_results()
        elif choice == "8":
            save_flashcards(flashcards)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
