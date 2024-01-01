employees=['priya','phani','ais','sri']
for i in employees:
    print(i)
print(employees[:3])
employees[0]='Priyanka'
print(employees)


numbers=[-1,-2,-3,-2,-2]
max=numbers[0]
for i in numbers:
    if i>max:
        max=i

print(max)
print("*******")
x,y,z,a,b=numbers
print(a)

# we have many methods in list such as insert, remove , append,clear, pop,index, sort , reverse, copy
numbers.append(20)
numbers.insert(4,30)
numbers.remove(-2)
print(numbers)
print(numbers.index(-2))
print(5 in numbers)
print(numbers.count(-2))
print(numbers.pop(-3))
#print(numbers.clear())
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers2=numbers.copy()
print(numbers2)