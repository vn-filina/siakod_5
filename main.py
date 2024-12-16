import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    weights = {
        'Д': 1,
        'З': 2,
        'П': 3,
        'Х': float('inf'),
        '#': 1
    }

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    open_set = []
    heapq.heappush(open_set, (0, start))

    cost_so_far = {start: 0}

    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, cost_so_far[goal]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                terrain = grid[neighbor[0]][neighbor[1]]
                new_cost = cost_so_far[current] + weights[terrain]

                if terrain != 'Х' and (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current

    return None, float('inf')

def display_path(grid, path):
    if not path:
        print("Путь не найден.")
        return

    display_grid = [row[:] for row in grid]
    for x, y in path:
        if display_grid[x][y] not in ['#', 'Д']:
            display_grid[x][y] = '*'
    for row in display_grid:
        print(' '.join(row))

def tests():
    print("Тест 1: Простой путь")
    grid = [
        ['Д', 'Д', 'Д', 'Д', '#'],
        ['Д', 'Х', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д']
    ]
    start = (0, 0)
    goal = (0, 4)
    path, length = a_star(grid, start, goal)
    print("Найденный путь:", path)
    print("Длина пути:", length)
    display_path(grid, path)

    print("\nТест 2: Препятствие на пути")
    grid = [
        ['Д', 'Д', 'Х', 'Д', '#'],
        ['Д', 'Х', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д']
    ]
    start = (0, 0)
    goal = (0, 4)
    path, length = a_star(grid, start, goal)
    print("Найденный путь:", path)
    print("Длина пути:", length)
    display_path(grid, path)

    print("\nТест 3: Путь через песок")
    grid = [
        ['Д', 'Д', 'Д', 'П', '#'],
        ['Д', 'Д', 'Д', 'П', 'Д'],
        ['Д', 'Д', 'Д', 'П', 'Д'],
        ['Д', 'Д', 'Д', 'П', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д']
    ]
    start = (4, 0)
    goal = (0, 4)
    path, length = a_star(grid, start, goal)
    print("Найденный путь:", path)
    print("Длина пути:", length)
    display_path(grid, path)

    print("\nТест 4: Путь через разные типы клеток")
    grid = [
        ['Д', 'З', 'П', 'Д', '#'],
        ['Д', 'Д', 'З', 'Д', 'Д'],
        ['Д', 'П', 'П', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д']
    ]
    start = (4, 0)
    goal = (0, 4)
    path, length = a_star(grid, start, goal)
    print("Найденный путь:", path)
    print("Длина пути:", length)
    display_path(grid, path)

    print("\nТест 5: Нет пути")
    grid = [
        ['Д', 'Д', 'Д', 'Д', '#'],
        ['Х', 'Х', 'Х', 'Х', 'Х'],
        ['Д', 'Д', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д'],
        ['Д', 'Д', 'Д', 'Д', 'Д']
    ]
    start = (2, 0)
    goal = (0, 4)
    path, length = a_star(grid, start, goal)
    print("Найденный путь:", path)
    print("Длина пути:", length)
    display_path(grid, path)

if __name__ == "__main__":
    tests()
