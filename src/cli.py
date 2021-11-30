""" This module contains the strings for getopt which describes valid
    arguments, and other miscellaneous variables """

shortoptions = "vhs:o:g:"
longoptions = ["version", "help",
               "geolog_path=", "solverviz_path=", "solver_path=", "solver=",
               "output=", "graphics="]
options_info = [
        ("-h, --help", "Print this help and exit"),
        ("-v, --version", "Print version number and exit"),
        ("--geolog_path", "Specify path to the Geolog executable"),
        ("--solverviz_path", "Specify path to the SolverViz executable"),
        ("--solver_path", "Specify path to the solver"),
        ("-s, --solver", "Specify the solver to be used"),
        ("-g, --graphics", "Specify graphics backend to use"),
        ("-o, --output", "Specify the output filename (without extension)")
]

options_corres = {
        '-s': "--solver",
        '-o': "--output",
        '-g': "--graphics"
        }
version = "0.1.1"
