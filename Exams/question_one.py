#calculate area of radius
def calculate_area():
   area=3.14*(radius**2)
   return area

radius=5
area = 3.14*(5**2)
print(area)
calculate_area()

#1(ii)
def calculating_sum_of_natural_numbers(n):
    if n==0:
        return 0
    else:
        return n + calculate_sum_of_natural_numbers(n-1)
n=4
calculating_sum_of_natural_numbers(4)
    

#1(iii)
numbers=[1,3,5,7,9]
del numbers[2]
numbers.append[10]
print(numbers)

#iv
#v
student_info={
    "name":"Alice",
    "age" :20,
    "grade":"A",
    "city":"New York"
}
print(student_info)
#vi
