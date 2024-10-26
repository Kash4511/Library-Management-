def library ():
    while True:
        print(" ---------------")
        print(" |1.View Books |\n |2.Borrow Book|\n |3.Return Book|\n |4.Add a Book |")
        print(" ---------------")
        pick = input("Enter your choice(Enter number wise): ")
        if pick == '1':
            print(" 1.View all books\n 2.Search by Genre\n 3.Search a book specifically")
            Books = {"To Kill a Mockingbird": "Harper Lee",
                    "1984": "George Orwell",
                    "The Great Gatsby": "F. Scott Fitzgerald",
                    "Pride and Prejudice": "Jane Austen",
                    "The Catcher in the Rye": "J.D. Salinger",
                    "Moby Dick": "Herman Melville",
                    "Beloved": "Toni Morrison"}
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
                    print(f"{specific} by {Books[specific]}")
                else:
                    print("The book is not available")
            else:
                print("Invalid")

library()
          

        
        
        