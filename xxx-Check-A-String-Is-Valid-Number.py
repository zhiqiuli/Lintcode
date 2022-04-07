'''
Given a long string, write a method that returns true if the string is a valid number or false otherwise. Only integers and decimals should be considered as valid. In other words, only characters allowed are digits, "-" and ".". The string can be very long (think millions of characters) and no built-in function/class can handle it without overflowing or losing precision. Not necessary to consider 1e4 or log.
'''

def checkIfValid(string):
    minus   = False
    decimal = False
    
    for i in range(len(string)):
        
        if string[i].isdigit():
            continue
        
        elif string[i] == '-':
            # appears once
            if minus:
                return False
            if i != 0:
                return False
            minus = True

        elif string[i] == '.':
            if decimal:
                return False
            decimal = True

        else:
            return False
        
    return True

print(checkIfValid('123'))
print(checkIfValid('123.3'))
print(checkIfValid('123.3.3'))
print(checkIfValid('12a.3'))
print(checkIfValid('-123.3'))
print(checkIfValid('-.3'))
