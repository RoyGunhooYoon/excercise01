"""
game_grid.py contains grid related operaton for dungeon game
(DOC incomplete)
"""

def add_vector(vector1, vector2):
    """Add two vector and return new (x, y) tuple."""
    x1, y1 = vector1
    x2, y2 = vector2

    return (x1 + x2, y1 + y2)


def make_grid(width, height):
    """Make grid with x,y tuple co-ordinate"""
    grid = []
    for x in range(width):
        for y in range(height):
            grid.append((x,y))
    
    return grid

