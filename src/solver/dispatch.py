from solver.proge import Proge

def instanciate_solver(solver_name, solver_path, input_path, out_path):
    if solver_name == "proge":
        return Proge(solver_path, input_path, out_path)
