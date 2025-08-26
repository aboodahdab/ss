# 📝 Advanced Assessment: Mini Personal AI Assistant

## Objective
Build a Python program that acts like a simple AI assistant. It should:

- Take text input from the user.
- Respond to commands intelligently.
- Save and load user preferences (like name, favorite color, or favorite game).
- Keep a simple history of conversations.

---

## Core Requirements

### 1. Command Handling
The assistant should understand commands like:

- `my name is <name>` → store the name
- `what is my name?` → respond with the stored name
- `add <item> to shopping list` → update a list
- `show shopping list` → display the list
- `add score <number> for <game>` → update a scoreboard
- `show scores` → display scoreboard

### 2. Data Management
- Use **dictionaries and lists** to store user data and scores.
- Save everything to a **JSON file** so it persists between runs.
- Load the data at startup.

### 3. Conversation History
- Store the last 10 interactions in a list.
- Save history to a file so it can be reviewed later.

### 4. Functions & Modules
Organize code with functions for each feature:

- `handle_name()`
- `handle_shopping()`
- `handle_scores()`
- `save_data()` and `load_data()`

Optional: split into multiple files (modules) for better structure.

### 5. Extra Challenges (Optional for Bonus)
- Add **simple AI responses**:
  - If user says “hello”, respond “Hi! How are you?”
  - If user asks “what can you do?”, list available commands.
- Use **random choices** for varied responses.
- Make the assistant **case-insensitive**.
- Add **basic math ability** (like `what is 5 + 7`).

