# 🎯 Perfect Guess Game

A simple number-guessing game built in Python — just a little project made for fun while learning Python.

## How it works

- The computer randomly picks a secret number between **1 and 45**
- You keep guessing until you get it right
- After each guess, you'll get a hint:
  - "Guess for higher number please!" → your guess was too low
  - "Guess for lower number please!" → your guess was too high
- Once you guess correctly, it tells you the number and how many total guesses it took you

## Run it

```bash
python game.py
```

You'll be prompted to enter a guess each round until you find the right number.

## Tech

- Pure Python, no external dependencies — just the built-in `random` module.

## Why I made this

A small beginner-friendly project to practice loops, conditionals, and user input handling in Python.
