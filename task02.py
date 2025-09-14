#task 5 Дар'я Романова
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

first = min(a,b)
second = max(a,b)

sum = second * (second + 1) // 2 - (first - 1) * first // 2

print ("The sum of numbers between them is:", sum)

