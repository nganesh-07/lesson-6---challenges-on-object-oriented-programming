class roman():
    def __init__(self):
        self.roman_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (5, "V"), (4, "IV"), (1, "I")]

    def inttoroman(self, num):
        if not 1<= num <= 3999:
            return("Input must be a value between 1 and 3999.")
        result = ""
        for value, symbol in self.roman_map:
            while num >= value:
                result += symbol
                num -= value
        return result
    

if __name__ == "__main__":
    try:
        userinput = int(input("Enter a number between 1 and 3999 here:"))
        converter = roman()
        print("Aligned roman numeral:", converter.inttoroman(userinput))
    except ValueError:
        print("Invalid input. Enter an integer between 1 and 3999.")