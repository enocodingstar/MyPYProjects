class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id

    def __str__(self):
        return f"Name: {self.username}, ID: {self.id}"
    
class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.borrowed = False
        self.borrowed_by = None

    def __str__(self):
        borrowed_status = f"Yes, by {self.borrowed_by}" if self.borrowed else "No"
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Borrowed: {borrowed_status}"
    

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def addBooks(self, book):
        for current_book in self.books:
            if current_book.id == book.id:
                print("Book already exists.")
                return
        self.books.append(book)
        print(f"Book: {book.title} has been added to the library")

    def viewBooks(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book) 
    
    def addUsers(self, user):
        for current_user in self.users:
            if current_user.id == user.id:
                print(f"User already exists.")
                return
        self.users.append(user)
        print(f"User {user.username} with ID {user.id} has been added to the library.")

    def viewUsers(self):
        if not self.users:
            print("No users to show.")
            return
        for user in self.users:
            print(user)

    def borrowBooks(self, user_id, book_id):
        if not any(user.id == user_id for user in self.users):
            print(f"User ID {user_id} doesn't exist.")
            return
        for book in self.books:
            if book.id == book_id and not book.borrowed:
                book.borrowed = True
                book.borrowed_by = f" User with ID {user_id}"
                print(f"You have borrowed '{book.title}'.")
                return
        print("Book isn't availlable or has been borrowed.")

    def returnBooks(self, book_id):
        if not any(book.id == book_id for book in self.books):
            print(f"Book with ID {book_id} doesn't exist.")
            return
        for book in self.books:
            if book.id == book_id and book.borrowed:
                book.borrowed = False
                book.borrowed_by = None
                print(f"You have returned '{book.title}'.")
                return
        print(f"Book with ID {book_id} is not borrowed and can't be returned.") 

    def removeBooks(self, book_id):
        if not any(book.id == book_id for book in self.books):
            print(f"Book with ID {book_id} does not exist.")
            return
        for book in self.books:
            if book.id == book_id:
                print(f"You have removed {book.title} from the library.")
                self.books.remove(book)

    def removeUsers(self, user_id):
        if not any(user.id == user_id for user in self.users):
            print(f"User with ID {user_id} does not exist.")
            return
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                print(f"User {user.title} with ID {user.id} has been removed from the library.")



def main():
    my_library = Library()
    while True:
        print("Welcome to the library. \n What would you like to do today?")
        print("Choose from the following options: \n"
            "1. Add a user\n"
            "2. Add a book\n"
            "3. View all users\n"
            "4. View all books\n"
            "5. Borrow a book\n"
            "6. Return a book\n"
            "7. Remove a book\n"
            "8. Remove a user\n"
            "9. Exit the library")
        
        try:
            choice = int(input("Choose an option (1-9): "))
        except ValueError:
            print("Enter a valid option.")
        else:
            if choice == 1:
                username = input("Enter a username: ").strip()
                try:
                    ID = int(input("Enter an ID for the user: "))
                except ValueError:
                    print("Enter a valid ID.")
                else:
                    my_library.addUsers(User(username, ID))
            elif choice == 2:
                try:
                    id = int(input("Enter an ID for the book: "))
                except ValueError:
                    print("Enter a valid ID.")
                else:
                    title = input("Enter the book title: ").strip()
                    author = input("Enter the author of the book: ").strip()
                    my_library.addBooks(Book(id, title, author))
            elif choice == 3:
                my_library.viewUsers()
            elif choice == 4:
                my_library.viewBooks()
            elif choice  == 5:
                user_id = int(input("Enter the user id: "))
                book_id = int(input("Enter the book id: "))
                my_library.borrowBooks(user_id,book_id)
            elif choice == 6:
                book_id = int(input("Enter a book ID: "))
                my_library.returnBooks(book_id)
            elif choice == 7:
                book_id = int(input("Enter a book ID:"))
                my_library.removeBooks(book_id)
            elif choice == 8:
                user_id = int(input("Enter a user ID: "))
                my_library.removeUsers(user_id)
            elif choice == 9:
                print("Thanks for using the library today!\n Exiting the library......")
                break
            







if __name__ == "__main__":
    main()                


