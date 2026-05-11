def main():
    print("NUMBER SYSTEM CONVERSION PROGRAM")
    B8relay = {0: "000", 1: "001", 2: "010", 3: "011", 4: "100", 5: "101", 6: "110", 7: "111"}
    B16relay = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
                "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    while True:
        print("***********************")
        print("1.Base: 2  -> Base: 8")
        print("2.Base: 2  -> Base: 10")
        print("3.Base: 2  -> Base: 16")
        print("4.Base: 8  -> Base: 2")
        print("5.Base: 8  -> Base: 10")
        print("6.Base: 10 -> Base: 2")
        print("7.Base: 10 -> Base: 8")
        print("8.Base: 16 -> Base: 2")
        print("***********************")
        choice = input("Enter your choice (q to quit):  ")
        match choice:
            case "6":
                print("Binary: " + b10to8or2(int(input("Decimal: ")), 2))
            case "2":
                print("Decimal: " + str(b2or8to10(input("Binary: "), 2)))
            case "7":
                print("Octal: " + b10to8or2(int(input("Decimal: ")), 8))
            case "5":
                print("Decimal: " + str(b2or8to10(input("Octal: "), 8)))
            case "4":
                print("Binary: " + b8or16to2(input("Octal: "), B8relay, 8))
            case "1":
                print("Octal: " + str(b2to8or16(input("Binary: "), B8relay, 3)))
            case "3":
                print("Hexa-decimal: " + str(b2to8or16(input("Binary: "), B16relay, 4)))
            case "8":
                print("Binary: " + b8or16to2(input("Hexa-decimal: "), B16relay, 16))
            case "q":
                break
            case _:
                print("Not a valid option!")
def b10to8or2(B10, n):
    B2 = ''
    while B10 > 0:
        B2 = str(B10 % n) + B2
        B10 //= n
    return B2
def b2or8to10(B2, n):
    B10 = 0
    pow = 0
    for bit in reversed(B2):
        B10 += (n ** pow) * int(bit)
        pow += 1
    return B10
def b8or16to2(B8, relation, n):
    B2 = ""
    if n == 8:
        for bit in B8:
            B2 += relation.get(int(bit))
    elif n == 16:
        for bit in B8:
            B2 += relation.get(bit)
    return B2
def b2to8or16(B2, relation, n):
    B8 = ""
    Remainder = 0
    if not (n - len(B2) % n) == n:
        Remainder = (n - len(B2) % n)
    for i in range(0,Remainder):
        B2 = "0" + B2
    for i in reversed(range(len(B2), 0, -n)):
        for key, value in relation.items():
            if value == B2[max(0, i - n):i]:
                B8 += str(key)
    return B8
if __name__ == '__main__':
    main()