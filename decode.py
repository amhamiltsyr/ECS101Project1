# test code
# takes an input string
# returns D.B and prints
# D = number of bits needed
# B = binary representation
my_file = open("decode_input.txt")
my_string = my_file.read()
my_ans = ""
bits = 0


def findcode(my_char):
    if my_char == "a":
        code = "00000"
    elif my_char == "e":
        code = "00001"
    elif my_char == "i":
        code = "00010"
    elif my_char == "o":
        code = "00011"
    elif my_char == "u":
        code = "00100"
    elif my_char == ".":
        code = "00101"
    elif my_char == ",":
        code = "00110"
    elif my_char == "A":
        code = "00111"
    elif my_char == "E":
        code = "01000"
    elif my_char == "I":
        code = "01001"
    elif my_char == "O":
        code = "01010"
    elif my_char == " ":
        code = "01011"
    elif my_char == "t":
        code = "01100"
    elif my_char == "s":
        code = "01101"
    elif my_char == "r":
        code = "01110"
    elif my_char == "T":
        code = "01111"
    elif my_char == "-":
        code = "1100110"
    elif my_char == "!":
        code = "1100111"
    elif my_char == "'":
        code = "1101000"
    elif my_char == "”":
        code = "1101001"
    elif my_char == "\n":
        code = "1101010"
    elif my_char == "U":
        code = "1101011"

    return code


for i in range(0, len(my_string)):
    val = findcode(my_string[i])
    bits = bits + len(val)
    my_ans = my_ans + val





