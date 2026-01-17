def evacuation_boats(w, priority, limit, queries):
    """
    w        : list of weights
    priority : list (0 or 1)
    limit    : max weight per boat
    queries  : list like ["CANPAIR 0 1", "REMAINING 2"]
    returns  : (minimum_boats, list_of_query_answers)
    """

    N = len(w)

    # Compute minimum boats (greedy)
    people = sorted([(w[i], priority[i]) for i in range(N)])
    l, r = 0, N - 1
    boats = 0

    while l <= r:
        if l != r and people[l][0] + people[r][0] <= limit and not (people[l][1] and people[r][1]):
            l += 1
        r -= 1
        boats += 1

    results = []

    for q in queries:
        parts = q.split()

        if parts[0] == "CANPAIR":
            x, y = int(parts[1]), int(parts[2])
            if w[x] + w[y] <= limit and not (priority[x] and priority[y]):
                results.append("Yes")
            else:
                results.append("No")

        else:  # REMAINING
            B = int(parts[1])
            results.append(max(0, N - 2 * B))

    return boats, results
w = [30, 50, 60, 40, 70, 80]
priority = [1, 0, 1, 0, 0, 1]
limit = 100
queries = ["CANPAIR 0 1", "CANPAIR 0 2", "REMAINING 2"]

boats, answers = evacuation_boats(w, priority, limit, queries)

print("Minimum boats =", boats)
for a in answers:
    print(a)
