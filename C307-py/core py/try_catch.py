# try:
#     # Code that might raise an exception
#     # For example: division by zero, file not found, invalid type conversion
# except ExceptionType:
#     # Code to execute if an exception of 'ExceptionType' occurs in the try block
#     # This block handles the error


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    res = a+b
except ValueError:
    print("Invalid input! Please enter numeric values.")
else:
    print("Result:", res)
finally:
    print("Execution completed.")
    
