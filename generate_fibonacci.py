prev = 0
current = 1
fib_list = []

for i in range(93):
    fib_list.append(prev)
    next = current + prev
    prev = current
    current = next

print(fib_list)
