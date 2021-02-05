a = float(input("Enter first number: "))
b = float(input("Enter second number: "))


def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mult(a, b):
	return a * b

def div(a, b):
	return a / b

print(a, "+", b, "=", add(a,b))
print(a, "-", b, "=", sub(a,b))
print(a, "*", b, "=", mult(a,b))

if b == 0:
	print(a, "/", b, "= N/A")
else:
	print(a, "/", b, "=", div(a,b))