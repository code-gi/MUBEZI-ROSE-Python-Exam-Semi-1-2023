#calculate area of radius
def calculate_area(radius_of_a_circle):
   area=3.14*(radius_of_a_circle)**2
   print(area_of_a_circle)
calculate_area(5)


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
numbers.del[2]
numbers.append[10]
print(numbers)

#iv
even_numbers=[2,4,6,8,10]
new_list=[]
new_list.append(even_numbers)
print(new_list)
#v
student_info={
    "name":"Alice",
    "age" :20,
    "grade":"A",
    "city":"New York"
}
print(student_info)
student_info[age]=25
print(student_info)
#vi
