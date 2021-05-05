# Lambda functions
implementation_lambda = lambda x: x * 2

print(implementation_lambda(4)) # Output: 8

# or

print((lambda x: x * 2)(4)) # Output: 8

def implementation_function(num):
    return lambda x: x * num

implementation_function_with_lambda = implementation_function(90) # num = 90

print(implementation_function_with_lambda(11)) # Output: 990