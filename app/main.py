from app.shapes import Rectangle, Square, Circle

def main() -> None:
    shapes = [
        Rectangle(3, 4),
        Square(5),
        Circle(2)
    ]
    for s in shapes:
        print(s.describe())

if __name__ == "__main__":
    main()

