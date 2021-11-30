from step.step_class import Step
import os

class SolverViz(Step):
    def set_display(self, display):
        self.display = display
    def run(self):
        if self.display is None:
            self.display = 'geogebra'
        out_path = "temp"

        move_command = f"cp {self.input_path} {self.path}/"
        print(f"SolverViz move command: {move_command}")
        if os.system(move_command) != 0:
            self.error()
        command = f"pushd {self.path} && ./run -t {self.display} -o {out_path} {self.input_path} && popd"
        print(f"Call to SolverViz: {command}")
        if os.system(command) != 0:
            self.error()

        move_command = f"mv {self.path}/{out_path}.ggb {out_path}.ggb"
        print(f"SolverViz move command: {move_command}")
        if os.system(move_command) != 0:
            self.error()
        return f"{out_path}.ggb"
        

