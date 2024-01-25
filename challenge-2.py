def longest_palindromic_substring(string)-> None:
    """
    param: string (str) string to be validated
    return: max_length (int) length of the palindrome
    """
    string_length = len(string)
    start = 0
    max_length = 1

    for center_index in range(string_length):
        left = center_index - 1
        right = center_index

        while left >= 0 and right < string_length and string[left] == string[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        left = center_index - 1 
        right = center_index + 1

        while left >= 0 and right < string_length and string[left] == string[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    print("Longest palindrome in the string is: ", string[start:start + max_length])

    return max_length

# Input string can be changed below accordingly for testing.
# Expected input type: Python string object passed to the function : longest_palindromic_substring as params

input_string1: str = "Ilikeracecarsthatgofast"
input_string2: str = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

length = longest_palindromic_substring(input_string1)
print("Max Length: ", length)

length = longest_palindromic_substring(input_string2)
print("Max Length: ", length)
