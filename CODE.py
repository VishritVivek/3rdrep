num=int(input("YOUR NUMBER : "))
def factorial(n):
    if n>=2:
        return n*(factorial(n-1))
    else:
        return 1
print("FACTORIAL IS : ",(factorial(num)))
