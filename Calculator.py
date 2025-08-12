def calculator():
    first_number = int(input('Enter first number. '))
    
    second_number = int(input('Enter second number. '))
    
    operator = input('Enter operator to perform operation: +, *, / , - ')
    
    if operator == '+':
        print('The result is ' , first_number + second_number)
    
    elif operator == '*':
        print('The result is ', first_number * second_number)
    
    elif operator == '/':
        print('The result is ' ,first_number / second_number)
    
    elif operator == '-':
        print('The result is ' ,first_number - second_number)
        
    else:
         print('Invalid')
         
calculator()