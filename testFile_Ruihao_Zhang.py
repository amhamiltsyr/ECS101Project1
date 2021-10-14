"""

list = ['00000','00001','00010','00011','00100',
        '00101','00110','00111','01000','01001','01010','01011','01100','01101','01110', '01111']
list2 = ['a','e','i','o','u','.',',','A','E','I','O','<space>','t','s','r','T']

list3 = ['1000000','1000001','1000010','1000011','1000100','1000101','1000110','1000111',
'1001000','1001001','1001010','1001011','1001100','1001101','1001110',
'1001111','1010000','1010001','1010010','1010011','1010100','1010101',
'1010110','1010111','1011000','1011001','1011010','1011011','1011100',
'1011101','1011110','1011111','1100000','1100001','1100010','1100011',
'1100100','1100101','1100110','1100111','1101000','1101001','1101010',
'1101011','1101100','1101101','1101110','1101111','1110000','1110001',
'1110010','1110011','1110100','1110101','1110110','1110111','1111000',
'1111001','1111010','1111011','1111100','1111101','1111110','1111111']

list4 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','v','w','x','y','x'
,'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','V','W','X','Y','Z',
'-','!',"'", '"' ,'\n','U','qu','and','the','sh','th','an' ,'he','is','er','es',
'to','in','st','at','ng','an','or','of', ', ' , '. ']

"""
# Please ignore above.


"""
Project 1 ---- Decode
Name: Ruihao Zhang
Group 7

input --- binary file ---- binary strings
output --- output file ---- Strings

"""


def decoding(str, dic):
    return dic[str]

if __name__ == '__main__':
    # type the input binary file(if in the same directory,just xx.txt, if not, type the whole path.
    fileInput = input("please enter the path(or name,including format) of the input file: ")
    # output file, way is same as above
    fileOutput = input("Enter the path of output file: ")
    f = open(fileInput, "r")
    f2 = open(fileOutput,"w")
    inputString = f.readline()                  # read from the text file





    # list for short(binary)
    list = ['00000', '00001', '00010', '00011', '00100',
            '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111']

    #list for short(letter)
    list2 = ['a', 'e', 'i', 'o', 'u', '.', ',', 'A', 'E', 'I', 'O', ' ', 't', 's', 'r', 'T']

    # list for long(binary)
    list3 = ['1000000', '1000001', '1000010', '1000011', '1000100', '1000101', '1000110', '1000111',
             '1001000', '1001001', '1001010', '1001011', '1001100', '1001101', '1001110',
             '1001111', '1010000', '1010001', '1010010', '1010011', '1010100', '1010101',
             '1010110', '1010111', '1011000', '1011001', '1011010', '1011011', '1011100',
             '1011101', '1011110', '1011111', '1100000', '1100001', '1100010', '1100011',
             '1100100', '1100101', '1100110', '1100111', '1101000', '1101001', '1101010',
             '1101011', '1101100', '1101101', '1101110', '1101111', '1110000', '1110001',
             '1110010', '1110011', '1110100', '1110101', '1110110', '1110111', '1111000',
             '1111001', '1111010', '1111011', '1111100', '1111101', '1111110', '1111111']

    # list for long(letter)
    list4 = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'v', 'w', 'x', 'y', 'x'
        , 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'V', 'W', 'X', 'Y', 'Z',
             '-', '!', "'", '"', '\n', 'U', 'qu', 'and', 'the', 'sh', 'th', 'an', 'he', 'is', 'er', 'es',
             'to', 'in', 'st', 'at', 'ng', 'an', 'or', 'of', ', ', '. ']
    # declare a dictionary
    dic = {}

    # Please ignore this ^_^
    """
    print(dic)
    print(list.__len__())
    print(len(list2))
    print(len(list3))
    print(len(list4))
    """


    # to create dictionary
    count = 0
    while(count < len(list2)):
        dic[list[count]] = list2[count]
        count += 1

    count2 = 0
    while(count2 < len(list4)):
        dic[list3[count2]] = list4[count2]
        count2 += 1



    list_1 = inputString.split('.')     # split the number of letter and the binary string
    list_2 = list_1[1]          # the binary string


    # since the first number of binary determines the short or long, thus...
    num = int(list_1[0])        # First get the total number of binary numbers
    i = 0
    str2 = ""                   # prepare a string  to store the binary string each time
    str3 = ""                   # string for output
    while (i < num):            # use the remaining number of binary as the condition

        if (list_2[i] == '0'):           # the condition for short
            str2 = list_2[i: (i + 5)]
            i += 5
            str3 += decoding(str2,dic)
        elif (list_2[i] == '1'):         # condition for long
            str2 = list_2[i: i + 7]
            i += 7
            str3 += decoding(str2,dic)
        else:
            pass

    f2.write(str3)              # write to output

    f.close()
    f2.close()



    # Please ignore things below.
"""    
    list = str.split(".")
    list2 = list[1]
    print(list)
    print(int(list[0]))
    print(list2)
    print(list2[0] == '0')
    print('2', end= '')
    print('3')
"""

"""
    num = int(list[0])
    i = 0
    str2 = ""
    while(i < num):

        if(list2[i] == '0'):
            str2 = list2[i : (i + 5)]
            i += 5
            print(str2, end= '')
            decoding(str2)
        elif(list2[i] == '1'):
            str2 = list2[i : i + 7]
            i += 7
            print(str2, end= '')
        else:
"""