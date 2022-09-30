def add(a, b):
	return a + b

def test_add():
	assert add(2, 3) == 5
	assert add("space", "ship") == "spaceship"

def subtract(a, b):
	return a - b

def test_subtract():
	assert subtract(2,3) == -1
	assert subtract(3,3) == 0

def multiply(a,b):
	return a * b

def test_multiply():
	assert multiply(5,5) == 25

