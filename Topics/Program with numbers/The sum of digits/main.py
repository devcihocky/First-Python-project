digit = int(input())

# Obcięcie do trzech ostatnich cyfr
last_three_digits = digit % 1000

# Rozdzielenie cyfr
hundreds = last_three_digits // 100
tens = (last_three_digits % 100) // 10
ones = last_three_digits % 10

# Sumowanie cyfr
sum_of_digits = hundreds + tens + ones

print(sum_of_digits)