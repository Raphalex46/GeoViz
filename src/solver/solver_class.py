from step.step_class import Step

""" General solver abstract class """
class Solver(Step):
    def error(self):
        """ Error out """
        print("An error occured while running the solver.")
        exit()

