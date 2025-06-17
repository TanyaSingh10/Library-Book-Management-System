'''
Problem:
A library wants to manage its books using Python. 

Each book has:
Title
Author
Genre
Year of publication

Tasks:
Take input for 5 books and store them using a list of dictionaries.
Create a set of all unique genres.
Create a tuple of all authors.
Print all books published after 2010.
Add a new book and remove an old one based on title.
'''

#books in a list of dictionaries
books = [
    {"Title":"Gone Girl", "Author":"Gillian Flynn", "Genre":"crime thriller","Year":2012},
    {"Title":"Life After Life", "Author":"Kate Atkinson", "Genre":"Spice of Life","Year":2003},
    {"Title":"Americanah", "Author":"Chimamanda Ngozi", "Genre":"Fiction","Year":2013},
    {"Title":"Normal People", "Author":"Sally Rooney", "Genre":"Love","Year":2018},
    {"Title":"Tenth of December", "Author":"George Saunders", "Genre":"Love","Year":2014}
] 

#set of genres
genres = {book["Genre"] for book in books}
print("Unique Genres: ",genres)

#tuple of authors
authors = tuple(book["Author"] for book in books)
print("All Authors: ",authors)

print("Books published after 2010: ")
for book in books:
    if book["Year"]>2010:
        print(book)

new = {"Title":"Salvage the Bones", "Author":"Jesmyn Ward", "Genre":"History","Year":"2011"}
books.append(new)
print("\nAdded one: ",books)

remove_bt = "Tenth of December"
for book in books:
    if book["Title"] == remove_bt:
        books.remove(book)
        print(f"Book '{remove_bt}' removed successfully!")
        break
    else:
        print(f"Book '{remove_bt}' not removed.")

print("\nAfter removal: ",books)
for book in books:
    print(book)