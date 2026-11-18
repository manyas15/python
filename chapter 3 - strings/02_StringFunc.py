# len(): Returns the length of a string.
import string


len("hello")  # Output: 5

# - str(): Converts an object to a string.
str(123)  # Output: '123'


# - lower(): Converts all characters in a string to lowercase.
"HELLO".lower()  # Output: 'hello'


# - upper(): Converts all characters in a string to uppercase.
"hello".upper()  # Output: 'HELLO'


# - title(): Capitalizes the first letter of each word.
"hello world".title()  # Output: 'Hello World'


# - capitalize(): Capitalizes the first character of the string.
"hello world".capitalize()  # Output: 'Hello world'


# - swapcase(): Converts uppercase characters to lowercase and vice versa.
"HeLLo".swapcase()  # Output: 'hEllO'


# - strip(): Removes whitespace from both ends of a string.
"  hello  ".strip()  # Output: 'hello'


# - lstrip(): Removes whitespace from the left side.
"  hello".lstrip()  # Output: 'hello'


# - rstrip(): Removes whitespace from the right side.
"hello  ".rstrip()  # Output: 'hello'


# - find(): Returns the first index of a substring, or -1 if not found.
"hello".find("l")  # Output: 2


# - index(): Returns the first index of a substring; raises ValueError if not found.
"hello".index("e")  # Output: 1


# - count(): Counts the occurrences of a substring.
"banana".count("a")  # Output: 3


# - startswith(): Checks whether a string starts with a given prefix.
"python".startswith("py")  # Output: True


# - endswith(): Checks whether a string ends with a given suffix.
"python".endswith("on")  # Output: True


# - split(): Splits a string into a list.
"a,b,c".split(",")  # Output: ['a', 'b', 'c']


# - join(): Joins elements of an iterable into a string.
"-".join(["a", "b", "c"])  # Output: 'a-b-c'


# - replace(): Replaces occurrences of a substring.
"hello".replace("l", "x")  # Output: 'hexxo'


# - removeprefix(): Removes a prefix if present.
"unhappy".removeprefix("un")  # Output: 'happy'


# - removesuffix(): Removes a suffix if present.
"report.pdf".removesuffix(".pdf")  # Output: 'report'


# - isalpha(): Checks whether all characters are letters and the string is non-empty.
"Hello".isalpha()  # Output: True



# - isdigit(): Checks whether all characters are digits and the string is non-empty.
"123".isdigit()  # Output: True



# - isalnum(): Checks whether all characters are letters or digits and the string is non-empty.
"abc123".isalnum()  # Output: True



# - isspace(): Checks whether all characters are whitespace and the string is non-empty.
"   ".isspace()  # Output: True



# - islower(): Checks whether all cased characters are lowercase.
"hello".islower()  # Output: True



# - isupper(): Checks whether all cased characters are uppercase.
"HELLO".isupper()  # Output: True

