import forInput as a #all the methods from forInput are stored in a
import Conversion as b

def forGate():
    data = a.forInput() #the value returned by forInput() method is stored
    num1 = data[0]      #value is stored in num1 from the first index of tuple
    num2 = data[1]      #value is stored in num2 from the second index of tuple

    index = 7
    carry = 0
    list_ = [0, 0, 0, 0, 0, 0, 0 ,0] #create list of length 8
    while index >= 0:
        xOrGate = int(num1[index]) ^ int(num2[index])
        andGate = int(num1[index]) * int(num2[index])

        xOrGate1 = xOrGate ^ carry
        andGate1 = xOrGate * carry

        orGate = andGate | andGate1

        carry = (orGate)
        list_[index] = str(xOrGate1)
        index = index - 1

    
    
    
    intNum1 = b.binaryToIntConv(num1)
    intNum2 = b.binaryToIntConv(num2)
    answer = ''.join(list_)
    sumInt = b.binaryToIntConv(answer)

    
    print("\n\n *********************    BIT-ADDER OUTPUT   ********************** ")
    print("*                                                                  *")
    print("*    1st Binary Value : ", num1, "   | 1st Decimal Value : ", "{0:0=3d}    *".format(intNum1))
    print("*    2st Binary Value : ", num2, "   | 2st Decimal Value : ", "{0:0=3d}    *".format(intNum2))
    print("*                     + ----------- ", "|                   + -----   *")
    print("*       Sum in Binary : ", answer, "   |    Sum in Integer : ", "{0:0=3d}    *".format(sumInt) )
    print("*                                                                  *")
    print(" ****************************************************************** ")
    
