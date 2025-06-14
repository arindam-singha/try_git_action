import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from first_project.first_script import add, subtract, multiply

# Test cases for the first_script module
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_mixed_operations():
    assert add(subtract(5, 3), multiply(2, 2)) == 6
    assert subtract(add(1, 1), multiply(2, 1)) == 0
    assert multiply(add(1, 2), subtract(5, 3)) == 6
