# using format() method
print('I love {} for "{}!"'.format('Pravin', 'Ranjan'))   # I love Pravin for "Ranjan!"

# using format() method and referring 
# a position of the object
print('{0} and {1}'.format('Pravin', 'Ranjan'))  # Pravin and Ranjan

print('{1} and {0}'.format('Pravin', 'Ranjan'))  # Ranjan and Pravin


# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.

print(f"I love {'Pravin'} for \"{'Python'}!\"")  #I love Pravin for "Python!"

# using format() method and referring 
# a position of the object
print(f"{'Pravin'} and {'Ranjan'}")  # Pravin and Ranjan


# ***************
# a use of format() method

# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
     .format('Coding', 'Using', other ='Python'))  # 

# using format() method with number 
print("Python :{0:2d}, Version :{1:8.2f}".
      format(12, 00.546))  # 

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))

print("Python: {a:5d},  Coding: {p:8.2f}".format(a = 453, p = 59.058))

