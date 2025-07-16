from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_datetime = datetime.now()

current_year = current_datetime.year

current_year


year_to_100 = current_year + (100 - age)

print (f"My name is {name} and I will in 100 yrs old in {year_to_100}")