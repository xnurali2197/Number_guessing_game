"""
Number Guessing Game
A fun interactive game where the player guesses a random number between 1-100
"""

import random


def get_valid_guess():
    """Get and validate player's guess"""
    while True:
        try:
            guess = int(input("\n🎯 Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100")
                continue
            return guess
        except ValueError:
            print("❌ Error: Please enter a valid number")


def play_game():
    """Main game logic"""
    # Game setup
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    guesses = []
    
    print("\n" + "="*50)
    print("🎮 Welcome to Number Guessing Game!")
    print("="*50)
    print(f"\n📝 Rules:")
    print(f"   • I'm thinking of a number between 1 and 100")
    print(f"   • You have up to {max_attempts} attempts")
    print(f"   • I'll give you hints: HIGHER or LOWER")
    print(f"   • Can you find the number?\n")
    
    while attempts < max_attempts:
        # Get player's guess
        guess = get_valid_guess()
        attempts += 1
        guesses.append(guess)
        
        # Check guess
        if guess == secret_number:
            return True, attempts, guesses
        elif guess < secret_number:
            remaining = max_attempts - attempts
            print(f"📈 The number is HIGHER!")
            print(f"   Attempts remaining: {remaining}/{max_attempts}")
        else:
            remaining = max_attempts - attempts
            print(f"📉 The number is LOWER!")
            print(f"   Attempts remaining: {remaining}/{max_attempts}")
        
        # Warm/Cold feedback
        if attempts > 1:
            previous_guess = guesses[-2]
            distance_to_secret = abs(guess - secret_number)
            previous_distance = abs(previous_guess - secret_number)
            
            if distance_to_secret < previous_distance:
                print("   🔥 Getting warmer!")
            elif distance_to_secret > previous_distance:
                print("   ❄️  Getting colder!")
    
    # Game over - player lost
    return False, attempts, guesses


def display_results(won, attempts, guesses, secret_number=None):
    """Display game results"""
    print("\n" + "="*50)
    
    if won:
        print(f"🎉 CONGRATULATIONS! You won!")
        print(f"✅ You found the number in {attempts} attempts!")
        
        # Difficulty rating
        if attempts <= 3:
            print("🏆 Amazing! You're a mind reader!")
        elif attempts <= 5:
            print("🥇 Excellent! Great guessing skills!")
        elif attempts <= 7:
            print("🥈 Good! Nice work!")
        else:
            print("🥉 Not bad! Better luck next time!")
    else:
        print(f"😢 Game Over! You didn't find the number.")
        print(f"❌ The number was: {secret_number}")
        print(f"   You made {attempts} attempts")
    
    print(f"\n📊 Your guesses: {', '.join(map(str, guesses))}")
    print("="*50)


def main():
    """Main game loop"""
    play_again = True
    games_played = 0
    games_won = 0
    
    while play_again:
        # Play game
        won, attempts, guesses = play_game()
        secret_number = random.randint(1, 100)  # For display purposes
        
        # Update stats
        games_played += 1
        if won:
            games_won += 1
        
        # Show results
        display_results(won, attempts, guesses, secret_number if not won else None)
        
        # Ask to play again
        while True:
            choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if choice in ['yes', 'y', 'ha', 'h']:
                break
            elif choice in ['no', 'n', 'yo\'q']:
                play_again = False
                break
            else:
                print("❌ Please enter 'yes' or 'no'")
    
    # Final stats
    print("\n" + "="*50)
    print("📈 GAME STATISTICS")
    print("="*50)
    print(f"Total games played: {games_played}")
    print(f"Games won: {games_won}")
    print(f"Games lost: {games_played - games_won}")
    
    if games_played > 0:
        win_percentage = (games_won / games_played) * 100
        print(f"Win rate: {win_percentage:.1f}%")
    
    print("\n👋 Thanks for playing Number Guessing Game!")
    print("Come back soon! 🎮")
    print("="*50)


if __name__ == "__main__":
    main()
