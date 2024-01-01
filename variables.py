# We use print keyword to print anything on screen
#To declare a string we can use '' or ""
print('Priyanka')
print("Gannavarapu")
# If you want to print a string multiple times just use * , so that the string get's multiplied n number of times and is printed
print('*' * 10 + "\nLet's get started")
#If you want to ask for input , simply use the inbuilt function input
name = input('Hey! What is your name ? ')
age = input('Age ? ')
is_working = input('Are you a working professional? ')
weight_lb = input('Weight ? ')
print("hi " + name  + " \nPlease find below details")
# For type conversion (example if you want to convert to integer) simply use int(variable_name)
print("age : "+ age + " \nworking :"+ is_working + " \nweight in kg :" + str(int(weight_lb)*0.454) )