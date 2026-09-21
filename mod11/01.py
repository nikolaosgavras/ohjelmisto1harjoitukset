class Publication:
    def __init__(self, publicationName):
        self.publication_name = publicationName

class Book(Publication):
    def __init__(self, publicationName, bookAuthor, pageCount):
        self.book_author = bookAuthor
        self.book_page_count = pageCount
        super().__init__(publicationName)

    def print_information(self):
        print(f"Publication name: {self.publication_name}\nBook author: {self.book_author}\nBook page count: {self.book_page_count}")

class Magazine(Publication):
    def __init__(self, publicationName, chiefEditor):
        self.chief_editor = chiefEditor
        super().__init__(publicationName)

    def print_information(self):
            print(f"Publication name: {self.publication_name}\nMagazine chief editor: {self.chief_editor}")

donaldduck = Magazine("Donald Duck", "Aki Hyyppä")
compartment6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donaldduck.print_information()
compartment6.print_information()