# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The game had many issues and some features were unresponsive. The game provides you with incorrect hints. After completing a round, the buttons stopped functioning properly.  
- List at least two concrete bugs you noticed at the start  
    1. The hints provided are backward. If the guess is higher than the secret, the hint says to go higher. If the guess is lower than the secret, the hint says to go lower. The expected behaviour is to show the opposite hint. 
    2. After completing a round, either win or lose, the "new game" stops working and the player is unable to restart the game. Pressing the button does not remove the win/lose screen that appears and the player is unable to make any more guesses.
    3. The "easy" difficulty has a lower number of attempts allowed than the "normal" difficulty setting. I expected the easy difficulty to have the most attempts allowed.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.
|-----------|-------------------|-----------------|------------------------|
|   Input   | Expected Behavior | Actual Behavior | Console Output / Error |
|-----------|-------------------|-----------------|------------------------|
|Guess of   |  "Go Higher" hint | "Go Lower" hint | None                   |
|78         |                   |                 |                        |
|-----------|-------------------|-----------------|------------------------|
|Clicked    |Win/lose overlay   |Overlay stays and| None                   |
|"new game" |disappears and a   |guessing is dis- |                        |
|           |new round starts   |abled            |                        |
|-----------|-------------------|-----------------|------------------------|
|Selected   |More attempts      |Fewer attempts   | None                   |
|"easy"     |allowed than       |than "normal"    |                        |
|difficulty |"normal"           |(6 compared to 8)|                        |
|-----------|-------------------|-----------------|------------------------|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
