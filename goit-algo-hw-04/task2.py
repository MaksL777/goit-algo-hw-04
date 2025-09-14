import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_snowflake(level, size=300):
    t = turtle.Turtle()
    t.speed(0)
    turtle.bgcolor("white")

    for _ in range(3):
        koch_curve(t, size, level)
        t.right(120)

    turtle.done()

if __name__ == "__main__":
    level = int(input("Вкажіть рівень рекурсії: "))
    draw_snowflake(level)
