



print("Select an operation to perform")
print("1, ADD")
print("2, SUBTRACT")
print("3, MULTIPLY")
print("4, DIVIDE")


try:

    operation = input("SELECT OPERATION:")

    operation = int(operation)

except ValueError:

    print("please enter a number")

except TypeError:

    print("unsupported data type, please enter a number")

except:
    print("error")

    
def add_numbers():

    try:
        num = input("Enter a number:")
        num = float(num)
        return num
    
    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

def subtract_numbers():

    try:
        num = input("Enter a number:")
        num = float(num)
        return num
    
    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

def multiply_numbers():

    try:
        num = input("Enter a number:")
        num = float(num)
        return num
    
    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

def divide_numbers():

    try:
        num = input("Enter a number:")
        num = float(num)
        return num
    
    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

try:

    if(operation == 1):
        
        while(True):

            num1 = add_numbers()

            num2 = add_numbers()

            added = num1 + num2

            print(added)

            if(num1 == None or num2 == None):

                print("error")

            else:

                break    
        


    elif(operation == 2):

        while(True):

            num1 = subtract_numbers()

            num2 = subtract_numbers()

            subtracted = num1 - num2

            print(subtracted)

            if(num1 == None or num2 == None):

                print("error")

            else:

                break



    elif(operation == 3):

        while(True):
            num1 = multiply_numbers()

            num2 = multiply_numbers()

            multiplied = num1 * num2

            print(multiplied)

            if(num1 == None or num2 == None):

                print("error")
                
            else:

                break



    elif(operation == 4):
    
        while(True):
                
                num1 = divide_numbers()

                num2 = divide_numbers()

                divided = num1 / num2

                print(divided)

                if(num1 == None or num2 == None):

                    print("error")

                else:

                    break

    elif(operation > 4):

        print("please choose a number within parameters")

except TypeError:

    print("unsupported data type, please enter a number")

except ValueError:
    
    print("please enter a number")

except:print("error")

