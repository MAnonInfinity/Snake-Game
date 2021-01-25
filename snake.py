from turtle import Turtle

STARTING_X_POS = 0
MOVE_DIS = 20
UP_DIR = 90
DOWN_DIR = 270
LEFT_DIR = 180
RIGHT_DIR = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        global STARTING_X_POS
        for i in range(3):
            self.add_segment((STARTING_X_POS, 0))
            STARTING_X_POS -= 20

    def increase_size(self):
        last_segment = self.segments[len(self.segments)-1]
        self.add_segment(last_segment.position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            last_segment = self.segments[i-1]
            self.segments[i].goto(last_segment.position())
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN_DIR:
            self.head.setheading(UP_DIR)

    def down(self):
        if self.head.heading() != UP_DIR:
            self.head.setheading(DOWN_DIR)

    def left(self):
        if self.head.heading() != RIGHT_DIR:
            self.head.setheading(LEFT_DIR)

    def right(self):
        if self.head.heading() != LEFT_DIR:
            self.head.setheading(RIGHT_DIR)
