# One try can have multiple except blocks . First the code in try is executed and based on the type of encountered error (if any) it executes the respective except block of cde

try :
    age=int(input('Enter Age: '))
    income=20000
    risk=income/age
    print(f"Age : {age}")
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Age can't be Zero !")