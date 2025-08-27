code = input().strip()
counter = 0
collection = []
if "if" not in code:
    print(-1)
else:
    for char in code:
        if char == "{":
            counter += 1
        elif char == "i":
            collection.append(counter)
        elif char == "}":
            counter -= 1
    n = len(collection)

    collection.sort()
    print(collection[((n + 1) // 2) - 1])
