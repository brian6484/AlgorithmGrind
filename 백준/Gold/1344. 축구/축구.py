import math

# Input winning rates and convert to probabilities
win_a = int(input()) / 100
win_b = int(input()) / 100
lose_a = 1 - win_a
lose_b = 1 - win_b

prime = [2, 3, 5, 7, 11, 13, 17]

fact = []
for i in prime:
    fact.append(math.factorial(18) // (math.factorial(i) * math.factorial(18 - i)))

a, b = 0, 0

for i in range(7):
    a += fact[i] * pow(win_a, prime[i]) * pow(lose_a, 18 - prime[i])
    b += fact[i] * pow(win_b, prime[i]) * pow(lose_b, 18 - prime[i])

# Calculate the total probability and round to 10^-6
result = round(a + b - a * b, 10)
print(result)