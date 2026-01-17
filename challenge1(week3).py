def temperature_alerts(temp, K, queries):
    """
    temp    : list of temperatures
    K       : threshold difference
    queries : list of queries like ["NEXT 3", "COUNT 0 7"]
    returns : list of outputs (strings or integers)
    """

    N = len(temp)
    alert = [0] * N

    # Next warmer
    stack = []
    for i in range(N):
        while stack and temp[i] >= temp[stack[-1]] + K:
            alert[stack.pop()] = i
        stack.append(i)

    # Next colder
    stack = []
    for i in range(N):
        while stack and temp[i] <= temp[stack[-1]] - K:
            idx = stack.pop()
            if alert[idx] == 0 or i < alert[idx]:
                alert[idx] = i
        stack.append(i)

    # Prefix sum for COUNT
    pref = [0] * N
    pref[0] = 1 if alert[0] != 0 else 0
    for i in range(1, N):
        pref[i] = pref[i - 1] + (1 if alert[i] != 0 else 0)

    results = []

    for q in queries:
        parts = q.split()
        if parts[0] == "NEXT":
            x = int(parts[1])
            results.append(alert[x] if alert[x] != 0 else "No Alert")
        else:  # COUNT
            L, R = int(parts[1]), int(parts[2])
            if L == 0:
                results.append(pref[R])
            else:
                results.append(pref[R] - pref[L - 1])

    return results
temp = [73, 74, 75, 71, 69, 72, 76, 73]
K = 3
queries = ["NEXT 0", "NEXT 3", "COUNT 0 7", "COUNT 4 7"]

print(temperature_alerts(temp, K, queries))
