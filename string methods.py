[22:50, 13/07/2021] Teju🥰:
  
 #String Methods

string = "welcome"

#capitalize()=Converts the first character to upper case
capitalized_string = string.capitalize()
print('Old String: ', string)
print('Capitalized String:', capitalized_string)


#casefold()=Converts string into lower case
string = "WELCOME"
print("String=",string)
print("Lowercase String:", string.casefold())


#center()=Returns a centered string
string = "Welcome"
new_string = string.center(20)
print("Centered String: ", new_string)


#count()=Returns the number of times a specified value occurs in a string
string = "Hi This is Lokesh"
substring = "is"
count = string.count(substring)
print("The count is:", count)


#encode()=Returns an encoded version of the string
string = 'Lokesh!'
print('The string is:', string)
string_utf = string.encode()
print('The encoded version is:', string_utf)


#endswith()=Returns true if the string ends with the specified value
text = "Hi,I am Lokesh"
result = text.endswith('Lokesh')
print(result)
result = text.endswith('Hi')
print(result)
result = text.endswith('Hi,I am Lokesh')
print(result)


#expandtabs()=Sets the tab size of the string
str = 'xyz\t12345\tabc'
result = str.expandtabs()
print("str=",result)


#find()=Searches the string for a specified value and returns the position of where it was found
text = "Hi,I am Lokesh"
count=text.find('am')
print(count)


#format()=Formats specified values in a string
# default arguments
print("Hello {}, Your Age is {}.".format("Lokesh", 20))
# integer arguments
print("Your DOB is:{:d}".format(2000))


#format_map()=Formats specified values in a string
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))


#index()=Searches the string for a specified value and returns the position of where it was found
sentence = 'Python programming is fun.'
result = sentence.index('is fun')
print("Substring 'is fun':", result)


#isalnum()=Returns True if all characters in the string are alphanumeric
name = "Lokesh9963"
print(name.isalnum())


#isalpha()=Returns True if all characters in the string are in the alphabet
name = "hi lokesh"
print(name.isalpha())


#isdecimal()=Returns True if all characters in the string are decimals
s = "lokesh is 20"
print(s.isdecimal())


#isdigit()=Returns True if all characters in the string are digits
s = "2000"
print(s.isdigit())


#isidentifier()=Returns True if the string is an identifier
str = 'Lokesh'
print(str.isidentifier())


#islower()=Returns True if all characters in the string are lower case
s = 'Hi Lokesh'
print(s.islower())


#isnumeric()=Returns True if all characters in the string are numeric
s = '123456789'
print(s.isnumeric())


#isprintable=Returns True if all characters in the string are printable
s = 'Lokesh'
print(s)
print(s.isprintable())


#isspace()=Returns True if all characters in the string are whitespaces
s = ' hi '
print(s.isspace())


#istitle()=Returns True if the string follows the rules of a title
s = 'Hi Lokesh.'
print(s.istitle())


#isupper()=Returns True if all characters in the string are upper case
string = "HI LOKESH."
print(string.isupper())


#join()=Joins the elements of an iterable to the end of the string
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))


#ljust()=Returns a left justified version of the string
string = 'lokesh'
width = 11
# print left justified string
print(string.ljust(width))


#lower()=Converts a string into lower case
string = 'LOKESH'
print(string.lower())


#lstrip()=Returns a left trim version of the string
random_string = 'Hi Lokesh '
print(random_string.lstrip('H'))


#maketrans()=Returns a translation table to be used in translations
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))


#partition()=Returns a tuple where the string is parted into three parts
string = "Hi Lokesh"
print(string.partition('Lokesh'))


#replace()=Returns a string where a specified value is replaced with a specified value
string = 'Hi Lokesh'
print(string.replace('Lokesh', 'Lucky'))


#rfind()=Searches the string for a specified value and returns the last position of where it was found
string = 'Hi lokesh'
result = string.rfind('lokesh')
print("Substring 'lokesh':", result)


#rindex()=Searches the string for a specified value and returns the last position of where it was found
string = 'Hi lokesh'
result = string.rindex('Hi')
print("Substring 'Hi':", result)


#rjust()=Returns a right justified version of the string
string = 'lokesh'
width = 8
fillchar = '*'
print(string.rjust(width, fillchar))


#rpartition()=Returns a tuple where the string is parted into three parts
string = "Hi Lokesh"
print(string.rpartition('Lokesh'))


#rsplit()=Splits the string at the specified separator, and returns a list
text= "Hi Lokesh"
print(text.rsplit())


#rstrip()=Returns a right trim version of the string
string = 'Hi Lokesh'
print(string.rstrip())


#split()=Splits the string at the specified separator, and returns a list
string = 'Hi Lokesh'
print(text.split())


#splitlines()=Splits the string at line breaks and returns a list
grocery = 'Milk\nChicken\r\nBread\rButter'
print(grocery.splitlines())


#startswith()=Returns true if the string starts with the specified value
text = "Hi,I am Lokesh"
result = text.startswith('Lokesh')
print(result)
result = text.startswith('Hi')
print(result)


#strip()=Returns a trimmed version of the string
text = "Hi,I am Lokesh"
print(text.strip('esh'))


#swapcase()=Swaps cases, lower case becomes upper case and vice versa
string = 'Hi Lokesh'
print(string.swapcase())


#title()=Converts the first character of each word to upper case
string = 'hi lokesh'
print(string.title())


#translate()=Returns a translated string
firstString = "Hi"
secondString = "Hi"
thirdString = "Lokesh"
string = "Welcome"
print("Original string:", string)
translation = string.maketrans(firstString, secondString, thirdString)
print("Translated string:", string.translate(translation))


#upper()=Converts a string into upper case
string = 'lokesh'
print(string.upper())


#zfill()=Fills the string with a specified number of 0 values at the beginning
text = "Hi Lokesh"
print(text.zfill(11))
