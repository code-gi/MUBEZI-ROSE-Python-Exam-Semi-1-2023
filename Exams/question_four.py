def print_pattern(rows):
    for x in range(1, rows+1):
        for r in range(1, x+1):
            print(r, end="")
        print()
rows=[1,12,1234,12345]
#(ii) Recursive factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print_pattern(5)

#(iii) Function to return the sum of two numbers
def sum_numbers(a, b):
    return a + b
print(sum_numbers(3, 4))
#(iv)
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Year:", self.year)
#(v) An instance to display the information
car = Car("Toyota", 2021)
car.display_info()
