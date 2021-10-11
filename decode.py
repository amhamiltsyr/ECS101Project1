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
        code = "1000"
    return code


for i in range(0, len(my_string)):
    val = findcode(my_string[i])
    bits = bits + len(val)
    my_ans = my_ans + val





