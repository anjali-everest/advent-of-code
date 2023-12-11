def read_data() -> list:
    with open("input.txt") as f:
        return f.read().splitlines()

def find_galaxies(grid: list) -> list:
    return [(x, y) for y, row in enumerate(grid) for x, galaxy in enumerate(row) if galaxy == '#']

def find_empty_columns(grid: list) -> list:
    return [x for x in range(len(grid[0])) if all([row[x] == '.' for row in grid])]

def find_empty_rows(grid: list) -> list:
    return [y for y, row in enumerate(grid) if all([galaxy == '.' for galaxy in row])]

# find the manhattan distance between two points
def shortest_paths_sum(galaxies, empty_rows: list, empty_cols: list, mode:int) -> int:
    sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ax, ay = galaxies[i]
            bx, by = galaxies[j]

            ax, bx = min(ax, bx), max(ax, bx)
            ay, by = min(ay, by), max(ay, by)

            count = (bx - ax) + len(set(empty_cols) & set(range(ax, bx + 1))) * (1 if mode == 1 else (1000000 - 1))
            count += (by - ay) + len(set(empty_rows) & set(range(ay, by + 1))) * (1 if mode == 1 else (1000000 - 1))

            sum += count

    return sum

def cosmic_expansion():
    grid = read_data()
    galaxies = find_galaxies(grid)
    empty_cols = find_empty_columns(grid)
    empty_rows = find_empty_rows(grid)
    print(shortest_paths_sum(galaxies, empty_rows, empty_cols, 1))
    # return shortest_paths_sum(galaxies, empty_rows, empty_cols, 1000000)

cosmic_expansion()

