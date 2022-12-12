# Calculator
def calculate(first_number,second_number,operator):
    # Additiion (+)
    if(operator=='+'):
        return first_number+second_number
    # Substraction (-)
    elif(operator=='-'):
        return first_number-second_number
    # Multiplication (*)
    elif(operator=='*'):
        return first_number*second_number
    # Division(/)
    elif(operator=='/'):
        return int(first_number/second_number)
    # Power 2 (**)
    elif(operator=='^'):
        return first_number**second_number
    # Unknown
    else:
        return 'Sorry, but I cannot understand your operation'
