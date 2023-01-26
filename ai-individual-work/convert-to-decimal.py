"""
name : Taye Birhanu
id : DBUR/0963/12
"""


def roman_to_decimal(roman_numeral):
    decimal_value = 0
    roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0

    try:

        for i in roman_numeral[::-1]:
            if roman_to_decimal[i] < prev_value:
                decimal_value -= roman_to_decimal[i]
            else:
                decimal_value += roman_to_decimal[i]
            prev_value = roman_to_decimal[i]
        return decimal_value

    except:
        return "Invalid Input -> ",roman_numeral


while True:

    roman_number = input("Enter Roman number: ")

    print("The Roman number is: ","[",roman_to_decimal(roman_number.upper()),"]")

    choice = input("Convert again?, \'Y\' for yes/anykey for no: ")

    if choice.lower() != "y":
        break

