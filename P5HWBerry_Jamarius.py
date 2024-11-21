# Jamarius Berry
# 11/20/2024
# P5HW
# Create a text based game using fucntions


import random

import time

def create_character():
    
    print("\n--- WWE BACKSTAGE BRAWLS: CHOOSE YOUR FACE!!! ---")
    
    # Get character name
    while True:
        name = input("Enter superstars name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")
    
    # Get character rating
    while True:
        try:
            rating = int(input("Enter superstars rating (50-100): "))
            if 50 <= rating <= 100:
                break
            print("Rating must be between 50 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get character damage
    while True:
        try:
            damage = int(input("Enter superstars damage (10-50): "))
            if 10 <= damage <= 50:
                break
            print("Damage must be between 10 and 50.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get number of finishers
    while True:
        try:
            finishers = int(input("Enter number of finishers (1-5): "))
            if 1 <= finishers <= 5:
                break
            print("Finishers must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Create character dictionary
    character = {
        "name": name,
        "rating": rating,
        "damage": damage,
        "finishers": finishers
    }
    
    return character

def create_opponent():
    
    opponent_names = [
        "Pyscho Sid", "Hollywood Hulk Hogan", "Triple H", 
        "Randy Orton", "Big Show"
    ]
    
    opponent = {
        "name": random.choice(opponent_names),
        "rating": random.randint(50, 100),
        "damage": random.randint(10, 50),
        "finishers": random.randint(1, 5)
    }
    
    return opponent

def battle_simulation(player1, player2):
   
    # Create deep copies to preserve original character stats
    p1 = player1.copy()
    p2 = player2.copy()
    
    print(f"\n--- LETS BRAWL: {p1['name']} vs {p2['name']} ---")
    
    
    round_num = 1
    
    # Battle logic
    while True:
        print(f"\nRound {round_num}")
        print("FIGHT FIGHT FIGHT.....", end=" ", flush=True)

        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
            print()
        
        # Player 1 attacks
        damage1 = p1['damage']
        if p1['finishers'] > 0:
            damage1 = int(damage1 * 1.5)  
            p1['finishers'] -= 1
            print(f"{p1['name']} uses a finisher! IT'S A SLOBBER KNOCKER!")
        
        # Player 2 attacks
        damage2 = p2['damage']
        if p2['finishers'] > 0:
            damage2 = int(damage2 * 1.5)  
            p2['finishers'] -= 1
            print(f"{p2['name']} uses a finisher! HOLY CRAP!")
        
        # Reduce health based on damage
        p2['rating'] -= damage1
        p1['rating'] -= damage2
        
        # Print attack details
        print(f"{p1['name']} deals {damage1} damage. {p2['name']} health: {p2['rating']}")
        print(f"{p2['name']} deals {damage2} damage. {p1['name']} health: {p1['rating']}")
        
        # Check battle end conditions
        if p1['rating'] <= 0:
            print(f"\n{p2['name']} WINS!")
            return p2
        elif p2['rating'] <= 0:
            print(f"\n{p1['name']} WINS!")
            return p1
        
        round_num += 1

def main():
    
    while True:
        # Create player character
        player_character = create_character()
        
        # Create opponent
        opponent = create_opponent()
        
        # Display character details
        print("\n--- WWE SUPERSTARS ---")
        print("FACE:")
        for key, value in player_character.items():
            print(f"{key.capitalize()}: {value}")
        
        print("\nHEEL:")
        for key, value in opponent.items():
            print(f"{key.capitalize()}: {value}")
        
        # Battle simulation
        battle_simulation(player_character, opponent)
        
        # Ask to play again
        play_again = input("\nDo you want to brawl again? (yes/no): ").lower()
        if play_again != 'yes':
            print("See ya next time WWE Universe!")
            break

# Run the game
if __name__ == "__main__":
    main()
