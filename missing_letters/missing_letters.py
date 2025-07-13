# The main function along with the test function and test cases
# are all embedded here.
def missing_letters(text: str) -> str:
    """Return all English alphabet letters that aren't in text.

    Preconditions: all letters in text are lowercase
    Postconditions: the output are the letters from a to z that
    don't occur in text, in alphabetical order
    """
    alphabet = "abcdefghijklmnopqrstyuvwxyz"
    missing = ""
    for char in alphabet:
        if char not in text:
            missing += char
    return missing

def test(function, test_cases):
    for case in test_cases:
        name, text, expected = case
        result = function(text)
        if result == expected:
            print(f"{name}: PASS")
        else:
            print(f"{name}: FAIL — got '{result}' but expected '{expected}'")

PANGRAM = 'the quick brown fox jumps over the lazy dog.'

missing_letters_tests = [
    # case,         text,                           missing
    ['pangram',     PANGRAM,                        ''],
    ['no vowels',   'bcd fgh jklmn pqrst vwxyz',    'aeiou'],
    ['no cdefg',    'abhijklmnopqrstyuvwxyz',       'cdefg'],
    ['no kmswz',    'abcdefghijlnopqrtyuvxy',       'kmswz']
]

test(missing_letters, missing_letters_tests)
