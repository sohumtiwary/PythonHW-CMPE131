def cacti_number(plot):
    if plot is None:
        raise TypeError("plot must be a 2-D list")

    if not isinstance(plot, list) or (plot and not isinstance(plot[0], list)):
        raise TypeError("plot must be a 2-D list")

    if not plot:
        return 0

    rows, cols = len(plot), len(plot[0])

    for row in plot:
        if not isinstance(row, list) or len(row) != cols:
            raise TypeError("plot must be a rectangular 2-D list")
        if any(cell not in (0, 1) for cell in row):
            raise TypeError("plot may only contain 0 or 1")

    def adjacent_cells(r, c):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    for r in range(rows):
        for c in range(cols):
            if plot[r][c] == 1:
                if any(plot[nr][nc] == 1 for nr, nc in adjacent_cells(r, c)):
                    raise ValueError("input plot already has adjacent cacti")

    grid = [row.copy() for row in plot]
    placed = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and all(grid[nr][nc] == 0 for nr, nc in adjacent_cells(r, c)):
                grid[r][c] = 1
                placed += 1

    return placed
