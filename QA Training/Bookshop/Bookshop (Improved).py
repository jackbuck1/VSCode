JacksBookshop = {

     "Rick Riordan": [
         "The Lightning Thief",
         "The Sea of Monsters",
         "The Last Olympian"
     ],
     "Jonathan Haidt": [
         "The Happiness Hypothesis",
         "The Righteous Mind",
         "The Anxious Generation",
     ],
     "Colleen Hoover": [
         "It Ends With Us",
         "Verity",
         "Hopeless",
     ]
 }

print("Availible authors:")
print(", ".join(JacksBookshop.keys()))

author = input("Please enter an authors name " )

books = JacksBookshop.get(author) or ["Sorry, no books found"]
print(", ".join(books))