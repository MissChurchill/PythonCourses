print('Hello World')

name = input('Enter your name:\n')

amount = int(10.6)

roll = random.randint(1,6)

# defining a function begins with def then function name and in parentheses the parameters/values

def greeting(name):
    print('Hello', name)
    
# Main program
input_name = input('Enter your name:\n')

greeting(input_name)

# using global variables
name = input('Enter your name:\n')
greeting()

def addition(a, b):
    return a + b

num1 = float(input('Enter your 1st number:\n'))
num2 = float(input('Enter your 2nd number:\n')) 
result = addition(num1, num2) 
print('The result is', result)  
