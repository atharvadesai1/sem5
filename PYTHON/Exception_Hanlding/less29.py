class BaseError(Exception):
    pass

class HighValueError(BaseError):
    pass

class LowValueError(BaseError):
    pass

value = 51

while(True):
    try:
        num = int(input("Enter a number: "))
        if(num>value):
            raise HighValueError
        elif(num<value):
            raise LowValueError
        
    except HighValueError:
        print('The number is high, try again!')
    
    except LowValueError:
        print('The number is low, try again!')

    except KeyboardInterrupt:
        print('\nYou stopped the program by ctrl+c')
        break

    except ValueError:
        print('Enter the valid input!')
    else:
        print(f"Hurray! you found the number {num}")
        break

    finally:
        print('Code executed.')

    