# Pascals Triangle
def generate_pascals_triangle(rows):
    triangle = []

    for row_num in range(rows):
        # Start the row with a 1
        row = [1]
        if triangle:  # If triangle is not empty
            last_row = triangle[-1]
            # Compute the in-between values for the row
            # [sum(pair) for pair in zip(last_row, last_row[1:])] this part just calculates the sum of elements.
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # End the row with a 1
            row.append(1)
        triangle.append(row)

    return triangle

# Function to print Pascal's Triangle
def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * len(triangle[-1])))

# Example usage
rows = 5
pascals_triangle = generate_pascals_triangle(rows)
print(pascals_triangle)
print_pascals_triangle(pascals_triangle)
