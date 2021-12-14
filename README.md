# GeoViz

Glue Python code for [Geolog](https://github.com/Raphalex46/Geolog) and 
[SolverViz](https://github.com/Raphalex46/solverviz).

This program's purpose is to provide a simple command to run the whole pipeline
with:
- Geolog, the geometric construction description language
- A formal geometric construction solver supported by Geolog and which can
  export its construction program in the SolveViz format
- SolverViz, which can export the generic format to a specific graphic backend
- The corresponding graphic backend

## Usage

The program can be launched with `python3 src/geoviz.py [OPTIONS] <input_file>`.
The `<input_file>`, or you can use the wrapper script with
`./run [OPTIONS] <input_file>`, which will redirect the output to a log file.

Note that the options must be provided before the positional argument.
The program currently uses `getopt` to fetch the options, which is pretty
limited in this regard.

## Configuration file

In order to run the program with certain arguments by default, you can create
a configuration file named `geoviz.conf` in the working directory.

The configuration file is a just a single line with options, for example,
if SolverViz and Geolog are located in the parent directory, the following
options can be specified in the configuration file:
```
--geolog_path ../Geolog/ --solverviz_path ../SolverViz
```


