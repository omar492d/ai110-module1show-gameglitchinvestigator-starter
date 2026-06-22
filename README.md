# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
   Glitchy Guesser is a number-guessing game that runs on the web. There are three difficulties that differ in how many attempts are allowed. The player guesses a secret number and gets a higher/lower hint. The player gains points on correct guesses and loses points on incorrect guesses. This game was a learning experience for how to understand, develop, and debug real projects using AI.
- [x] Detail which bugs you found.
   1. Reversed hints: the game told the player to go higher when the guess was too high and go lower when the guess was too low.
   2. Unresponsive "new game" button: after a round ended, the button appeared to do nothing and the player was unable to restart.
   3. Incorrect difficulties: the Easy difficulty had lower attempts allowed than the Normal difficulty.
- [x] Explain what fixes you applied.
   1. Swapped the hint messages in the game logic.
   2. Made the "new game" button to correctly modify the state, which resolved the issue.
   3. Changed Easy mode to have 8 attempts and Normal mode to have 6 attempts.
   4. Refactored the game logic into logic_utils.py

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters 57
2. Game hints to "Go LOWER"
3. User enters 40
4. Game hints to "Go HIGHER"
5. User enters 48
6. Correct answer! Round ends.
7. User presses "new game"
8. Score updates after each guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
