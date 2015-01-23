__author__ = 'limenglin'

running = True
while running:
    n = int(input("Enter a integer between 1 to 127:"))
    if 0 < n < 128:
        running = False
    else:
        print("Invalid input. Try again!")

print("ASCII character:", chr(n))