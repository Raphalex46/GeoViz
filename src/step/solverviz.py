from step.step_class import Step
import os

class SolverViz(Step):
    def __init__(self, path, input_path, output_path):
        super().__init__(path, input_path, output_path)
        self.display = "geogebra"

    def set_display(self, display):
        self.display = display

    def ext_from_display(self):
        if self.display == "geogebra":
            return "ggb"

    def run(self):
        out_ext = self.ext_from_display()

        command = f"pushd {self.path} && ./run -t {self.display} -o {self.out_path}\
        {self.input_path} && popd"
        print(f"Call to SolverViz: {command}")
        if os.system(command) != 0:
            self.error()
        out_file = f"{self.out_path}.{out_ext}"
        self.launch_backend(out_file)
        return out_file
        
    def launch_backend(self, file):
        # Launch the program that corresponds to the backend we want to use
        if self.display == "geogebra":
            command = f"geogebra {file}"
            print(f"Launch graphic backend, command: {command}")
            if os.system(command) != 0:
                self.error()
