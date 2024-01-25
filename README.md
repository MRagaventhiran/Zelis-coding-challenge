# Zelis-coding-challenge

Python version: 3.10.13

## *Challenge 1: English Words to Integer transformation*

### Undertanding of the problem:

Provided with an exhaustive list of words that will be represented for the number.
Solution should be converting the input word given into integer.
The input range can be anywhere between -999,999,999 to 999,999,999
The solution should be able to handle negative numbers too.

### Approach for solution:

The getNumberFromWords function follows the following steps to convert English words to integers:

1. Split the input string into a list of words.
2. Check for the presence of the word 'negative' at first to determine the sign of the number.
3. Iterate through the list of words, accumulating the numeric value based on the predefined mapping in the word_to_int_mapping dictionary.
4. Handle special cases for words like 'hundred,' 'thousand,' and 'million' to correctly calculate the numeric value.
5. Raise a ValueError for invalid words or representations.
6. Output the final integer value, considering the sign.
7. The code also includes a loop to test the function with the provided input array.

## *Challenge 2: Find longest palindrome in the given string*

### Understanding of the problem:

Given a input string, the longest palindrome should be found.
There can be many palindromes in the string with varying length
Only the palindrome with max length is taken.

### Approach for the solution:

1. Initializes variables such as string_length, start, and max_length.
2. It iterates through each character in the input string (string) using a for loop with center_index as the potential center for palindromic substrings.
3. For each potential center, the function expands outward (both left and right) to check if the characters at those positions are equal and form a palindrome.
4. Two while loops handle the expansion:
    - The first while loop handles the case where the potential palindrome has an odd length (centered at a single character).
    - The second while loop handles the case where the potential palindrome has an even length (centered between two characters).
5. If a longer palindrome is found, the function updates start and max_length.
6. The final result is printed, indicating the longest palindromic substring in the given string.
7. The function returns the length of the longest palindromic substring (max_length).
