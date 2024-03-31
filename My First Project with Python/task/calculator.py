# Write your code here


print("Earned amount")
income = float(202+118+2250+1680+1075+80)

print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")

print("Income: " + str(income))

print("Income: $" + str(income))
print("Staff expenses:")
expenses = input()
print("Other expenses:")
other_expenses = input()
net_income = float(income) - float(expenses) - float(other_expenses)

print("Net income: $" + str(net_income))