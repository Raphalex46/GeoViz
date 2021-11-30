from solver.solver_class import Solver
import os

class Proge(Solver):
    def run(self):
        # Create the command string
        move_command = f"cp {self.input_path} {self.path}/Wernick/tmp.pl"
        print(f"Proge move command: {move_command}")
        if os.system(move_command) != 0:
            self.error()
        # Weird due to the way Proge works
        command = f"pushd {self.path} && echo \"tmp.\nv\n{self.out_path}\" |\
        {self.path}/run && popd"
        print(f"Call to Proge: {command}")
        # Dont actually check the error code. Proge needs to be closed with 
        # sigint...
        os.system(command)
        #    self.error()

        remove_command = f"rm {self.path}/Wernick/tmp.pl"
        print(f"Proge remove command: {remove_command}")
        if os.system(remove_command) != 0:
            self.error()

        return f"{self.out_path}.xml"
