class Function_Calc:

    def modular(self, value_1, value_2):  # divisible function
        if value_2 == 0:
            return False
        elif value_1 % value_2 == 0:  # if the value_1 can be divided by the value_2 with no remainder, then return True
            return True
        else:
            return False

    def triangle(self, height, base):  # area of a triangle function
        return (height * base) / 2

    def percentage(self, value_1, value_2):  # area of a triangle function
        return (value_1 / value_2) * 100

    def inches(self, value_1):
        return value_1 * 2.54  # multiplies the value by the length of an inch in centimeters
