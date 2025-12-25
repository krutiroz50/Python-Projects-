import random 

easy_words = ["apple","train","tiger","money","india",
              "house","green","table","chair","phone"
            ,"water","plant","cloud","smile","light"
            ,"bread","music","dance","river","beach"]
medium_words=["python","bottle","monkey","planet","laptop",
              "guitar","window","forest","camera","bridge"
            ,"school","friend","family","travel","garden"
            ,"butter","silver","orange","circle","pencil"]
hard_words=["elephant","diamond","umberella","computer","mountain",
            "airplane","building","notebook","chocolate","football"
            ,"hospital","painting","sandwich","telephone","backpack"
            ,"dinosaur","fireworks","jewellery","microscope","telescope"
            ]

print("Welcome to the Password Guessing Game!")
print("Choose a difficulty level: easy, medium or hard ")

level=input("Enter your choice: ").lower()
if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level.")
    secret =random.choice(easy_words)

attempts=0
print("\nGuess the secret password")

while True:
    guess=input("Enter your guess: ").lower()
    attempts += 1

    if guess==secret:
        print(f"Congratulations! You've guessed the password '{secret}' in {attempts} attempts.")
        break
    
    hint= ""

    for i in range(len(secret)):
      if i < len(guess) and guess[i] == secret[i]:
        hint += guess[i]
      else:
        hint += "_"

    print("Hint: ", hint)
print("Game over.")


