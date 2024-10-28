def library_ID (used_LID):
    while True:
        LID = input("Enter your Library ID: ")
        if LID in used_LID:
            print("The Library ID has already Logged in: ")
            continue
        if "LID" in LID:
            print(f"Your Library ID is {LID}")
            used_LID.append(LID)
            return True
        
        else:
            print("invalid Library ID..")
            continue


def library(borrowed_book):
    Books = {
        "To Kill a Mockingbird": "Harper Lee",
        "One Hundred Years of Solitude": "by Gabriel Garcia Marquez",
        "War and Peace": "by Leo Tolstoy",
        "Beloved by": "Toni Morrison",
        "1984": "George Orwell",
        "The Great Gatsby": "F. Scott Fitzgerald",
        "Pride and Prejudice": "Jane Austen",
        "The Catcher in the Rye": "J.D. Salinger",
        "Moby Dick": "Herman Melville",
        "Beloved": "Toni Morrison"
    }

    if not library_ID(used_LID):
        print("No valid Library ID entered.")
        return

    while True:
        print(" ---------------")
        print(" |1. View Books |\n |2. Borrow Book|\n |3. Return Book|\n |4. Add a Book |\n |5.Exit|")
        print(" ---------------")
        pick = input("Enter your choice (Enter number): ")

        if pick == '1':
            print(" 1. View all books\n 2. Search by Genre\n 3. Search a book specifically")
            search_book = input("Enter your choice (number): ")
            if search_book == '1':
                for book, author in Books.items():
                    print(f"|{book} by {author}|\n")
            elif search_book == '2':
                genres = {
                    "Historical Fiction": [
                        "To Kill a Mockingbird by Harper Lee",
                        "One Hundred Years of Solitude by Gabriel Garcia Marquez",
                        "War and Peace by Leo Tolstoy",
                        "Beloved by Toni Morrison"
                    ],
                    "Dystopian & Science Fiction": ["1984 by George Orwell"],
                    "Classic / Tragedy": ["The Great Gatsby by F. Scott Fitzgerald"],
                    "Romance / Satire": ["Pride and Prejudice by Jane Austen"],
                    "Coming-of-Age": ["The Catcher in the Rye by J.D. Salinger"],
                    "Adventure / Epic": ["Moby Dick by Herman Melville"],
                    "Fantasy / Adventure": ["The Hobbit by J.R.R. Tolkien"]
                }
                for genre, books in genres.items():
                    print(f"|{genre}:\n{books}|\n")
            elif search_book == '3':
                specific = input("Enter the book you want to search: ")
                if specific in Books:
                    print(f"{specific} by {Books[specific]}")
                else:
                    print("The book is not available.")
            else:
                print("Invalid choice.")
        
        elif pick == '2':
            for book, author in Books.items():
                print(f"|{book} by {author}|\n")
            borrow_book = input("Enter the book you want to borrow: ")
            if borrow_book in Books:
                if borrow_book in borrowed_book:
                    print("The book is currently unavailable as it has already been borrowed.")
                else:
                    Yes_or_no = input(f"The selected book is '{borrow_book}' by {Books[borrow_book]}. Do you want to borrow? (Yes/No): ").lower()
                    if Yes_or_no == 'yes':  
                        borrowed_book.append(borrow_book)
                        print(f"The book '{borrow_book}' has been borrowed by you.")
                    else:
                        print("Cancelling...")
            else:
                print("The entered book is not in our library collection.")

        elif pick == '3':
            print("Borrowed books:", borrowed_book)
            return_book = input("Enter the book you want to return: ")
            if return_book in borrowed_book:
                y_or_no = input(f"Are you sure you want to return '{return_book}'? (Yes/No): ").lower()
                if y_or_no == 'yes':
                    borrowed_book.remove(return_book)
                    print(f"The book '{return_book}' has been returned.")
                else:
                    print("Cancelling...")
            else:
                print("This book was not borrowed or does not exist.")

        elif pick == '4':
            y_or_no = input("Do you want to add a book? (Yes/No): ").lower()
            if y_or_no == 'yes':
                add_book = input("Enter the new book title: ")
                add_author = input("Enter the author of the book: ")
                Books[add_book] = add_author
                print(f"You added '{add_book}' by {add_author} to the library.")
            else:
                print("Cancelling...")

        else:
            print("Exiting...")
            break  

used_LID = []
borrowed_id = []
library(borrowed_id)
                    

        
        
        
