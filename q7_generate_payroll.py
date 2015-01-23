__author__ = 'limenglin'

name = str(input("Enter name:"))
hours = int(input("Enter number of hours worked weekly:"))
pay = float(input("Enter hourly pay rate:"))
CPF = int(input("Enter CPF contribution rate(%):"))

print("Payroll statement for", name)
print("Number of hours worked in week:", hours)
print("Hourly pay rate: $", pay)
print("Gross pay = $", pay * hours)
print("CPF contribution at", CPF, "=", CPF / 100 * pay * hours)
print("Net pay = $", (100 - CPF) / 100 * pay * hours)