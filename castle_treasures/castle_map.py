class CastleGraph:
    def __init__(self, n, m, castle_map):
        self.N = n
        self.M = m
        self.castle_map = castle_map
        self.graph = {}
        self.keys = {}
        self.doors = {}
        self.coins = {}
        self.room_ids = {}  # Initialize the room IDs dictionary
        self.collected_coins = 0  # Initialize the collected coins counter
        self.collected_keys = 0
        self.neighbors = []

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def build_graph(self):
        for x in range(self.N):
            for y in range(self.M):
                cell = self.castle_map[x][y]

                if cell == "#":
                    continue

                node = (x, y)
                neighbors = []

                if cell == "P":
                    self.start_x, self.start_y = x, y

                if cell == "K":
                    self.keys[node] = True

                if cell == "D":
                    self.doors[node] = True

                if cell == "G":
                    self.coins[node] = True

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.N and 0 <= ny < self.M:
                        if self.castle_map[nx][ny] != "#":
                            self.neighbors.append((nx, ny))

                for neighbor in neighbors:
                    self.add_edge(node, neighbor)

    def dfs(self, node, visited, room_id):
        visited[node] = True
        self.room_ids[node] = room_id

        if node in self.keys:
            self.keys[node] = False
            self.collected_keys += 1

        if node in self.doors:
            if self.collected_keys == 0:
                min_neighbor_room_id = room_id
                return min_neighbor_room_id
            self.doors.pop(node)

        if node in self.coins:
            self.coins[node] = False
            self.collected_coins += 1

        min_neighbor_room_id = room_id

        for neighbor in self.graph.get(node, []):
            if not visited[neighbor]:
                neighbor_room_id = self.dfs(neighbor, visited, room_id)
                min_neighbor_room_id = min(min_neighbor_room_id, neighbor_room_id)

        return min_neighbor_room_id

    def find_maximum_rooms_and_coins(self):
        visited = {(x, y): False for x in range(self.N) for y in range(self.M)}
        max_rooms = 0
        max_coins = 0

        for x in range(self.N):
            for y in range(self.M):
                node = (x, y)

                if not visited[node] and self.castle_map[x][y] != "#":
                    self.collected_coins = 0  # Reset collected coins for each room
                    max_rooms += 1
                    max_coins = max(max_coins, self.collected_coins)

        return max_rooms, max_coins


def read_input(input_file):
    with open(input_file, "r") as f:
        N, M = map(int, f.readline().split())
        castle_map = [list(f.readline().strip()) for _ in range(N)]

    return N, M, castle_map


def write_output(output_file, max_rooms, max_coins):
    with open(output_file, "w") as f:
        f.write(f"{max_rooms}\n")
        f.write(f"{max_coins}\n")
