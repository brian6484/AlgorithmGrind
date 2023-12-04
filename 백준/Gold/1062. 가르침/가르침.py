from itertools import combinations

def word2bit(word):
    bit = 0
    for char in word:
        bit |= 1 << (ord(char) - ord('a'))
    return bit

n, m = map(int, input().split())
lst = [input().strip() for _ in range(n)]  # Use strip() to remove leading/trailing whitespaces
bits = list(map(word2bit, lst))
if m < 5:
    print(0)
    exit()
base_bit = word2bit('acint')
alphabet = [1 << i for i in range(26) if not (base_bit & (1 << i))]

answer = 0

for comb in combinations(alphabet, m - 5):
    know_bit = sum(comb) | base_bit  # Use 'comb' directly instead of 'combination'

    count = 0
    for bit in bits:
        if bit & know_bit == bit:  # Check if bit is a subset of know_bit
            count += 1

    answer = max(answer, count)

print(answer)