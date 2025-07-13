# Meal Time Checker 🕒🥗

This is a simple Python program that determines which meal time it is based on user input.

## How it works

The program asks the user to input a time in `HH:MM` 24-hour format. It then converts the 
time into a float (e.g., `7:30` becomes `7.5`) and tells the user if it’s:

- **Breakfast time** (between 7:00 and 8:00)
- **Lunch time** (between 12:00 and 13:00)
- **Dinner time** (between 18:00 and 19:00)
- **Fasting time** (any other time)

## Example
INPUT:  12:30
OUTPUT: lunch time
