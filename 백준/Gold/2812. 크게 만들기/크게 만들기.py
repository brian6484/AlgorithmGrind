n, k = map(int, input().split())
number = input()

stack = [number[0]]

for i in range(1, n):
    num = number[i]
    while stack and stack[-1] < num and k:
        stack.pop()
        k -= 1
    stack.append(num)

result = ""
while stack:
    result += stack.pop()

result=result[::-1]
if k:
    result = result[:-k]

print(result)