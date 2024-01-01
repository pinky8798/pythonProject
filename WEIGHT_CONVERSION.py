# PROBLEM STATEMENT :  Program to convert weight from lb - kg and viceversa based on user input

weight_value = input("Hello! Please enter your weight : ")
weight_unit = input("Enter L for weight in LBs and K for weight in KGs : ")

if weight_unit.upper() == 'L':
    weight = int(weight_value) * 0.454
    print(f"Your weight in KGs is {weight}")
elif weight_unit.upper() == 'K':
    weight = int(weight_value) / 0.454
    print(f"Your weight in LBs is {weight}")
else:
    print("Sorry! weight can only be in LBs or KGs")
