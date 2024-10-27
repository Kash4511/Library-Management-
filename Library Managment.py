def library (borrowed_book):
    Books = {"To Kill a Mockingbird": "Harper Lee",
                    "One Hundred Years of Solitude": "by Gabriel Garcia Marquez",
                    "War and Peace":"by Leo Tolstoy",
                    "Beloved by":" Toni Morrison",
                    "1984": "George Orwell",
                    "The Great Gatsby": "F. Scott Fitzgerald",
                    "Pride and Prejudice": "Jane Austen",
                    "The Catcher in the Rye": "J.D. Salinger",
                    "Moby Dick": "Herman Melville",
                    "Beloved": "Toni Morrison"}
    while True:
        print(" ---------------")
        print(" |1.View Books |\n |2.Borrow Book|\n |3.Return Book|\n |4.Add a Book |")
        print(" ---------------")
        pick = input("Enter your choice(Enter number wise): ")
        if pick == '1':
            print(" 1.View all books\n 2.Search by Genre\n 3.Search a book specifically")
            print("All the Books ")
            search_book= input("Enter what you want to search(enter number wise): ")
            if search_book == '1':
                for book, author in Books.items():
                    print(f"\n |{book} by {author}|")
                    continue
            elif search_book == '2':
                genres = {"Historical Fiction": ["To Kill a Mockingbird by Harper Lee",
                                                "One Hundred Years of Solitude by Gabriel Garcia Marquez",
                                                "War and Peace by Leo Tolstoy",
                                            "   Beloved by Toni Morrison"],
                         "Dystopian & Science Fiction": ["1984 by George Orwell"], 
                         "Classic / Tragedy": ["The Great Gatsby by F. Scott Fitzgerald"],
                         "Romance / Satire":["Pride and Prejudice by Jane Austen"],
                         "Coming-of-Age": ["The Catcher in the Rye by J.D. Salinger"],
                         "Adventure / Epic":["Moby Dick by Herman Melville"],
                         "Fantasy / Adventure":["The Hobbit by J.R.R. Tolkien"]}
                for genre, books in genres.items():
                    print(f"|{genre}|:\n{books}\n ")
                    continue 
            elif search_book == '3':
                specific = input("Enter the book that you want to Search: ")
                if specific in Books:
                    
                    print(f"|{specific} by {Books[specific]}|")
                else:
                    print("The book is not available")
            else:
                print("Invalid")
        elif pick == '2':
            for book, author in Books.items():
                    print(f"\n |{book} by {author}|")
            borrow_book = input("Enter the book you want to borrow: ")
            if borrow_book in Books:
                if borrow_book in borrowed_book:
                    print("The book is currently unavailable as it has already been borrowed.")
                else:
                    Yes_or_no = input(f"The selected book is '{borrow_book}' by {Books[borrow_book]}. Do you want to borrow? (Yes/No): ").lower()
                    if Yes_or_no == 'yes':  
                        borrowed_book.append(borrow_book)
                        print(f"The Book '{borrow_book}' has been borrowed by you from the library!")
                    else:
                        print("Cancelling...")
            else:
                print("The entered book is not in our library collection.")
borrowed_book = []
library(borrowed_book)

        
        
        
