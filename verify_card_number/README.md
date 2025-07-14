# Credit Card Validator (Luhn Algorithm)

This Python script verifies the validity of a credit card number using the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm), a checksum formula used to validate various identification numbers, especially credit card numbers.

## Features

- Accepts card numbers with or without spaces or dashes.
- Implements the Luhn algorithm to validate card numbers.
- Provides simple pass/fail output.

## How to Use

Run the program:

```bash
python card_validator.py
Enter a credit card number when prompted, for example:

Enter credit card number (with or without spaces or dashes): 4111-1111-1111-1111
OUTPUT: VALID!

You can include a test suite by uncommenting the test_verify_card_number() function in the script.
