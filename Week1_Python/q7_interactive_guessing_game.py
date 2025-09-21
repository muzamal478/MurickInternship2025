# Interactive Guessing Game
# Number guessing game with hints, scoring, and replay
import random

def guessing_game():
    try:
        # Get range and difficulty
        low, high = map(int, input("Enter range (low high): ").split())
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        max_attempts = {'easy': 15, 'medium': 10, 'hard': 5}[difficulty]
        
        num = random.randint(low, high)
        attempts = 0
        score = 100
        
        while attempts < max_attempts:
            guess = int(input("Guess: "))
            attempts += 1
            diff = abs(guess - num)
            
            if diff == 0:
                print(f"Correct! Attempts: {attempts}, Score: {score}")
                break
            elif diff < 5:
                print("Very close!")
            elif diff < 10:
                print("Close!")
            else:
                print("Much too high!" if guess > num else "Much too low!")
            score -= 10
        
        if attempts >= max_attempts:
            print(f"Game over! Number was {num}")
        
        # Replay option
        if input("Play again? (y/n): ").lower() == 'y':
            guessing_game()
    except (ValueError, KeyError) as e:
        print(f"Error: {e}. Please try again.")
        guessing_game()

# Run the game
if __name__ == "__main__":
    guessing_game()