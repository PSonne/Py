print('Hello World.')
string = 'Hi there'
print(string)
print(len(string))

print(' ')

# ** allows for exponentials
result = 2+2**(5*5)
print(result)
# can reuse variables in expressions as arguments
print(result - result)

# normal division is / and floor division is //
result = 5/2
print(result)
result = 5//2
print(result)

print(' ')
result2 = print(2+2)

# can apply multiplications to strings
string = 'aB' * 4
print("'aB' * 4 = " + string)

# method for displaying type of a variable
test_method_type1 = 'test'
print(test_method_type1)
print(type(test_method_type1))
test_method_type2 = 5
print(test_method_type2)
print(type(test_method_type2))

# the .split() method allows to separate words within a string
print('Hello world'.split(' '))
# Without params it slices at whitespaces by default
print('Hello \t\n there,\t\t\t stranger.'.split())

# Display value at [index]
mystring = "Hello World"
print(mystring)
print("Lettre à l'index 2 de 'Hello World'")
print(mystring[2])
print("Lettre à l'index 0 de 'Hello World'")
print(mystring[0])

# Slicing : my_list[start:stop:step] : negative values can be used (stop is exclusive)
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list)
print("\nWith slicing at 0:3")
print(my_list[0:3])  # displays the first 3 elements of a list
print(my_list[:3])  # if you ommit start it's 0 by default
print(my_list[4:])  # skips first 4 elements of a list

# step value of slicing
print(my_list[::2])  # skip every other element

# slicing with negative values
print('\nSlicing with negative values allows to go backward :')
print(my_list[::-1])  # going backward for the whole list
print(my_list[-1:-3:-1])  # with parameters

# reversing a list
lst = [1, 2, 3, 4]
# with the dedicated method
lst.reverse()
print("Using reverse() : ", lst)
lst.reverse()
print("Rereverse second time to get back to ascd order :", lst)

# creating a second, reversed list from first one
lst2 = lst[::-1]
print("Reversed 2nd list :", lst2)

# reversing a list with slicing : diff here is that this creates a new list
print('\nBy slicing, creating a new list :')
lst = [1, 2, 3, 4]
print(lst)
print(lst[::-1])
print(lst)  # the original list is untouched

# with reverse iterator (extremly low memory and CPU usage)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
rev = reversed(lst)
for i in rev:
    print(i)

print('\nSlicing strings :')
# with strings
mystring = 'Hello World'
print(mystring)
print(mystring[::-1])

# chaining calls on one line
# replace changes a word to another, upper for upper case
print('Hello world'.replace('world', 'student').upper())

replaceTest = "test replace : is it working?"
print(replaceTest)
print('And with replace :')
print(replaceTest.replace('?', ', yes it is!'))

# Formated strings
print(' ')
my_age = 34
print(f'My age is {my_age}')  # form of destructuring within the string

print(' ')
print(f'3+4={3+4}')
print(f'My age is, unfortunately, not {my_age - 8}'
      f'\nMy age is, actually, {my_age}')

name = 'John'
age = 60
print(f"{name = }, {age = }")

print('\n')
# =================== Print function :
print('===== Print function : ')
print(1)
print('Some text')
print('a tab:\t and some text')
print('\nwith a lign break')
print()  # same above
print('This is my age :', 34)

print(' ')
# =================== Booleans :
print('===== Booleans and conditionals : ')
door_is_locked = True
if door_is_locked:
    print("Mom', open the door!")
else:
    print('Everything is ok !')

# Comparison operators
print('Operators')
print('2 > 1 :', 2 > 1)  # expected : true
print('2 > 1 :', 2 < 1)  # expected : false
print('2 < 3 < 4 < 5 < 6 :', 2 < 3 < 4 < 5 < 6)  # expected : true
print('2 < 3 > 2 :', 2 < 3 > 2) # expected : true
print('3 <= 3 :', 3 <= 3) # expected : true
print('3 >= 2 :', 3 >= 2) # expected : true
print('2 == 2 :', 2 == 2) # expected : true
print('4 != 5 :', 4 != 5) # expected : true
print('\nWith strings : \n')
print('a' == 'a')
print('a' > 'b')
# Remark : in the table of characters uppercase letters are smaller than lowercase and digits are smaller than letters

# For and While loop
print('\n===== For and While\n')
for letter in 'Hello':
    print(letter)
