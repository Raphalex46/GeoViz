import os
from step.step_class import Step

class Geolog(Step):
    def __init__(self, path, input_path, output_path):
        super().__init__(path, input_path, output_path)
        self.solver = "proge"

    def set_solver(self, solver):
        self.solver = solver

    def ext_from_solver(self):
        if self.solver == "proge":
            return "pl"

    def run(self):
        out_ext = self.ext_from_solver()

        command = f"pushd {self.path} && ./run -t {self.solver} -l french\
        {self.input_path} > {self.out_path}.{out_ext} && popd"
        print(f"Call to Geolog: {command}")
        if os.system(command) != 0:
            self.error()

        return f"{self.out_path}.{out_ext}"
