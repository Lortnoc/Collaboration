"""The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly."""
def counter(start, stop):
	x = start
	if ___:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


"""

Problem: This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

1 2 3

2 4 6

3 6 9
"""
def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(x*y, end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above