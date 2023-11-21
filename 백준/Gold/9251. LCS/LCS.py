hola1 = input()
hola2 = input()

# Initialize the DP table with zeros
dp = [[0 for _ in range(len(hola2) + 1)] for _ in range(len(hola1) + 1)]

for i in range(1, len(hola1) + 1):
    for j in range(1, len(hola2) + 1):
        if hola1[i - 1] == hola2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])