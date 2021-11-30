import os
import os.path

""" Parent class for steps (part of the pipeline) """
class Step:
    def __init__(self, path, input_path, out_path):
        # Make the paths absolute for easier handling
        self.path = os.path.abspath(path)
        self.input_path = os.path.abspath(input_path)
        self.out_path = os.path.abspath(out_path)

    def run(self):
        """ Run step on input file """
        pass

    # Move files in the correct place to run the program
    def move_in(self):
        command = f"cp {self.input_path} {self.path}/"
        print("Step move in command: {command}")
        if os.system(command) != 0:
            self.error()

    def move_out(self, out_name):
        command = f"cp {self.path}/{out_name} {out_name}"
        print("Step move out command: {command}")
        if os.system(command) != 0:
            self.error()

    def error(self):
        """ Error out """
        exit()
