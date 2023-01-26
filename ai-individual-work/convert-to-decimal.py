"""
name : Taye Birhanu
id : DBUR/0963/12

AI individual Assignment
"""

def roman_to_decimal(roman_numeral):
    decimal_value = 0
    roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    char_freq = []
    K = 4
    current_char, count = None, 0

    try:

        for i in roman_numeral[::-1]:
            if i == current_char:
                count += 1
            else:
                current_char,count = i,1

            if count == K:
                char_freq.append(K * i)
                return print("Invalid Roman Number; No 4 Consecutive Roman Number ->", char_freq[0])

            if roman_to_decimal[i] < prev_value:
                decimal_value -= roman_to_decimal[i]
            else:
                decimal_value += roman_to_decimal[i]
            prev_value = roman_to_decimal[i]

    except:
        return print("Invalid input ->",roman_numeral)

    return print("The Roman Number is: ","[",decimal_value,"]")



while True:

    roman_number = input("Enter Roman number: ")

    roman_to_decimal(roman_number.upper())

    choice = input("Convert again?, \'Y\' for yes/anykey for no: ")

    if choice.lower() != "y":
        break
