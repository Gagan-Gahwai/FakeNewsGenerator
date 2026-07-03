# import random module
import random

# creat subject

subjects = [
    "Salman khan",
    "Shahrukh khan", 
    "Samay Raina"
    "Virat Kohali",
    "Narendra Modi",
    "Nirmala Sitharaman",
    "A Group of Monkeys",
    "A mumbai Cat",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "declares war on",
    "orders",
    "celebrates EID"
]

places_or_things = [
    "at red fort",
    "in Mumbai local Train",
    "a plat of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL Match",
    "at india gate",
    "at jhumrilaiya",
    "to kapill sharma show",
    "Indias got latent"
    
]

#3 start the headline generation loop

while True:
    sub = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {sub} {action} {place}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes or no)").strip().lower()
    if user_input == "no":
        break

# Print goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day")
