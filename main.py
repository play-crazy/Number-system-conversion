
def main():
    print("NUMBER SYSTEM CONVERSION PROGRAM")

    while True:
        print("1.Decimal to binary")
        print("2.Binary to decimal")
        choice = input("Enter your choice (q to quit):  ")
        match choice:
            case "1":
                print("Binary: " + B10toB2(int(input("Decimal: "))))
            case "2":
                print("Decimal: " + str(B2toB10(input("Binary: "))))
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


if __name__ == '__main__':
    main()
