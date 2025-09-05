"""
Codewars solutions

No names from the Katas will be given, but I will be showing my solutions-
and thought processes. 

"""



#-- Even vs Odd Returner--

def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
#Modulo % to divide even numbers w/o a emainer
#Use "number" in an if conditional
#I'll use return when returning "Even" or "Odd" as a case of the condition

#--!Updated my previous Kata to this sleek looking ternary expression.. BRILLIANT!



#--Number to string conversion--

def number_to_string(num):
    return str(num)

# ^ I'll just use the str() method and assign the parameter to the name parameter




#--Destroy those string spaces!

def no_space(x):
    return x.replace(' ' ,'')

""" ^ In the given funtion, a parameter x is assigned to a file with
        WAY to many random wide spaces. I'll return x through the .replace()
        function. Making any double wide white spaces into a single space. 
""" 



# --Create a function that accepts a parameter representing a name and returns the message:

# Create  a function
# Assign it a parameter called name
# and returns a message from the kata

def greet(name):
    return f"Hello, {name} how are you doing today?"
    return f"Hello, {name} how are you doing today?"

print(greet("Ryan"))
print(greet("Shingles"))



# add the value "codewars" to the already defined websites array
#Append to the list using the .append() function

websites = []
websites.append("codewars")



# Using a predefided list of consecutive strings.
# Return the first longest string consisting of k consecutive strings taken in the array.
def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    
    longest = ""
    for i in range(len(strarr) - k + 1):
        combined = "".join(strarr[i:i+k])
        if len(combined) > len(longest):
            longest = combined
    return longest

"""
Use the defined function and parameters
use a conditional with k and check if its <= 0 or if k is > then the length of the array
Assign an empty string for the content of a for loops iterations
Loop through the indexs of the strarr to get the length and the range 
subtract from the ranges length from k and add 1
Combine both indexs in an empty string to be assigned back to the temp string
Check if the length of combined is greater then the length of the longest string arr
it'll be true so i can jsut make them equal to each other  and return  the result
 
"""