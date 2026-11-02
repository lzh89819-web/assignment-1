"""Assignment 1: Turtle Drawing and QA Bot."""

import re
import turtle


# A shared color palette for the Turtle drawing.
COLORS = ["cyan", "yellow", "magenta", "lime", "orange", "white"]


def draw_square(pen, side_length):
    """Draw a square with the given side length."""
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)


def draw_triangle(pen, side_length):
    """Draw an equilateral triangle with the given side length."""
    for _ in range(3):
        pen.forward(side_length)
        pen.right(120)


def draw_star(pen, side_length):
    """Draw a five-pointed star with the given side length."""
    for _ in range(5):
        pen.forward(side_length)
        pen.right(144)


def task1_turtle_drawing():
    """Create a colorful pattern with changing shapes, colors, and sizes."""
    screen = turtle.Screen()
    screen.setup(width=900, height=700)
    screen.title("Assignment 1 - Colorful Turtle Pattern")
    screen.bgcolor("midnight blue")

    artist = turtle.Turtle()
    artist.shape("turtle")
    artist.speed(0)
    artist.width(2)

    # Repeat the pattern while changing its color, size, and direction.
    for step in range(60):
        artist.pencolor(COLORS[step % len(COLORS)])
        side_length = 30 + step * 2

        # Cycle through a square, a triangle, and a star.
        if step % 3 == 0:
            draw_square(artist, side_length)
        elif step % 3 == 1:
            draw_triangle(artist, side_length)
        else:
            draw_star(artist, side_length)

        artist.right(17)

    artist.hideturtle()
    screen.exitonclick()


def task2_qa_bot():
    """Answer questions by matching at least five supported keywords."""
    print("\nWelcome to the Edge AI QA Bot!")
    print("Ask about HKU, robots, Jetson, AI, or humans.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        question = input("You: ").strip().lower()

        if question in ("quit", "exit"):
            print("Bot: Goodbye!")
            break

        # Extract complete words so that short keywords such as "ai" match safely.
        words = set(re.findall(r"[a-z0-9]+", question))

        # Use conditional logic to select an answer for the matched keyword.
        if "hku" in words:
            print("Bot: HKU is The University of Hong Kong.")
        elif "robot" in words or "robots" in words:
            print("Bot: A robot is a programmable machine that can perform tasks.")
        elif "jetson" in words:
            print("Bot: Jetson Nano is an AI computer.")
        elif "ai" in words:
            print("Bot: AI means Artificial Intelligence.")
        elif "human" in words or "humans" in words:
            print("Bot: Humans design AI systems and decide how they should be used.")
        else:
            print("Bot: Sorry, I don't understand.")


def main():
    """Let the user choose which assignment task to run."""
    print("Assignment 1")
    print("1. Turtle Drawing")
    print("2. QA Bot")

    choice = input("Choose Task 1 or Task 2: ").strip()

    if choice == "1":
        task1_turtle_drawing()
    elif choice == "2":
        task2_qa_bot()
    else:
        print("Invalid choice. Please run the program again and enter 1 or 2.")


if __name__ == "__main__":
    main()
