# Dictionary containing 3 authors, with multiple books for each
# # Input for author names
# Return as a String, NOT a list!
# Includes error handling for mispelling (.get)

JacksBookshop = {
  "author1": {
  "name": "Rick Riordan",
  "book1": "The Lightning Thief", 
  "book2": "The Sea of Monsters", 
  "book3": "The Last Olympian",
},
  "author2": {
  "name": "Jonathan Haidt",
  "book1": "The Happiness Hypothesis", 
  "book2": "The Righteous Mind",
  "book3": "The Anxious Generation",  
},
  "author3": {
  "name": "Colleen Hoover", 
  "book1": "It Ends With Us",
  "book2": "Verity",
  "book3": "Hopeless",    
}
}

author_name = input("Enter the author's name: ")

found = False
for author in JacksBookshop.values():
    if author["name"].lower() == author_name.lower():
        found = True
        print(f"Books by {author_name}:")
        for key, value in author.items():
            if key.startswith("book"):
                print(value)
        break

if not found:
 print(f"No books found for author named {author_name}.")