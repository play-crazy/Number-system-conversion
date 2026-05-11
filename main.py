

def main():
    print("NUMBER SYSTEM CONVERSION PROGRAM")


    while True:
        print("1.Decimal to binary")
        print("2.Binary to decimal")
        choice = input("Enter your choice (q to quit):  ")
        match choice:
            case "1":
                print("Binary: " + base10ToBase2(int(input("Decimal: "))))
            case "2":
                pass
            case "q":
                break
            case _:
                print("Not a valid option!")

def base10ToBase2(base10):
    base2 = ''
    while base10 > 0:
        base2 = str(base10 % 2) + base2
        base10 //= 2
    return base2

if __name__ == '__main__':
    main()
