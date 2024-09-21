# Initial data
books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
tags = {"classic", "dystopian", "novel", "literature"}

# a. Access the second book's author from the books tuple and print it
second_book_author = books[1][1]  # Access the second book (index 1) and get the author (index 1 within the book)
print("Author of the second book:", second_book_author)

# b. Add a new record for the book "Brave New World" by Aldous Huxley, published in 1932
# Since tuples are immutable, we create a new tuple by concatenating the new record
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print("\nUpdated books tuple:")
print(books)

# c. Unpack the details of the third book into separate variables and print them
title, author, year = books[2]  # Unpacking the third book
print(f"\nThird book details:\nTitle: {title}\nAuthor: {author}\nYear: {year}")

# d. Loop through the books tuple and print each book's title
print("\nBook Titles:")
for book in books:
    print(book[0])  # Access the title (index 0) of each book

# e. Add a new tag "sci-fi" to the tags set and print the updated set
tags.add("sci-fi")
print("\nUpdated tags set after adding 'sci-fi':")
print(tags)

# f. Use a method to remove the tag "novel" from the tags set and print the updated set
tags.discard("novel")  # discard() will not raise an error if the tag doesn't exist
print("\nUpdated tags set after removing 'novel':")
print(tags)