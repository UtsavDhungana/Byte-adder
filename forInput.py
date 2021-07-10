from Conversion import *

#Method to typecast variable to int
def intValidation(num):
    if(len(num) == 0):
        print("\n      ------------ ERROR!! ------------- ")
        print("     |                                  |")
        print("     |    You cannot leave it empty.    |")
        print("     |                                  |")
        print("      ---------------------------------- ")
        return False
    else:
        flag = False
        while(not flag):
            try:
                num = int(num)
                flag = True
            except ValueError:
                print("\n -----------------------ERROR!!!------------------------ ")
                print("|                                                       |")
                print("|   You cannot enter special character or alphabets.    |")
                print("|                                                       |")
                print(" ------------------------------------------------------- ")
                return False

    return True


def validation1(num):
    if(len(num) == 0):
        print("\n      ------------ ERROR!! ------------ ")
        print("     |                                 |") 
        print("     |    You cannot leave it empty.   |")
        print("     |                                 |")
        print("      --------------------------------- ")
        return False
    try:
        if(int(num) < 0 or int(num) > 255):
            print("\n ------------------ERROR!!!----------------------- ")
            print("|                                                 |")
            print("|   You can enter number only from 0 to 255.      |")
            print("|                                                 |")
            print(" ------------------------------------------------- ")
            return False
    except ValueError:
        print("\n -----------------------ERROR!!!------------------------ ")
        print("|                                                       |")
        print("|   You cannot enter special character or alphabets.    |")
        print("|                                                       |")
        print(" ------------------------------------------------------- ")
        return False

    return True


def validation2(num):
    if(len(num) == 0):
        print("\n      ------------ ERROR!! ----------- ")
        print("     |                                |") 
        print("     |   You cannot leave it empty.   |")
        print("     |                                |")
        print("      -------------------------------- ")
        return False
    
    for i in range(len(num), 8):
        num = str(0) + num 

    flag = False
    if(len(num) != 8):
        print("\n -----------------------ERROR!!!------------------------- ")
        print("|                                                        |")
        print("|    You cannot enter Binary number greater than 8-bit.  |")
        print("|                                                        |")
        print(" -------------------------------------------------------- ")
        return False
    else:
        for i in num:
            try:
                if(int(i) < 0 or int(i) > 1): 
                    flag = False
                    print("\n -----------------------ERROR!!!----------------------------- ")
                    print("|                                                            |")
                    print("|   Please make sure your number contains digits 0-1 only.   |")
                    print("|                                                            |")
                    print(" ------------------------------------------------------------ ")
                    
                    break
                else:
                    flag = True
            except ValueError:
                flag = False
                print("\n -----------------------ERROR!!!------------------------- ")
                print("|                                                        |")
                print("|    You cannot enter special character or alphabets.    |")
                print("|                                                        |")
                print(" -------------------------------------------------------- ")
                break
    return flag

    
    
def forInput():
    key = 0
    while(key == 0):
        a = (input("\nFor Decimal, press 1 ------- For Binary, press 2    :  ")).strip()
        

        while(intValidation(a) == False):
            a = input("\nFor Decimal, press 1 ------- For Binary, press 2    :  ").strip()
        a = int(a)


        if(a == 1):
            sumIndicator = 0
            while(sumIndicator == 0):
                print("\n **************************  Note  **************************** ")
                print("*                                                              *")  
                print("*            Number should not be negative.                    *")
                print("*         Number should not be greater than 255.               *")
                print("*    Sum of Entered Number should not be greater than 255.     *")
                print("*                                                              *")
                print(" ************************************************************** ")
                
                num1 = (input("\nEnter first Decimal Number : ")).strip()
                
                while(validation1(num1) == False ):
                    num1 = (input("\nEnter first Decimal Number again : ")).strip()
                num1 = int(num1)

               
                num2 = input("\nEnter second Decimal Number : ").strip()
                
                
                while(validation1(num2) == False):
                    num2 = input("\nEnter second Decimal Number again : ").strip()
                num2 = int(num2)

                if((num1 + num2) > 255):
                    print("\n -----------------------ERROR!!!------------------------ ")
                    print("|                                                       |")
                    print("|     Sum of entered number should not exceed 255.      |")
                    print("|                                                       |")
                    print(" ------------------------------------------------------- ")

                    
                
                else:
                    key = 1
                    sumIndicator = 1
                    return intToBinaryConv(num1, num2)
       

        elif(a == 2):
            sumIndicator = 0
            while(sumIndicator == 0):
                print("\n **************************  Note  **************************** ")
                print("*                                                              *")
                print("*                You can only enter 0 or 1.                    *")
                print("*         You can only enter 8 digit in maximum.               *")
                print("*   Sum of Entered Number should not be greater than 255.      *")
                print("*                                                              *")
                print(" ************************************************************** ")
                      
                num1 = (input("\nEnter first Binary Number : ")).strip()

                while(validation2(num1) == False):
                    num1 = (input("\nEnter first Binary Number again : ")).strip()

                for i in range(len(num1), 8):
                    num1 = str(0) + num1 

                    
                num2 = (input("\nEnter second Binary Number : ")).strip()


                while(validation2(num2) == False):
                    num2 = (input("\nEnter Second Binary Number again : ")).strip()

                for i in range(len(num2), 8):
                    num2 = str(0) + num2


                if((binaryToIntConv(num1) + binaryToIntConv(num2)) > 255):
                    print("\n -----------------------ERROR!!!------------------------ ")
                    print("|                                                       |")
                    print("|     Sum of entered number should not exceed 255.      |")
                    print("|                                                       |")
                    print(" ------------------------------------------------------- ")
                       
                else:
                    key = 1
                    sumIndicator = 1
                    return num1, num2
       
        else:
            print("\n       ------------- ERROR!! -------------- ")
            print("     |                                     |") 
            print("     |   Only option 1 and 2 available.    |")
            print("     |                                     |")
            print("      ------------------------------------- ")
  

            

