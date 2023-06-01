#Create a Calculator program, using functions and dictionaries
def addition(val1,val2):
    return val1+val2

def subtraction(val1,val2):
    return val1-val2

def multiplication(val1,val2):
    return val1*val2

def division(val1,val2):
    return val1/val2

def power(val1,val2):
    return val1**val2

operation_dict={"+":addition,"-":subtraction,"*":multiplication,"/":division,"**":power}

def calc(operator,val1,val2):
    calculation_to_perform=operation_dict[operator]
    return calculation_to_perform(val1,val2)

continue_operation=True
val1=float(input("Enter 1st value: "))
while continue_operation:
    operation_to_perform=input("what Operation do you want to perform: \n+ or - or * or / or ** \n")
    val2=float(input("Enter 2nd value: "))
    result= calc(operation_to_perform,val1,val2)
    print(f"The value of {val1}{operation_to_perform}{val2}={result}")
    continue_val=input("Do you continue types 'yes' or 'no': ")
    if continue_val=="yes":
        val1= result
        #continue
    else:
        continue_operation=False


#or
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False

calculator()