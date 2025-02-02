def main():
    print ("This program converts US dollers to LKR sterling")
    print()

    dollars = eval (input("Enter amount in dollers: "))
    LKR = convert_to_LKR(dollars)
    print("This is",LKR,"LKR.")

convert_to_LKR = lambda dollars: dollars * 308

main()



