def polygon_area(vertices):
    """
    Calculates the area of a 2D regular polygon using the Shoelace formula.

    Parameters:
    vertices (list of tuples): A list of the (x, y) coordinates of the vertices of the polygon.

    Returns:
    float: The area of the polygon.
    """
    n = len(vertices)
    if n < 3:
        return 0.0
    # Use the Shoelace formula to calculate the area of the polygon
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += (vertices[i][0] * vertices[j][1]) - (vertices[j][0] * vertices[i][1])
    return abs(area / 2.0)


print(polygon_area([(1,6),(3,1),(7,2),(4,4),(8,5)]))