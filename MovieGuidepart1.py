# Lara Salinas CIS261 Lab Movie Guide Part 1

def display_menu():
    print("Menu:")  
    print("1. Display all titles")  
    print("2. Add a title") 
    print("3. Delete a title")
    print("4. Exit")
    
def display_titles(movie_list):
    print("\nMovie Titles:")
    for title in movie_list:
        print(title)
        
def add_title(movie_list):
    title = input("Enter the title of the movie to add: ")
    movie_list.append(title)
    print(f"{title} has beem added to the list. ")
    
def delete_title(movie_list):
    title = input("Enter the title of the movie to delete: ")
    if title in movie_list:
        movie_list.remove(title)
        print(f"{title} has been removed from the list. ")
    else:
        print("Title not found in the list.")
        
def main():
    movie_list = ["Movie 1", "Movie 2", "Movie 3" ]
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
    if choice == "1":
      display_titles(movie_list)
    elif choice == "2":
      add_title(movie_list)
    elif choice == "3":
      delete_title(movie_list)
    elif choice == "4":
      print("Exit program.")
      break
      print('loop ended.')
    else:
      print("Invalid comman. Please enter a number between 1 and 4.")
      

if __name__== "__main__":
    main()
