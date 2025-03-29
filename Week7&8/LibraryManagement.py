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
                books.append()











while True:
    print("Welcome to the library! \n What would you like to do today?")
    print("Choose from the following options: \n "
          "1. Add a user \n"
          "2. View users\n"
          "3. Add a book\n"
          "4. View books\n")                
