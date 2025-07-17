num = int(input("Enter your number : "))

div_range = range(1,num+1)

divisor = []

for i in div_range:
    if num % i == 0:
        divisor.append(i)

print (divisor)