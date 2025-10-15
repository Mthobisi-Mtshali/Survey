from os import name
import sqlite3
from turtle import title

# CREATING TABLE AND POPULATE
def create_table():
    try:
       conn = sqlite3.connect("ebookstore.db") # Connect to the database
       cursor = conn.cursor() 

       # Creating table called author
       cursor.execute("""
          CREATE TABLE IF NOT EXISTS author(
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           country TEXT NOT NULL
          )
        """
        )
       # Populatingthe table using list
       authors = [
               (1290,"Charles Dickens","England"),
               (8937,"J.K Rowling","England"),
               (2356,"C.S Lewis","Ireland"),
               (6380,"J.R.R Tolkien","South Africa"),
               (5620,"Lewis Carroll","England")
               ]
       cursor.executemany("INSERT INTO author VALUES(?,?,?)",authors)
       conn.commit()

       # Creating a table called book
       cursor.execute("""
        CREATE TABLE IF NOT EXISTS book(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   authorID INTEGER NOT NULL,
                   qty INTEGER NOT NULL,
                   FOREIGN KEY (authorID) REFERENCES author(id) 
                   )
         """
       )
       # Populating table called book
       books = [
             (3001,"A Tale of Two Cities",1290, 30),
             (3002,"Herry Potter and the wordrobe",8937,40),
             (3003,"The LiON, the Witch and thewordrope",2356,25),
             (3004,"The Lord of the Rings",6380,37),
             (3005,"Alice's Adventures in Wonderland",5620,12)
             ]
             
       cursor.executemany("INSERT INTO book VALUES(?,?,?,?)", books)
       conn.commit()
   
       #cursor.execute("SELECT * FROM book")
       for row in cursor.fetchall():
        print(row)
      
       

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
    finally:
       conn.close();


# update table function with try and catch error, open and closes database with SQL statements

