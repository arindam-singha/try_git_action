# Simple Python script with basic math operations

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference between a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

# Main program to test the functions
if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Addition of {x} and {y} is: {add(x, y)}")
    print(f"Subtraction of {x} and {y} is: {subtract(x, y)}")
    print(f"Multiplication of {x} and {y} is: {multiply(x, y)}")