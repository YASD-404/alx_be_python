def perform_operation(num1, num2,operation):
        if operation=='add':
            return num1+num2
        elif operation=='subtract':
            return num1-num2
        elif operation=='multiply':
            return num1*num2
        elif operation=='divide':
            if num2==0:
                return "ZeroDivisionError"
            else:
                return num1/num2
        else:
            print("Wrong data type")
    
print(perform_operation(5,6,'add'))