import heapq
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal, R, C):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    open_set = []
    heapq.heappush(open_set, (0, start)) 
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        for mv in moves:
            nr, nc = current[0] + mv[0], current[1] + mv[1]

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current

    return None, None
def main():
    try:
        with open("input.txt", "r") as file:
            R, C = map(int, file.readline().split())

            grid = []
            for _ in range(R):
                grid.append(list(map(int, file.readline().split())))

            sr, sc = map(int, file.readline().split())
            tr, tc = map(int, file.readline().split())

    except FileNotFoundError:
        print("ERROR: input.txt file not found! Place input.txt beside A_serche.py")
        return

    start = (sr, sc)
    goal = (tr, tc)

    path, cost = a_star_search(grid, start, goal, R, C)

    if path is None:
        print("Path not found using A*")
    else:
        print(f"Path found with cost {cost} using A*")
        print("Shortest Path:", end=" ")
        print(path)


if __name__ == "__main__":
    main()
