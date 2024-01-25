from typing import Dict, List

# Mapping for the words from the exhaustive list 
word_to_int_mapping: Dict[str, int] = {
    'negative': -1,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000
}

def getNumberFromWords(words: str)-> int:

    """
    This function converts the English interpretation
    of words into integer representation

    param: (str) python string object 
    return: (int) converted integer 
    """

    word_stack: List[str] = words.split(' ')

    if 'negative' in words and word_stack[0] != 'negative':
        print('Invalid English representation of number')
        raise ValueError('Invalid English representation of number')
    
    negative_flag: bool = False

    final_sum: int = 0
    count_sum: int = 0
    swap_value: int = 0

    for word in word_stack:

        mapped_value: str = word_to_int_mapping.get(word)

        if mapped_value == -1:
            negative_flag=True
            continue

        if word == 'hundred':
            count_sum = count_sum * mapped_value
        elif word in ['thousand', 'million']:
            count_sum = count_sum * mapped_value
            swap_value = count_sum
            count_sum = 0
        elif mapped_value:
            count_sum+=mapped_value
        else:
            print(f'Invalid word: {word}')
            raise ValueError(f'Invalid word: {word}')

        final_sum = count_sum + swap_value
    
    if negative_flag:
        final_sum = final_sum * -1

    return final_sum

# Input array List of string: Range expectation is from -999,999,999 to 999,999,999 in english words
# Expected Input type: Python string object added to the List below

input_array: List[str] = [
                          'six', 'negative seven hundred twenty nine',
                          'one million one hundred one', 'two hundred fifty thousand six hundred fifty six',
                          'nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine',
                          'negative nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine',
                          ]

for word in input_array:
    try:
        print(getNumberFromWords(word))
    except ValueError as error_msg:
        print("Error: ", error_msg)

