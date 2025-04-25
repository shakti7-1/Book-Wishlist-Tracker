# Define a Book class with title, author, and genre
class Book:
    def __init__(self, title, author, genre):
        # Initialize the book's attributes
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        # Return a formatted string when printing the book
        return f"{self.title} by {self.author} [{self.genre}]"

# List to store all books added to the wishlist
wishlist = []

# Function to add a new book to the wishlist
def add_book():
    title = input("Book title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    wishlist.append(Book(title, author, genre))  # Add book to list

# Function to display all books in the wishlist
def view_wishlist():
    for i, book in enumerate(wishlist, 1):  # Show books with numbers
        print(f"{i}. {book}")

# Function to remove a book from the wishlist by index
def remove_book():
    view_wishlist()
    idx = int(input("Remove which book? ")) - 1
    if 0 <= idx < len(wishlist):  # Check if valid index
        wishlist.pop(idx)         # Remove book from list
        print("Removed!")

# Main function to display menu and handle user choices
def main():
    while True:
        print("\n1. Add Book\n2. View Wishlist\n3. Remove Book\n4. Exit")
        ch = input("Choice: ")
        if ch == "1":
            add_book()
        elif ch == "2":
            view_wishlist()
        elif ch == "3":
            remove_book()
        elif ch == "4":
            break

# Start the program
if __name__ == "__main__":
    main()
