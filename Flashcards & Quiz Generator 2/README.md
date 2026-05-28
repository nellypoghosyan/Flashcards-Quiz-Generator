**Project Name:**  
QuizBrains

**Team members:**  
Mane Karapetyan  
Nelli Poghosyan  
Rozeta Gevorgyan

**Overview:**  
A text-based Flashcards & Quiz Generator that allows users to create, edit, and study flashcards. It includes multiple quiz modes and a simple menu-driven interface.

**How to run:**

**Windows (PowerShell, Command Prompt, or Windows Terminal)**

1. Open **PowerShell**, **Command Prompt**, or **Windows Terminal**

2. Navigate to the project folder:  
   cd "Flashcards & Quiz Generator"  
3. Run the program:  
   python source\\main.py

### **macOS / Linux (Terminal)**

1. Open **Terminal**

2. Navigate to the project folder:  
   cd "Flashcards & Quiz Generator"  
3. Run the program:  
   python3 source/main.py

## **Running the Program in an IDE**

### **PyCharm**

1. Open **PyCharm**

2. **File → Open…** → select the project folder

3. Open source/main.py

4. **Run** the program

### **VS Code**

1. Open **VS Code**

2. **File → Open Folder…** → select the project folder

3. Open source/main.py

4. **Run** the program

**Features implemented:**

### **Managing Flashcards:**

* Add new flashcards

* Edit existing flashcards

* Delete flashcards

* View a list containing all saved flashcards

* Automatic prevention of empty or invalid entries

### **Quiz System:**

* **Multiple-choice quiz:**

  * randomized order of questions

  * randomized answer choices

  * automatic scoring and feedback for the user

* **Open-answer quiz:**

  * user is asked for typed definitions

  * automatic feedback for the user

  * automatic scoring

### **File Handling:**

* Load flashcards automatically at the start of the program

* Save updated flashcards to file

* Save quiz results with:

  * score

  * total number of questions in the quiz

  * score in percentage form

  * timestamp

* Show full quiz history

* Automatically create the data/ folder if it is missing

### **User Interface:**

* Clear, numbered main menu

* Text-based interaction

* Input validation for:

  * empty answers

  * invalid menu options

  * insufficient flashcards for quizzes

### **Project Structure:**

* Modular design (file\_manager.py, flashcards\_functions.py, quiz\_functions.py, main.py)

* Functions with docstrings

* Organized source/ and data/ folders

* Portable across Windows, macOS, and Linux

**File Formats Used:**

**.txt files** \- used to store all saved data for the program

flashcards.txt \- contains flashcards  
quiz\_stats.txt \- stores quiz results 

**.py files** \- all source code is written in Python

file\_manager.py — handles loading, saving, and checking data files  
main.py — main program and menu  
flashcards\_functions.py \- flashcard management  
quiz\_functions.py \- quiz system

