def format_name(first_name, last_name):
	# code goes here
    string = "Name: "
    if first_name != "" and last_name != "":
        string += first_name + ", " + last_name
    elif first_name == "" and last_name !="":
        string += last_name
    elif first_name !="" and last_name == "":
        string += first_name
    else:
        return ""
  
    return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

"""
def format_name(first_name, last_name):
	# code goes here
	string = "Name: "
	if first_name != "" and last_name != "":
		string += last_name + ", " +first_name
	elif first_name != "" and last_name == "":
		string += first_name
	elif first_name == "" and last_name != "":
		string += last_name 
	else:
		string = ""
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
"""
def fractional_part(numerator, denominator):

	# Operate with numerator and denominator to 
    # keep just the fractional part of the quotient
    if denominator:
        result = numerator/ denominator
    else:
        return 0
    result -= int(result)
    return result


print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


"""
def fractional_part(numerator, denominator):
	if denominator:
		result = numerator/denominator
	else:
		result= 0 
	result = result - int(result)
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	return result

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

"""