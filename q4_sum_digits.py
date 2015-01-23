__author__ = 'limenglin'

running = True

while running:
    n = int(input("Enter a integer between 0 to 1000:"))
    if 0 < n < 1000:
        running = False
    else:
        print("Invalid input. Try again")

sum = n % 10 + (n // 10) % 10 + n // 100

print("sum of digits equals to", sum)