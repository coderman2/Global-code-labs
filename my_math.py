def calculate(operation,num1,num2):
    operation = operation.upper()
    
    if operation == "ADD":
        result= num1 + num2
    elif operation == "SUBTRACT":
        result= num1 - num2
    elif operation == "MULTIPLY":
        result= num1 * num2
    elif operation == "DIVIDE":
        if num2 !=0:
           result= num1 / num2
        else:
            return "cannot divide by zero"
    else:
        return "Invalid format"
    
    return result

operation = input("What operation do you want to perform?\n")
num1 = int(input("Input first number \n"))
num2 = int(input("Input second number \n"))

result = calculate(operation,num1,num2)
print(result)

    