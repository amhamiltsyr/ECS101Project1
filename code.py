# test code
# takes an input string
# returns D.B and prints
# D = number of bits needed
# B = binary representation
my_file = open("code_input.txt")
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
    elif my_char == "b":
        code = "1000000"
    elif my_char == "c":
        code = "1000001"
    elif my_char == "d":
        code = "1000010"
    elif my_char == "f":
        code = "1000011"
    elif my_char == "g":
        code = "1000100"
    elif my_char == "h":
        code = "1000101"
    elif my_char == "j":
        code = "1000110"
    elif my_char == "k":
        code = "1000111"
    elif my_char == "l":
        code = "1001000"
    elif my_char == "m":
        code = "1001001"
    elif my_char == "n":
        code = "1001010"
    elif my_char == "p":
        code = "1001011"
    elif my_char == "q":
        code = "1001100"
    elif my_char == "v":
        code = "1001101"
    elif my_char == "w":
        code = "1001110"
    elif my_char == "x":
        code = "1001111"
    elif my_char == "y":
        code = "1010000"
    elif my_char == "z":
        code = "1010001"
    elif my_char == "B":
        code = "1010010"
    elif my_char == "C":
        code = "1010011"
    elif my_char == "D":
        code = "1010100"
    elif my_char == "F":
        code = "1010100"
    elif my_char == "G":
        code = "1010110"
    elif my_char == "J":
        code = "1011000"
    elif my_char == "K":
        code = "1011001"
    elif my_char == "L":
        code = "1011010"
    elif my_char == "N":
        code = "1011100"
    elif my_char == "Q":
        code = "1011110"
    elif my_char == "R":
        code = "1011111"
    elif my_char == "S":
        code = "1100000"
    elif my_char == "V":
        code = "1100001"
    elif my_char == "W":
        code = "1100010"
    elif my_char == "X":
        code = "1100011"
    elif my_char == "Y":
        code = "1100100"
    elif my_char == "Z":
        code = "1100101"
    elif my_char == "qu":
        code = "1101100"
    elif my_char == "and":
        code = "1101101"
    elif my_char == "the":
        code = "1101110"
    elif my_char == "sh":
        code = "1101111"
    elif my_char == "th":
        code = "1110000"
    elif my_char == "an":
        code = "1110001"
    elif my_char == "he":
        code = "1110001"
    elif my_char == "is":
        code = "1110011"
    elif my_char == "er":
        code = "1110100"
    elif my_char == "es":
        code = "1110101"
    elif my_char == "to":
        code = "1110110"
    elif my_char == "in":
        code = "1110111"
    elif my_char == "st":
        code = "1111000"
    elif my_char == "at":
        code = "1111001"
    elif my_char == "ng":
        code = "1111010"
    elif my_char == "an":
        code = "1111011"
    elif my_char == "or":
        code = "1111100"
    elif my_char == "of":
        code = "1111101"
    elif my_char == ", ":
        code = "1111110"
    elif my_char == ". ":
        code = "1111111"
    return code


for i in range(0, len(my_string)):
    val = findcode(my_string[i])
    bits = bits + len(val)
    my_ans = my_ans + val
print(str(bits) +"." + my_ans)





