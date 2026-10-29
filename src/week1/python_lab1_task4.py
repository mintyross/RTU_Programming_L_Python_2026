"""
Task 4 – Text-based Arithmetic Analyzer
---------------------------------------
Create a text-based analyzer made of small helper functions.

Rules used by all functions:
- Words are pieces of text separated by whitespace (use .split()).
- A NUMBER is a word that is a whole integer, optionally with a leading
  minus sign, e.g. "7", "42", "-3".
  Punctuation at the end of a word is ignored, so "5," "10." "8!" count
  as 5, 10 and 8. Use word.rstrip(".,!?;:") to remove it.
  Decimals ("3.5") and mixed words ("abc123") are NOT numbers.
- You do not need the `re` module; .split(), .rstrip() and .isdigit()
  are enough.

Helper functions:
- count_characters(text) -> int    : characters that are not whitespace
- count_words(text)      -> int    : number of words
- extract_numbers(text)  -> list   : list of ints, in the order they appear
- analyze_text(text)     -> dict   : combines the helpers (see below)

analyze_text() returns a dict with exactly these keys:
    "characters" : int   (from count_characters)
    "words"      : int   (from count_words)
    "numbers"    : list  (from extract_numbers)
    "sum"        : int   (sum of the numbers, 0 if there are none)
    "average"    : float (average of the numbers, 0.0 if there are none,
                          NOT rounded)

In the main block: read a line of text, call analyze_text(), and print a
summary. Round the average to 2 decimals when printing.

Example run:
    Enter text: I have 3 apples and 5 pears
    Characters (no spaces): 21
    Words: 7
    Numbers: [3, 5]
    Sum: 8
    Average: 4.00

Examples (these are also used to check your work):
>>> count_characters("a b  c")
3
>>> count_words("I have 3 apples and 5 pears")
7
>>> extract_numbers("Scores: 10, -4 and 7! but not 3.5 or abc123")
[10, -4, 7]
>>> result = analyze_text("I have 3 apples and 5 pears")
>>> result["characters"], result["words"], result["numbers"]
(21, 7, [3, 5])
>>> result["sum"], result["average"]
(8, 4.0)
>>> analyze_text("no numbers here")["average"]
0.0
"""


def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    # TODO: implement
    return len("".join(text.split()))


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    # TODO: implement
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    # TODO: implement
    numbers = []

    for word in text.split():
        # Strip trailing punctuation from the word
        cleaned_word = word.rstrip(".,!?;:")

        # Check if a number starts with '-' and the rest is digits
        if cleaned_word.startswith("-") and cleaned_word[1:].isdigit():
            numbers.append(int(cleaned_word))

        # Handle regular positive integers
        elif cleaned_word.isdigit():
            numbers.append(int(cleaned_word))

    return numbers


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    num_of_char = count_characters(text)
    num_of_words = count_words(text)
    numbers = extract_numbers(text)

    sum_of_numbers = sum(numbers)

    # Prevent ZeroDivisionError if no numbers exist
    if len(numbers) > 0:
        average = float(sum_of_numbers / len(numbers))
    else:
        average = 0.0

    # Return a dictionary
    return {
        "characters": num_of_char,
        "words": num_of_words,
        "numbers": numbers,
        "sum": sum_of_numbers,
        "average": average,
    }


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    # TODO: read input, call analyze_text(), and print results
    user_input = input("Enter text: ")
    result = analyze_text(user_input)

    # Printing with exact formatting as specified in the example run
    print(f"Characters (no spaces): {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Numbers: {result['numbers']}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']:.2f}")
