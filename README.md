# CLI Habit Tracker

> *"You don't rise to the level of your goals, you fall to the level of your systems."* — *Atomic Habits*

A simple command-line Habit Tracker built using Python and SQLite to help users build better systems and track their daily habits.

## Features

* Add new habits
* Mark habits as Done or Missed for the day
* Track current streaks
* View best streaks achieved
* Calculate consistency percentages based on habit logs
* View statistics for individual habits or all habits at once
* Reset all stored data when needed

## Tech Stack

* Python
* SQLite

## Project Structure

```text
habit-tracker/
│
├── main.py      # Handles user interaction and menu operations
├── db.py        # Handles database creation and queries
├── streak.py   # Calculates streaks and consistency percentages
└── habits.db   # SQLite database file (created automatically)
```

## How It Works

1. Add a habit.
2. Mark it as Done or Missed every day.
3. The application stores daily logs using SQLite.
4. Streaks and consistency are calculated from the stored logs whenever requested.

## What I Learned

This project helped me strengthen my understanding of:

* Python and SQLite integration
* Database operations using SQL
* Working with dates and streak calculations
* Writing modular and maintainable code
* Debugging and problem-solving while building real projects

## Future Improvements

* Weekly and monthly statistics
* HTML-based reports for visualizing progress
* Graph-style streak visualizations
* A GUI or web-based version of the Habit Tracker

---

This project was built as a way to apply concepts I had previously learned and gain hands-on experience by building something from scratch.
