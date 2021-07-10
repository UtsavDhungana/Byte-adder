from forGate import *
    
def forMain():
    a = 'Y'
    print("\n        ...............................       ")
    print("       .             WELCOME           .     ")
    print("       .               TO              .     ")
    print("       .       BIT-ADDER PROGRAM       .     ")
    print("        ...............................      ")

    forGate()
    while(a == 'Y'):
        
        b = (input("\nDo you want to continue the program ? (Y / N) : ")).upper()
        if (b == 'N'):
            print("\n           _______________________________________________     ")
            print("             ___________________________________________     ")
            print(" ")
            print("                       Thank You for your time.               ")
            print("                          Have a nice Day!!!!                 ")
            print("                                  :D                          ")
            print("             ___________________________________________")
            print("           _______________________________________________ ")
            a = 'N'
        elif(b == 'Y'):
            print("\n        ...............................       ")
            print("       .          WELCOME BACK         .     ")
            print("       .               TO              .     ")
            print("       .       BIT-ADDER PROGRAM       .     ")
            print("        ...............................      ")
            forGate()
        else:
            print("\n      ------------ ERROR!! ------------- ")
            print("     |                                  |")
            print("     |        Enter valid Option        |")
            print("     |                                  |")
            print("      ---------------------------------- ")


forMain()


 


