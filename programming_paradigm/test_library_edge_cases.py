from library_management import Book, Library

def test_edge_cases():
    library = Library()
    
    # Test with empty library
    print("Testing empty library:")
    print("Available books in empty library:")
    library.list_available_books()
    
    # Add some books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    
    print("\nAfter adding books:")
    library.list_available_books()
    
    # Test checking out non-existent book
    print(f"\nTrying to check out non-existent book: {library.check_out_book('Non-existent Book')}")
    
    # Test checking out existing book
    print(f"Checking out 'The Great Gatsby': {library.check_out_book('The Great Gatsby')}")
    
    # Test checking out already checked out book
    print(f"Trying to check out 'The Great Gatsby' again: {library.check_out_book('The Great Gatsby')}")
    
    print("\nAvailable books after checkout:")
    library.list_available_books()
    
    # Test returning non-existent book
    print(f"\nTrying to return non-existent book: {library.return_book('Non-existent Book')}")
    
    # Test returning book that's not checked out
    print(f"Trying to return 'To Kill a Mockingbird' (not checked out): {library.return_book('To Kill a Mockingbird')}")
    
    # Test returning checked out book
    print(f"Returning 'The Great Gatsby': {library.return_book('The Great Gatsby')}")
    
    print("\nFinal available books:")
    library.list_available_books()

if __name__ == "__main__":
    test_edge_cases()
