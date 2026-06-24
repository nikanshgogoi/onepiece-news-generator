import random

subjects = ["Luffy","Zoro","Sanji","Robin","Nami","Usopp","Franky","Brook","Jinbe"]

actions = [
    "stole 500 plates of biryani",
    "challenged a goat to a boxing match",
    "accidentally became a king",
    "ate 47 bananas in one sitting",
    "started a dance battle",
    "declared war on mosquitoes",
    "opened a school for cats",
    "got lost while using Google Maps",
    "tried to teach fish how to fly",
    "won a staring contest against a statue"
]

places = [
    "at Kaziranga University",
    "inside a hostel bathroom",
    "near the college canteen",
    "at a tea stall",
    "in the middle of a football field",
    "on top of a water tank",
    "at the railway station",
    "during an online class",
    "inside a shopping mall",
    "at a wedding ceremony"
]

print("One Piece Funny News Generator 🥸")
print(subjects)

input_subject = input("Enter the name of the character: ").title()

if input_subject in subjects:

    while True:
        print("\nBREAKING NEWS!! 😱")
        print(f"{input_subject} {random.choice(actions)} {random.choice(places)} 😂")

        redo = input("\nRegenerate? (y/n): ").strip().lower()

        if redo == "n":
            break

else:
    print("You entered wrong input!! 🥲")

print("\nGoodbye.. Yohohohoho 💀!")