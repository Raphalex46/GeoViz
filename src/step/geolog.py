import os
from step.step_class import Step

class Geolog(Step):
    def set_solver(self, solver):
        self.solver = solver
    def run(self):
        if self.solver is None:
            self.solver = "proge"

        out_path = "temp.pl"
        command = f"pushd {self.path} && ./run -t {self.solver} -l french {self.input_path} > {out_path} && popd"
        print(f"Call to geolog: {command}")
        if os.system(command) != 0:
            self.error()
        move_command = f"mv {self.path}/{out_path} {out_path}"
        print(f"Geolog move command: {move_command}")
        if os.system(move_command) != 0:
            self.error()
        return out_path
