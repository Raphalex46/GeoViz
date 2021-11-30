import getopt
import sys
import cli
from solver import proge, dispatch
from step import geolog, solverviz

def parse_cl():
    """ Parse command line """
    return getopt.getopt(sys.argv[1:], cli.shortoptions, cli.longoptions)

def handle_cl(args):
    """ Execute according to options. Leaving remaining value-options (and
    positional arguments) in a dictionnary """

    # Fill dictionnary with default values
    opt_dict = {
            '--solver_path': "./Proge",
            '--geolog_path': "./Geolog",
            '--solverviz_path': "./SolverViz",
            '--solver': "proge"
            }

    # For each argument, fill the dictionnary or take corresponding action
    for opt, val in args[0]:
        if opt == '-h' or opt == '--help':
            print_help()
            exit()
        if opt == '-v' or opt == '--version':
            print_version()
            exit()
        # Translate corresponding short / long options
        if opt in cli.options_corres.keys():
            opt = cli.options_corres[opt]
        # Fill the dictionnary
        opt_dict[opt] = val

    # If the number of positional arguments is incorrect, print usage and exit
    if len(args[1]) != 1:
        print_usage()
        exit(1)
    opt_dict['input_file'] = args[1][0]
    return opt_dict

def print_version():
    print(f"Geoviz v{cli.version}")

def print_help():
    """ Print help string """
    print_version()
    print_usage()
    print("Options: ")
    for opt, help_string in cli.options_info:
        print("{0: <15s} {1: <s}".format(opt, help_string))

def print_usage():
    """ Print usage """
    print(f"Usage: {sys.argv[0]} [OPTIONS] <input_file>")

if __name__ == '__main__':
    # Start by parsing command line arguments
    options = handle_cl(parse_cl())

    print(f"Creating and running language layer...")
    # Create our first layer (geolog)
    language_layer = geolog.Geolog(options['--geolog_path'],
            options['input_file'])
    language_layer.set_solver(options['--solver'])
    # Run language layer
    inter_file = language_layer.run()

    print(f"Creating and running solver layer...")
    # Create solver layer
    solve = dispatch.instanciate_solver(options['--solver'],
            options['--solver_path'], inter_file)
    # Run solver layers
    viz_file = solve.run()

    print(f"Creating and running graphic layer...")
    # Create graphic export layer
    graphic_layer = solverviz.SolverViz(options['--solverviz_path'], viz_file)
    # Specify the display backend to use
    graphic_layer.set_display("geogebra")
    # Run graphic export layer
    out_file = graphic_layer.run()
