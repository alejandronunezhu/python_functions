def verify_card_number(card_number: str) -> bool:
    """Return True if card number is valid according to the Luhn algorithm."""
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main() -> None:
    card_number = input("Enter credit card number (with or without spaces or dashes): ")
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if not translated_card_number.isdigit():
        print("Invalid input: card number must contain only digits.")
        return

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

if __name__ == "__main__":
    main()

#def test_verify_card_number() -> None:
#    tests = [
#        ("Valid Visa", "4111 1111 1111 1111", True),
#        ("Valid Mastercard", "5500-0000-0000-0004", True),
#        ("Invalid number", "1234 5678 9012 3456", False),
#        ("Short number", "4111", False)
#    ]
#    for name, number, expected in tests:
#        result = verify_card_number(number.replace(" ", "").replace("-", ""))
#        print(f"{name}: {'PASS' if result == expected else 'FAIL'}")
#
## Run tests:
#test_verify_card_number()
