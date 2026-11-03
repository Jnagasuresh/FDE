
# traditional way 
def squarefunc(num):
    return num*num

result = squarefunc(5)
print(result)

result1 = squarefunc(345)
print(result1)

lamdafunc = lambda num: num*num

result2 = squarefunc(345)
print(f"lambda results {result2}")


# Lambda with 2 arguments
lambdaadd = lambda a, b: a+b
result3 = lambdaadd(10,22)
print(f"lambda add {result3}")

#lambda with default value
lambda_1= lambda x, y=10: x+y
lambda_2 = lambda *args: sum(args) # variable positional
lambda_3= lambda **kwargs: kwargs.get("name") # variable keyword

# Condtional logic
sign = lambda n: "positive" if n > 0 else "negative" if n < 0 else "zero"
condresult=sign(-5)   # 'negative'
print(f"conditional {condresult}")

# Most common uses: passing a function as an argument
#Sorting with a custom key:

people = [("Ana", 31), ("Raj", 25), ("Li", 40)]
print(f" sorted array {sorted(people, key=lambda p: p[1])}")              # by age
print(f" Sorted array descending {sorted(people, key=lambda p: (-p[1], p[0]))}")        # age descending, then name
print(f" max {max(people, key=lambda p: p[1])}")                    # ('Li', 40), it is taking age as input for p[1]

#Lambdas capture variables by reference, not by value, so all of these see the final i: