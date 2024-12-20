from aocd import get_data, submit
import networkx

day, year = 20, 2024
data = get_data(day=day, year=year)
data = data.splitlines()

m, n = len(data), len(data[0])
ex = ey = -1

G = networkx.Graph()

for i in range(m):
    for j in range(n):
        if data[i][j] in '.SE':
            G.add_node((i, j))

for i in range(m):
    for j in range(n):
        if data[i][j] in '.SE':
            if data[i][j] == 'E':
                ex, ey = i, j
            for dx, dy in [(0, 1), (1, 0)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and data[nx][ny] != '#':
                    G.add_edge((i, j), (nx, ny))

shortest_paths = dict(networkx.shortest_path_length(G, target=(ex, ey)))

def get_reachable(x, y, max_dist):
    reachable = []
    for dx in range(-max_dist, max_dist + 1):
        remaining_dist = max_dist - abs(dx)
        for dy in range(-remaining_dist, remaining_dist + 1):
            if dx == dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and data[nx][ny] in '.SE':
                reachable.append((nx, ny))
    return reachable

def solve(cheat_size):
    res = 0
    for node in G.nodes:
        i, j = node
        reachable = get_reachable(i, j, cheat_size)
        for dx, dy in reachable:
            cost = abs(i - dx) + abs(j - dy)
            savings = shortest_paths[(i, j)] - (shortest_paths[(dx, dy)] + cost)
            if savings >= 100:
                res += 1
    return res

submit(solve(2), part="a", day=day, year=year)
submit(solve(20), part="b", day=day, year=year)