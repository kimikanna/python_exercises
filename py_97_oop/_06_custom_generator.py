# Example 1

def square_all(numbers):
    for x in numbers:
        yield x ** 2


favorite_numbers = [6, 57, 4, 7, 68, 95]
squares = square_all(favorite_numbers)
for n in squares:
    print(n, end=" ")

print("\n------------")


# Example 2

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __iter__(self):
        yield self.x
        yield self.y
        self.x += 1
        self.y += 1


p = Point(1, 2)
print("", end="| ")
for _ in range(1, 10):
    cord_x, cord_y = p
    print(cord_x, cord_y, end=" | ")

print("\n------------")

# Example 3

fruits = ["banana", "mango", "apple"]
reverse_fruits = (y[::-1] for y in fruits)
for fruit in reverse_fruits:
    print(f"[{fruit}]", end=" ")
