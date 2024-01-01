customers={"name":"priya", "age":25 ,"email":"priya@gmail.com"}
customers["birthday"]="7/8/1998"
print(customers)
print(customers["name"])
print(customers.get("nickname","pri"))


phone_num = input("enter phone number: ")
dict1={'1':'one','2':'two'}
output=''
for i in phone_num:
    output += (dict1.get(i,"!")) + " "

print(output)