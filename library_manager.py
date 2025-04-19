import os
import json

def load_library():
    """Load library from file if it exists, otherwise return empty list."""
    if os.path.exists("library.txt"):
        try:
            with open("library.txt", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading library file. Starting with empty library.")
            return []
    return []

def save_library(library):
    """Save library to file."""
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=2)
    print("Library saved to file.")

def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    
    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("Please enter a valid year.")
    
    genre = input("Enter the genre: ").strip()
    
    while True:
        read = input("Have you read this book? (yes/no): ").lower()
        if read in ['yes', 'no']:
            read_status = read == 'yes'
            break
        print("Please enter 'yes' or 'no'.")
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ").strip()
    initial_len = len(library)
    
    library[:] = [book for book in library if book["title"].lower() != title.lower()]
    
    if len(library) < initial_len:
        print("Book removed successfully!")
    else:
        print("Book not found.")

def search_books(library):
    """Search for books by title or author."""
    print("Search by:")
    print("1. Title")
    print("2. Author")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        search_term = input("Enter the title: ").strip().lower()
        matches = [book for book in library if search_term in book["title"].lower()]
    elif choice == "2":
        search_term = input("Enter the author: ").strip().lower()
        matches = [book for book in library if search_term in book["author"].lower()]
    else:
        print("Invalid choice.")
        return
    
    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_stats(library):
    """Display library statistics."""
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty.")
        return
    
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.1f}%")

def main():
    """Main program loop."""
    library = load_library()
    
    while True:
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()