users = []
books = []


class User:
    def __init__(self, name):
        self.name = name

    def addUser(self):
        for user in users:
            if self.name == user:
                print("User already exists!")
            else:
                users.append(self.name)
                print(users)
                print(f"User {self.name} has been added.")

class Book:
    def __init__(self, title, author, status, duedate, fine):
        self.title = title
        self.author = author
        self.status = status
        self.duedate = duedate
        self.fine = fine

    def addBook(self):
        for book in books:
            if self.title == book["title"] & self.author == book["author"]:
                print("Book already exists")
            else:
                book = {"title": self.title, "author": self.author, "status": self.status}
                books.append(book)
        













while True:
    print("Welcome to the library! \n What would you like to do today?")
    print("Choose from the following options: \n "
          "1. Add a user \n"
          "2. View users\n"
          "3. Add a book\n"
          "4. View books\n"
          "5. Borrow a book \n"
          "6. Return a book\n"
          "7.Remove a user\n"
          "8. Remove a book\n"
          "9. Exit the library")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid choice. Enter a valid choice (1-5)")
    else:
        if choice == 1:
            username = input("Enter the username: ")
            user = User(username)
            user.addUser()
            print(f"User {username} has been added.")
        elif choice == 2:
            if users:
                for i, user, in enumerate(users, start=1):
                    print(f"{i}. {user.name} ")
            else:
                print("No users to show.")

