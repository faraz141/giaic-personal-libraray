Personal Library Manager
Overview
The Personal Library Manager is a command-line Python application that allows users to manage their book collection. Users can add, remove, search, and display books, as well as view basic statistics about their library. The program stores book details such as title, author, publication year, genre, and read status. It also includes optional file handling to save and load the library to/from a library.txt file.
Features

Add a Book: Input details (title, author, year, genre, read status) to add a book to the library.
Remove a Book: Remove a book by its title.
Search for a Book: Search books by title or author, displaying matching results.
Display All Books: List all books with their details in a formatted manner.
Display Statistics: Show the total number of books and the percentage of books read.
File Handling: Automatically save the library to library.txt on exit and load it on startup.
User-Friendly Menu: Navigate the program using a simple numbered menu.

Requirements

Python 3.6 or later: The program uses standard Python libraries (os and json), so no additional packages are required.
A terminal or command-line interface to run the script.

Installation

Download the Script:

Save the library_manager.py file to a directory of your choice (e.g., ~/Desktop).


Verify Python Installation:

Ensure Python is installed by running:
python --version

or
python3 --version


If Python is not installed, download it from python.org.




Usage

Navigate to the Directory:

Open a terminal and use the cd command to navigate to the folder containing library_manager.py. For example:
cd ~/Desktop




Run the Program:

Execute the script using:
python library_manager.py

or
python3 library_manager.py




Interact with the Menu:

The program displays a menu with six options:
Menu
Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice:


Enter a number (1–6) to select an option and follow the prompts.



File Handling:

The library is automatically saved to library.txt in the same directory when you exit (option 6).
On startup, the program loads the library from library.txt if it exists.



Sample Output
Adding a Book
Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book added successfully!

Displaying All Books
Your Library:
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read
2. 1984 by George Orwell (1949) - Dystopian - Unread

Displaying Statistics
Total books: 2
Percentage read: 50.0%

File Structure

library_manager.py: The main Python script containing the application logic.
library.txt: A JSON-formatted file (created automatically) that stores the library data.

Troubleshooting

"python: command not found": Ensure Python is installed and added to your system's PATH. Try using python3 instead of python.
File Not Found: Verify that library_manager.py is in the current directory (use ls or dir to check).
Invalid Input: The program includes input validation (e.g., for publication year and read status). Follow the prompts carefully.
File Corrupted: If library.txt is corrupted, the program will start with an empty library and print an error message.

Notes

The program is case-insensitive for title and author searches and removals.

The library is stored as a list of dictionaries, with each book represented as:
{
  "title": "Book Title",
  "author": "Author Name",
  "year": 2020,
  "genre": "Genre",
  "read": true
}


The program does not require any external dependencies beyond the Python standard library.


Future Improvements

Add sorting options (e.g., by title, author, or year).
Support editing existing book details.
Add more advanced search filters (e.g., by genre or year).
Implement a graphical user interface (GUI).

License
This project is open-source and available for personal use. Feel free to modify and share it!
Contact
For questions or suggestions, please open an issue or contact the developer.
Happy reading!
