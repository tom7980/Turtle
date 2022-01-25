import tkinter as tk

# Expansion module for Turtle GUI that allows the user to specify paths using a simple language
# Instructions include:
# Movement: U(p), D(own), L(eft), R(ight), F(orward), B(ackward), T(urn):L | R
# Drawing: C(olour): white | black | red | green | blue | cyan | yellow | magenta, X(Toggle Draw)

# We do the same thing TKInter does and pass in the root window to apply the path module
class TurtlePathModule:
    def __init__(self, turtleGUI):
        self.turtle = turtleGUI
        self.root = turtleGUI.root

        self.path_input_frame = tk.Frame(self.root)
        self.path_input_frame.grid(column = 5, row = 0)

        tk.Label(self.path_input_frame, text = "Input Path here - type H and press Go to get recognised inputs").grid(column=0, row = 0)

        self.path_input_text = tk.Text(self.path_input_frame, height = 20, width = 40)
        self.path_input_text.grid(column = 0,row = 1, sticky=tk.W, columnspan=4)

        self.path_buttons = tk.Frame(self.path_input_frame)
        self.path_buttons.grid(column=0,row=2, stick=tk.W)
        self.path_error = tk.Label(self.path_buttons, text = 'Log:')
        self.path_error.grid(column = 1, row = 0, sticky=tk.W, padx = 2)

        tk.Button(self.path_buttons, text = "Go", command = self.runPath).grid(column = 0, row = 0, sticky=tk.W, padx = 2)

        self.help_message = "Instructions include: \nMovement: U(p), D(own), L(eft), R(ight), F(orward), B(ackward), T(urn):L | R \nDrawing: C(olour): white | black | red | green | blue | cyan | yellow | magenta, X(Toggle Draw)"

    def runPath(self):
        # Empty the log on new test run
        self.path_error.configure(text=f"Log:")
        # Get path input
        input = self.path_input_text.get("1.0", "end-1c")
        input = input.lower()

        if len(input) == 0:
            error = f"Error no input"
            self.path_error.configure(text=f"Log: {error}")
        elif len(input) == 1 and input == 'h':
            self.path_input_text.delete("1.0", "end")
            self.path_input_text.insert("1.0", self.help_message)
        else:
            commands = input.split(",")
            for command in commands:
                stripped = command.strip()
                if stripped == 'u':
                    self.turtle.move_up()
                elif stripped == 'd':
                    self.turtle.move_down()
                elif stripped == 'l':
                    self.turtle.move_left()
                elif stripped == 'r':
                    self.turtle.move_right()
                elif stripped == 't:r':
                    self.turtle.turn_right()
                elif stripped == 't:l':
                    self.turtle.turn_left()
                elif stripped == 'f':
                    self.turtle.move_forward()
                elif stripped == 'b':
                    self.turtle.move_backwards()
                elif stripped[0] == 'c':
                    if stripped[2:] in self.turtle.colours:
                        self.turtle.change_colour(stripped[2:])
                    else:
                        error = f"Error unrecognised colour - {stripped[2:]}"
                        self.path_error.configure(text=f"Log: {error}")
                        break
                elif stripped == 'x':
                    self.turtle.toggle_draw()
                else:
                    error = f"Error unrecognised character - {stripped}"
                    self.path_error.configure(text=f"Log: {error}")
                    break




        

