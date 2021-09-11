# Function consuming a BigInt number (response of getAmountsOut contract function)
# formating the number as a string to add correct number of 0's between
# the decimal point and the first digit.
# returning a float representation of the number, rounded to 18 decimal places


def format_num(number: int):
    string = str(number)
    length = len(string)
    num_zeros = 18 - length
    zeros = []
    for _ in range(num_zeros):
        zeros.append("0")

    if len(zeros) <= 0:
        final_string = "0." + string
        final_num = round(float(final_string), 18)
        return final_num
    else:
        zeros_string = ""
        for zero in zeros:
            zeros_string = zeros_string + zero
        final_string = "0." + zeros_string + string
        final_num = round(float(final_string), 18)
        return final_num
