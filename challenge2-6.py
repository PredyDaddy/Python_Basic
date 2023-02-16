from cgitb import text
import code


class Borrower:
    """Represents a person that can borrow books"""

    newIdCode = 1;    # Class variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.newIdCode
        Borrower.newIdCode += 1     # Updates for next new borrower ...
        self.booksBorrowed = []

    def borrowBook(self,book):
        self.booksBorrowed.append(book)
       
    def showAllbooks(self):
        for c in self.booksBorrowed:
            print(c)

    def showBorrowerDetails(self,bor):
        print('Lending book',,'to',self.firstname,self.lastname)
        print(self.firstname,self.lastname,'id:')

class Book:
    """A class to represent a book in a library"""
    def __init__(self,title,author,code) -> None:
         self.title = title
         self.author = author
         self.code = code
         self.onloan = True
    
    def showTitle(self,title):
        print('Lending book',self.title,'to',self.author)
        print(self.author,'id:',self.code)

class Library:
    """A class to represent a lending library"""
    def __init__(self) -> None:
        self.allborrowers = []
        self.allbooks = []

    def addBook(self,book):
        self.allbooks.append(book.title)

    def addBorrower(self,bor):    
        z = bor.FN +' '+ bor.LN
        self.allborrowers.append(z)

    def lendbook(self,bor,book):    
        if book.onloan:
            print('Sorry thats already on loan')
        else:
            z = bor.FN +' '+ bor.LN
            if z in self.allborrowers:
                book.onloan = True
                bor.borrowBook(book.title)
                print('Lending book',book.title,'to',z)
            else:
                print('404 Bad Gateway')



         


def main():
    ## Create some books ...
    book1 = Book('Kafkas motorbike','Bridget Jones', 1290)
    book2 = Book('Cooking with Custard','Jello Biafra', 1002)
    book3 = Book('History of Bagpipes','John Cairncross', 987)

    # Put the books in the library
    library = Library()     # Creates the library
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)

    # Create some borrowers ...
    bor1 = Borrower('Kevin','Wilson')
    bor2 = Borrower('Rita','Shapiro')
    bor3 = Borrower('Max','Normal')

    library.addBorrower(bor1)
    library.addBorrower(bor2)
    library.addBorrower(bor3)

    # make some loans ...
    library.lendBook(bor1, book1)
    bor1.showBorrowerDetails()
    bor1.showAllBooks()
    library.lendBook(bor2,book3)
    bor2.showBorrowerDetails()
    bor2.showAllBooks()
    # Try to lend book3 out again ....
    library.lendBook(bor3,book3)

if __name__ == "__main__":
        main()
