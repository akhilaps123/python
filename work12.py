def mini_library():
    try: 
        book = (input("Enter a book title:"))
        if not book.replace(" ","").isalpha():
            raise ValueError("Error ,book title contains only alphabets and spaces")
        
        publication_year = (input("Enter publication year:"))
        if not (publication_year.isdigit() and len(publication_year)== 4 and (publication_year.startswith("19") or publication_year.startswith("20"))):
            raise ValueError("Error,the publication year must be a 4-digit number starting with '19' or '20'.")
        print("\n Book added successfully")
        print(f"Title:{book}")
        print(f"publication_year:{publication_year}")
    
    except ValueError as e:
        print(e)
    
    finally:
        print("\nprocess completed - Thank you for using the mini library system.")

mini_library()