from file_manager import save_flashcards

def add_flashcard(flashcards):
    """
    Adds a new flashcard to the given dictionary.
    flashcards (dict): {term: definition}
    """
    term = input("Enter the term of your flashcard: ").strip()

    if term == "":
        print("Invalid input: term cannot be empty.")
        return

    if term in flashcards:
        overwrite = input("This term already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite == "yes":
            definition = input("Enter the new definition: ").strip()
            if definition == "":
                print("Invalid input: definition cannot be empty.")
                return
            flashcards[term] = definition
            print("Flashcard updated.")
            save_flashcards(flashcards)  
        elif overwrite == "no":
            print("No changes have been made.")
        else:
            print("Invalid input.")
    else:
        definition = input("Enter the definition of your term: ").strip()
        if definition == "":
            print("Invalid input: definition cannot be empty.")
            return
        flashcards[term] = definition
        print("Flashcard added.")
        save_flashcards(flashcards)      


def edit_flashcard(flashcards):
    """
    Edits the definition of an existing flashcard.
    """
    term = input("Enter the term you want to change the definition for: ").strip()

    if term not in flashcards:
        print("No such flashcard detected.")
        return

    new_definition = input("Enter the new definition: ").strip()

    if new_definition == "":
        print("Invalid input: definition cannot be empty.")
        return

    flashcards[term] = new_definition
    print("Flashcard updated.")
    save_flashcards(flashcards)  



def delete_flashcard(flashcards):
    """
    Deletes an existing flashcard from the dictionary.
    """
    term = input("Enter the name of the flashcard you want to remove: ").strip()

    if term == "":
        print("Invalid input: term cannot be empty.")
        return

    if term not in flashcards:
        print("No such flashcard detected.")
        return

    del flashcards[term]
    print("Flashcard deleted as requested.")
    save_flashcards(flashcards)  



def list_flashcards(flashcards):
    """
    Prints all flashcards in a numbered list.
    """
    if not flashcards:
        print("No flashcards available.")
        return

    print("\nYour flashcards:")
    for i, (term, definition) in enumerate(flashcards.items(), start=1):
        print(f"{i}. {term} – {definition}")
