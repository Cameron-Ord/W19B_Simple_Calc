



print("Select an operation to perform")
print("1, ADD")
print("2, SUBTRACT")
print("3, MULTIPLY")
print("4, DIVIDE")

    #setting exceptions for ValueError and TypeError


try:

    #getting the string input from user

    operation = input("SELECT OPERATION:")

    #changing the data type to int

    operation = int(operation)

except ValueError:

    print("please enter a number")

except TypeError:

    print("unsupported data type, please enter a number")

except:
    print("error")

    
def add_numbers():

    try:

        #getting the number input from user and then converting the data type to float

        num = input("Enter a number:")

        num = float(num)

        #returns the number

        return num
    
        #if incorrect value or type is entered, handles the error

    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

def subtract_numbers():

    try:

         #getting the number input from user and then converting the data type to float

        num = input("Enter a number:")

        num = float(num)

        #returns the number

        return num
    
    
        #if incorrect value or type is entered, handles the error

    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

def multiply_numbers():

    try:

         #getting the number input from user and then converting the data type to float

        num = input("Enter a number:")

        num = float(num)

        #returns the number

        return num
    
        #if incorrect value or type is entered, handles the error
    
    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

def divide_numbers():

    try:

         #getting the number input from user and then converting the data type to float

        num = input("Enter a number:")
        num = float(num)

        #returns the number

        return num
    
        #if incorrect value or type is entered, handles the error
    
    except ValueError:
        
        print("please enter a number")

    except TypeError:

        print("unsupported data type, please enter a number")
    
    except:
        print("operation failed")

try:

#if user inputs 1 at operation selection, calls the function

    if(operation == 1):
        
        while(True):

            #loops the function call which is returned inside the function

            num1 = add_numbers()

            num2 = add_numbers()

            added = num1 + num2

            print(added)

            #breaks the loop once both both nums are entered since neither can be Null once values are assigned

            if(num1 == None or num2 == None):

                print("error")

            else:

                break    
        
    #if user inputs 2 at operation selection, calls the function

    elif(operation == 2):

        while(True):

            num1 = subtract_numbers()

            num2 = subtract_numbers()

            subtracted = num1 - num2

            print(subtracted)

            #breaks the loop once both both nums are entered since neither can be Null once values are assigned

            if(num1 == None or num2 == None):

                print("error")

            else:

                break

    #if user inputs 3 at operation selection, calls the function

    elif(operation == 3):

        while(True):
            num1 = multiply_numbers()

            num2 = multiply_numbers()

            multiplied = num1 * num2

            print(multiplied)

            #breaks the loop once both both nums are entered since neither can be Null once values are assigned

            if(num1 == None or num2 == None):

                print("error")
                
            else:

                break

    #if user inputs 4 at operation selection, calls the function

    elif(operation == 4):
    
        while(True):
                
            num1 = divide_numbers()

            num2 = divide_numbers()

            divided = num1 / num2

            print(divided)

            #breaks the loop once both both nums are entered since neither can be Null once values are assigned

            if(num1 == None or num2 == None):

                print("error")

            else:

                break

    elif(operation > 4):

        print("please choose a number within parameters")

    #handles exceptions where user inputs incorrect values or types when choosing operation

except TypeError:

    print("unsupported data type, please enter a number")

except ValueError:

    print("please enter a number")

except:print("error")

