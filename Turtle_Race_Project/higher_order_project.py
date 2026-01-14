#example
def add(n1, n2):
    return n1 + n2

def calculator(n1, n2, func): #remember a function can take as many inputs as you want & you can define those inputs within your function
    return func(n1, n2)       #thus this calculator function is a higher order function whcih only works with Python not java and other languages

result = calculator(1,8, add) #remember you do not need to add parenthesis of a function within a function
print(result)
