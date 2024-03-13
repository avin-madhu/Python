# Input a string, replace all the occurances of the first character with $ except the first character.

str = input("Enter a string: ")
first = str[0]
print( str[0]+str[1:].replace(first, '$'))
