from collections import defaultdict, deque

def broadcast_network_feed(N, K, operations):
    """
    N          : number of units (1..N)
    K          : max recent messages kept per unit
    operations : list of operations as strings
                 e.g. ["S 1 2", "B 2 5", "F 1"]

    returns    : list of outputs for each F operation
    """

    subscriptions = [set() for _ in range(N + 1)]
    messages = defaultdict(deque)
    msg_id = 0

    results = []

    for op in operations:
        parts = op.split()

        if parts[0] == "S":
            u, v = int(parts[1]), int(parts[2])
            subscriptions[u].add(v)

        elif parts[0] == "U":
            u, v = int(parts[1]), int(parts[2])
            subscriptions[u].discard(v)

        elif parts[0] == "B":
            u = int(parts[1])
            msg_id += 1
            messages[u].append(msg_id)
            if len(messages[u]) > K:
                messages[u].popleft()

        elif parts[0] == "F":
            u = int(parts[1])
            feed = []

            for sender in subscriptions[u] | {u}:
                feed.extend(messages[sender])

            feed = sorted(feed, reverse=True)[:10]

            if not feed:
                results.append("EMPTY")
            else:
                results.append(" ".join(map(str, feed)))

    return results
N = 3
K = 2

operations = [
    "S 1 2",
    "S 1 3",
    "B 2 5",
    "B 3 9",
    "F 1",
    "U 1 2",
    "B 3 6",
    "F 1",
    "F 2"
]

output = broadcast_network_feed(N, K, operations)

for line in output:
    print(line)