def update_book(id,title,authorID,qty,name,country):
    try:
        conn = sqlite3.connect("ebookstore.db")
        cursor = conn.cursor()


        if title:
            cursor.execute("UPDATE book SET title = ? WHERE id = ?", (title, id))
        if authorID:
            cursor.execute("UPDATE book SET authorID = ? WHERE id = ?", (authorID,id))
        if qty:
            cursor.execute("UPDATE book SET qty = ? WHERE id =?", (qty,id))

        
        if authorID:
            if name:
                cursor.execute("UPDATE author SET name = ?", (name,authorID))
    
            if country:
                cursor.execute("UPDATE author SET country = ?", (country,authorID))
        conn.commit()
    except sqlite3.Error as e:
        print(f" Database error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
    finally:
       conn.close()
    print(f"BOOK ID {id} update successfull")


# add function with try and catch error, open and closes database with SQL statements

def add_book(id, title, authorID, qty,name,country):
    try:
        conn = sqlite3.connect("ebookstore.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO book (id, title, authorID, qty) VALUES (?,?,?,?)", (id,title,authorID,qty))
        cursor.execute("INSERT OR IGNORE INTO author (id,name, country) VALUES (?,?,?)", (authorID,name,country))
        conn.commit()
    except sqlite3.Error as e:
        print(f" Database error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
    finally:
         conn.close()
    print(f"{title} added successfull")


# delete function with try and catch error, open and closes database with SQL statements

def delete_book(id):
    try:
        conn = sqlite3.connect("ebookstore.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f" Database error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
    finally:
        conn.close()
    print(f"Book ID {id} deleted successfull")


# search function with try and catch error, open and closes database with SQL statements

def search_books(searchword):
    try:
       conn = sqlite3.connect("ebookstore.db")
       cursor = conn.cursor()

       cursor.execute(
           '''
            SELECT * FROM book WHERE title LIKE ? OR CAST (authorID AS TEXT) LIKE ?
           ''',(f"%{searchword}%", f"%{searchword}%")
           )
       result = cursor.fetchall()
    except sqlite3.Error as e:
        print(f" Database error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
    finally:
       conn.close()

    if result:
        print("\n********************************** Search results **********************************")
        for row in result:
            print(f"ID {row[0]}, title:{row[1]}, AuthorID:{row[2]}, Quantity:{row[3]}")
            
    else:
            print("No book found")


# View all function with try and catch error, open and closes database with SQL statements
def View_All():
    try:
       conn = sqlite3.connect("ebookstore.db")
       cursor = conn.cursor()
    
       #cursor.execute('''SELECT * FROM author''')
       cursor.execute("""
         SELECT b.title AS book_title , 
         a.name AS author_name, 
         a.country AS author_country
         FROM book b
         INNER JOIN author a ON b.authorID = a.id
       """)
       result = cursor.fetchall()
    except sqlite3.Error as e:
        print(f" Database error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
    finally:
       conn.close()
    print("\n*********************************** All Book ****************************************")

    if result:
       for title,name,country in result:
         #print(f"ID {row[0]}, name:{row[1]}, country:{row[2]}")
         print(f"Title: {title}")
         print(f"Author: {name}")
         print(f"Country: {country}")
         print("\n-----------------------------------   -------------------------------------------")
    else:
            print("No books found")
#def input_validation(id,authorID,qty):

# Menu Function that calleds create_table() function and displays menu selection

def menu():
    create_table()
    #input_validation(id,authorID,qty)
    while True: 
        print("\n ***************************** SHELF Tracking Menu *****************************")
        print("1. Add New Book ")
        print("2. Update Book ")
        print("3. Delete Books ")
        print("4. Search Books ")
        print("5. View All Books ")
        print("0. Exit ")
        print("\n ---------------------------------------- END -----------------------------------")
        
        choice = input("Enter you prefered action from 1 to 5 and 0 being EXIT")

        if choice == '1':
            while True:
                try:
                   id = int(input("Enter book's ID number: "))
                   if 1000 <= id <= 9999:
                       break
                   else:
                       print("Book ID must be a four digits")
                except ValueError:
                    print("Please Enter a valid numbers")

            title =input("Enter Title: ")

            while True:
                try:
                    authorID = int(input("Enter autho's ID: "))
                    if 1000 <= authorID <= 9999:
                        break
                    else:
                        print("Author ID must be a four (4) digits not less or greater")
                except ValueError:
                    print("Please enter valid ID")

            while True:
                try:
                    qty = int(input("Enter qaulity number: "))
                    if qty < 0:
                        break
                    else:
                        print("Quantity can't be negative")
                except ValueError:
                    ("Enter quantity")

            name = input("Enter author name: ")
            country = input("Enter author's country: ")
                   
            add_book(id,title,authorID,qty,name,country)
            

        elif choice == '2':
            while True:
                try:
                   id = int(input("Enter book's ID number: "))
                   if 1000 <= id <= 9999:
                       break
                   else:
                       print("Book ID must be a four digits")
                except ValueError:
                    print("Please Enter a valid numbers")

            title =input("Enter Title: ")

            
            while True:
                try:
                    authorID = int(input("Enter autho's ID: "))
                    if 1000 <= authorID <= 9999:
                        break
                    else:
                        print("Author ID must be a four (4) digits not less or greater")
                except ValueError:
                    print("Please enter valid ID") 

            while True:
                try:
                    qty = int(input("Enter qaulity number: "))
                    if qty < 0:
                        break
                    else:
                        print("Quantity can't be negative")
                except ValueError:
                    ("Enter quantity")

            name = input("Enter author name: ")
            country = input("Enter author's country: ")

            update_book(id,title,authorID,qty,name,country)
            

        elif choice == '3':
            id = int(input("Enter bokk's ID number (4 digits): "))
            delete_book(id)

        elif choice == '4':
            searchword = input("Enter book title or authorID: ")
            search_books(searchword)

        elif choice == '5':
            View_All()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid, try again")

if __name__ == "__main__":
    menu()






        



    

