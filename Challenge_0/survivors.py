def findSurvivorPosition(n, k):
    captured = list(range(1, n + 1))
    current = 0

    while len(captured) > 1:
        current = (current + k - 1) % len(captured)
        captured.pop(current)

    return captured[0]

n = int(input("Number of people: "))
k = int(input("Eliminate every kth person: "))

print("Survivor:", findSurvivorPosition(n, k))