# Jessica Barry
# EC500 HW1: Quality
# Arabic Numerials -> Roman Numerials
# Reference: https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/

def getRoman(arabic):
    ara = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]

    i = (len(ara)) - 1
    roman = ""

    while arabic:
        div = arabic // ara[i]
        arabic %= ara[i]

        while div:
            roman = rom[i] + roman
            div -= 1
        i -= 1

    return roman
