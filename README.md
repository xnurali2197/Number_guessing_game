# 🎮 Number Guessing Game

A fun and interactive command-line game where players guess a randomly selected number between 1 and 100. Features hints, attempt tracking, and game statistics.

## Features ✨

- **Random Number Selection**: Number between 1-100 generated each game
- **Smart Hints**: "HIGHER" or "LOWER" hints after each guess
- **Warm/Cold Feedback**: Additional feedback showing if you're getting closer
- **Attempt Tracking**: Keep track of how many attempts you've made
- **Game Statistics**: Track wins, losses, and win rate across multiple games
- **Input Validation**: Robust error handling for invalid inputs
- **User-Friendly**: Clear prompts and engaging emoji feedback
- **Multiple Rounds**: Play as many games as you want in one session

## Requirements 📋

- Python 3.6+
- No external dependencies

## Installation & Usage 🚀

### Run the game:
```bash
python game.py
```

### How to Play:

1. Run the script
2. The game thinks of a number between 1-100
3. Enter your guess when prompted
4. Receive hints: "HIGHER" or "LOWER"
5. Continue guessing until you find the number (max 10 attempts)
6. View your statistics and choose to play again

### Example Gameplay:

```
==================================================
🎮 Welcome to Number Guessing Game!
==================================================

📝 Rules:
   • I'm thinking of a number between 1 and 100
   • You have up to 10 attempts
   • I'll give you hints: HIGHER or LOWER
   • Can you find the number?

🎯 Enter your guess (1-100): 50
📉 The number is LOWER!
   Attempts remaining: 9/10

🎯 Enter your guess (1-100): 25
📈 The number is HIGHER!
   Attempts remaining: 8/10
   🔥 Getting warmer!

🎯 Enter your guess (1-100): 35
🎉 CONGRATULATIONS! You won!
✅ You found the number in 3 attempts!
🏆 Amazing! You're a mind reader!
```

## File Structure 📁

```
05-number-guessing-game/
├── game.py          # Main game application
└── README.md       # This file
```

## Functions 🔧

- `get_valid_guess()` - Get and validate player input
- `play_game()` - Main game logic and loop
- `display_results(won, attempts, guesses, secret_number)` - Show game results
- `main()` - Overall game management and statistics

## Game Rules 📋

1. **Objective**: Find the secret number between 1-100
2. **Attempts**: You have a maximum of 10 attempts
3. **Hints**: After each guess, you receive a hint:
   - "HIGHER" if your guess is too low
   - "LOWER" if your guess is too high
4. **Feedback**: 
   - 🔥 "Getting warmer!" if you're closer than before
   - ❄️ "Getting colder!" if you're further than before
5. **Win**: Correctly guess the number before attempts run out
6. **Lose**: Use all 10 attempts without guessing correctly

## Difficulty Ratings 🏆

Based on number of attempts:
- **1-3 attempts**: 🏆 "Amazing! You're a mind reader!"
- **4-5 attempts**: 🥇 "Excellent! Great guessing skills!"
- **6-7 attempts**: 🥈 "Good! Nice work!"
- **8+ attempts**: 🥉 "Not bad! Better luck next time!"

## Game Statistics 📊

After playing, you'll see:
- Total games played
- Games won
- Games lost
- Overall win percentage

### Example Stats:
```
📈 GAME STATISTICS
==================================================
Total games played: 5
Games won: 4
Games lost: 1
Win rate: 80.0%
```

## Input Validation ⚠️

The game handles:
- ✅ Non-numeric inputs (prompts to try again)
- ✅ Numbers outside 1-100 range
- ✅ Negative numbers
- ✅ Decimal inputs

## Strategy Tips 💡

### Best Strategy - Binary Search:
1. Start with 50 (middle of range)
2. Always pick the middle of the remaining range
3. This guarantees finding any number in 7 attempts

### Mathematical Probability:
- Probability of winning: 100% (if you use binary search)
- Expected attempts: ~6-7 with optimal strategy
- Worst case: 10 attempts (or less with smart guessing)

## Example Strategies 🎯

### Conservative (Guaranteed Win):
```
Guess 50 → Get hint → Guess middle of remaining range
Result: ~6-7 attempts average
```

### Fast & Lucky:
```
Guess random numbers and hope
Result: Highly variable, risky
```

### Systematic:
```
Start at 25, 75, or follow a pattern
Result: ~8-9 attempts average
```

## Code Features 🔧

- **Modular Design**: Separate functions for game logic
- **Input Validation**: Comprehensive error checking
- **Hint System**: Progressive hints keep game engaging
- **Statistics Tracking**: Maintains game history
- **User Feedback**: Emoji and colored output for clarity

## Customization Ideas 💡

- Change difficulty level (more/fewer attempts)
- Change number range (1-1000 instead of 1-100)
- Add difficulty levels with different ranges
- Include leaderboard tracking
- Add time limit per guess
- Add hint cost system

## Future Enhancements 🔮

- Multiplayer support
- Difficulty settings
- Leaderboard with file storage
- Time-based challenges
- 2-player mode (one thinks, one guesses)
- Network multiplayer
- Mobile app version

## Common Questions ❓

**Q: What's the maximum number of attempts?**
A: 10 attempts. You can find any number optimally in 7 with binary search.

**Q: Can I guess the same number twice?**
A: Yes, but it's not recommended!

**Q: What happens if I exceed attempts?**
A: Game ends and shows the secret number.

**Q: Is the number truly random?**
A: Yes, uses Python's `random.randint()` function.

## Performance Notes 🚀

- Instant response to guesses
- No lag or delays
- Lightweight - no external dependencies
- Works on any computer with Python

## Error Handling 🐛

All potential errors are handled:
- ✅ Invalid numeric input
- ✅ Out of range numbers
- ✅ Non-integer values
- ✅ Unexpected input during menu choices

## Author 👨‍💻

Created as part of 1-week GitHub pushing marathon

## License 📜

MIT License - Free to use and modify

## Play Now! 🎮

```bash
python game.py
```

Have fun and good luck! 🍀
