
def main():
    print("NUMBER SYSTEM CONVERSION PROGRAM")

    while True:
        print("*******************")
        print("1.Decimal to binary")
        print("2.Binary to decimal")
        print("3.Decimal to Octal")
        print("4.Octal to Decimal")
        print("5.Octal to Binary")
        print("6.Binary to Octal")
        print("*******************")
        choice = input("Enter your choice (q to quit):  ")
        match choice:
            case "1":
                print("Binary: " + B10toB2(int(input("Decimal: "))))
            case "2":
                print("Decimal: " + str(B2toB10(input("Binary: "))))
            case "3":
                print("Octal: " + B10toB8(int(input("Decimal: "))))
            case "4":
                print("Decimal: " + str(B8toB10(input("Octal: "))))
            case "5":

                print("Binary: " + B8toB2(input("Octal: ")))
            case "6":
                print("Octal: " + str(B2toB8(input("Binary: "))))
            case "q":
                break
            case _:
                print("Not a valid option!")

def B10toB2(B10):
    B2 = ''
    while B10 > 0:
        B2 = str(B10 % 2) + B2
        B10 //= 2
    return B2

def B2toB10(B2):
    B10 = 0
    pow = 0
    for bit in reversed(B2):
        B10 += (2 ** pow) * int(bit)
        pow += 1
    return B10

def B10toB8(B10):
    B8 = ''
    while B10 > 0:
        B8 = str(B10 % 8) + B8
        B10 //= 8
    return B8

def B8toB10(B8):
    B10 = 0
    pow = 0
    for bit in reversed(B8):
        B10 += (8 ** pow) * int(bit)
        pow += 1
    return B10

def B8toB2(B8):
    B2 = ""
    relation = {0:"000", 1:"001", 2:"010", 3:"011", 4:"100", 5:"101", 6:"110", 7:"111" }
    for bit in B8:
        B2 += relation.get(int(bit))
    return B2

def B2toB8(B8):
    B10 = 0
    pow = 0
    for bit in reversed(B8):
        B10 += (8 ** pow) * int(bit)
        pow += 1
    return B10


if __name__ == '__main__':
    main()
