""" Abstract class for steps (part of the pipeline) """
class Step:
    def __init__(self, path, input_path):
        self.path = path
        self.input_path = input_path

    def run(self):
        """ Run step on input file """
        pass

    def error(self):
        """ Error out """
        exit()
