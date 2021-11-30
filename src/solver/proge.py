from solver.solver_class import Solver
import os

class Proge(Solver):
    def run(self):
        # Create the command string
        move_command = f"cp {self.input_path} {self.path}/Wernick/temp.pl"
        print(f"Proge move command: {move_command}")
        if os.system(move_command) != 0:
            self.error()
        out_path = "tmp"
        # Weird due to the way Proge works
        command = f"pushd {self.path} && echo \"temp.\nv\n{out_path}\" | {self.path}/run && popd"
        print(f"Call to Proge: {command}")
        # Dont actually check the error code. Proge needs to be closed with 
        # sigint...
        os.system(command)
        #    self.error()
        move_command = f"mv {self.path}/{out_path}.xml {out_path}.xml"
        print(f"Proge move command: {move_command}")
        if os.system(move_command) != 0:
            self.error()
        return f"{out_path}.xml"
