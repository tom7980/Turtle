import tkinter as tk
from PIL import Image, ImageTk

class TurtleGUI:
    def __init__(self, root):
        self.root = root
        root.title("Turtle Robot")

        self.position = [150,150]

        self.facing = "North"
        self.draw = True

        self.canvas = tk.Canvas(root, bg="white", height=300, width=300)
        self.canvas.grid(column=0, row=0, columnspan=4)

        self.make_turtle()

        tk.Button(window, text="↑", command=self.move_up).grid(column=0, row=1)
        tk.Button(window, text="↓", command=self.move_down).grid(column=1, row=1)
        tk.Button(window, text="←", command=self.move_left).grid(column=2, row=1)
        tk.Button(window, text="→", command=self.move_right).grid(column=3, row=1)
        tk.Button(window, text="↰", command=self.turn_left).grid(column=1, row=2)
        tk.Button(window, text="↱", command=self.turn_right).grid(column=2, row=2)
        tk.Button(window, text="Forward", command=self.move_forward).grid(column=3, row=2)
        tk.Button(window, text="Toggle Draw", command =self.toggle_draw).grid(column=0, row=2)

    def make_turtle(self):
        # Turtle Body
        self.canvas.create_rectangle(self.position[0]-4, self.position[1]-4, self.position[0] + 4, self.position[1] + 4, fill='#51f07c', tag=("turtle",))
        # Turtle Head
        self.canvas.create_rectangle(self.position[0]-2, self.position[1]-4, self.position[0] + 2, self.position[1] - 7, fill='#51f07c', tag=("turtle", "head"))

    def toggle_draw(self):
        self.draw = not self.draw
    
    def move_up(self):
        if self.draw == True:
            self.canvas.create_line(self.position[0], self.position[1], self.position[0], self.position[1] - 10, fill="black", width=1)
        self.canvas.move("turtle", 0, -10)
        self.position[1] -= 10


    def move_down(self):
        if self.draw == True:
            self.canvas.create_line(self.position[0], self.position[1], self.position[0], self.position[1] + 10, fill="black", width=1)
        self.canvas.move("turtle", 0, 10)
        self.position[1] += 10


    def move_left(self):
        if self.draw == True:
            self.canvas.create_line(self.position[0], self.position[1], self.position[0] - 10, self.position[1], fill="black", width=1)
        self.canvas.move("turtle", -10, 0)
        self.position[0] -= 10


    def move_right(self):
        if self.draw == True:
            self.canvas.create_line(self.position[0], self.position[1], self.position[0] + 10, self.position[1], fill="black", width=1)
        self.canvas.move("turtle", 10, 0)
        self.position[0] += 10

    def move_forward(self):
        if self.facing == "North":
            self.move_up()
        elif self.facing == "East":
            self.move_right()
        elif self.facing == "West":
            self.move_left()
        elif self.facing == "South":
            self.move_down()

    def turn_left(self):
        self.canvas.delete("head")
        if self.facing == "North":
            self.canvas.create_rectangle(self.position[0] - 4, self.position[1] - 2, self.position[0] - 7, self.position[1] + 2, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "West"
        elif self.facing == "West":
            self.canvas.create_rectangle(self.position[0] - 2, self.position[1] + 4, self.position[0] + 2, self.position[1] + 7, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "South"
        elif self.facing == "South":
            self.canvas.create_rectangle(self.position[0] + 4, self.position[1] - 2, self.position[0] + 7, self.position[1] + 2, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "East"
        elif self.facing == "East":
            self.canvas.create_rectangle(self.position[0] - 2, self.position[1] - 4, self.position[0] + 2, self.position[1] - 7, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "North"

    def turn_right(self):
        self.canvas.delete("head")
        if self.facing == "North":
            self.canvas.create_rectangle(self.position[0] + 4, self.position[1] - 2, self.position[0] + 7, self.position[1] + 2, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "East"
        elif self.facing == "West":
            self.canvas.create_rectangle(self.position[0] - 2, self.position[1] - 4, self.position[0] + 2, self.position[1] - 7, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "North"
        elif self.facing == "South":
            self.canvas.create_rectangle(self.position[0] - 4, self.position[1] - 2, self.position[0] - 7, self.position[1] + 2, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "West"
        elif self.facing == "East":
            self.canvas.create_rectangle(self.position[0] - 2, self.position[1] + 4, self.position[0] + 2, self.position[1] + 7, fill='#51f07c', tag=("turtle", "head"))
            self.facing = "South"




window = tk.Tk()

turtle_gui = TurtleGUI(window)

window.mainloop()
