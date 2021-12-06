import getopt
import sys
import cli
import os
from solver import dispatch
from step import geolog, solverviz

def parse_cl():
    """ Parse command line """
    additionnal_options = []
    # First check for a configuration file in working directory
    if os.path.isfile("./geoviz.conf"):
        config_file = open("./geoviz.conf")
        additionnal_options = config_file.read().replace('\n', '').split(' ')
        config_file.close

    arg_list = additionnal_options + sys.argv[1:]
    print(arg_list)
    return getopt.getopt(arg_list, cli.shortoptions, cli.longoptions)

def handle_cl(args):
    """ Execute according to options. Leaving remaining value-options (and
    positional arguments) in a dictionnary """

    # Fill dictionnary with default values
    opt_dict = {
            '--geolog_path': "./Geolog",
            '--solverviz_path': "./SolverViz",
            '--solver': "proge",
            '--graphics': "geogebra",
            '--output': "out",
            '--keep_files': False
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
        if opt == '--keep_files':
            opt_dict['--keep_files'] = True

    if not ('--solver_path' in opt_dict.keys()):
        if opt_dict['--solver'] == 'proge':
            opt_dict['--solver_path'] = './Proge'

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

    # Initialize cleanup list
    cleanup = []

    print(f"Creating and running language layer...")
    # Create our first layer (geolog)
    language_layer = geolog.Geolog(options['--geolog_path'],
            options['input_file'], "tmp")
    language_layer.set_solver(options['--solver'])
    # Run language layer
    inter_file = language_layer.run()
    cleanup.append(inter_file)

    print(f"Creating and running solver layer...")
    # Create solver layer
    solve = dispatch.instanciate_solver(options['--solver'],
            options['--solver_path'], inter_file, "tmp")
    # Run solver layers
    viz_file = solve.run()
    print(viz_file)
    cleanup.append(viz_file)

    print(f"Creating and running graphic layer...")
    # Create graphic export layer
    graphic_layer = solverviz.SolverViz(options['--solverviz_path'], viz_file,
            options['--output'])
    # Specify the display backend to use
    graphic_layer.set_display(options['--graphics'])
    # Run graphic export layer
    out_file = graphic_layer.run()

    if not options['--keep_files']:
        for file in cleanup:
            if os.system(f"rm {file}") != 0:
                print("File cleanup failed !")
