#!/usr/bin/env python
'''
Help: see https://github.com/stewart-lab/cmdlogtime
'''
__author__='Ron Stewart'
__author_email__='rstewart@morgridge.org'
import argparse
import os.path
from pathlib import Path as ph
import time
import sys
import pkg_resources

# ---------------  FUNCTIONS -------------------
def begin(command_line_def_file, write_msgs_to_stdout = 1):
    (start_time_secs, pretty_start_time) = get_time_and_pretty_time() 
    my_args = get_args(start_time_secs, pretty_start_time, command_line_def_file)
    addl_logfile = open_log_file(my_args["addl_logfile"])
    addl_logfile.write("Start: " + pretty_start_time +"\n")
    parms_logfile = open_log_file(my_args["parms_logfile"])
    script_logfile = open_log_file(my_args["script_logfile"])
    pkgs_logfile = open_log_file(my_args["pkgs_logfile"])
    write_args(my_args, parms_logfile)
    write_pkgs(pkgs_logfile)
    write_files(sys.argv[0], command_line_def_file, script_logfile)
    err_file = os.path.join(my_args["out_dir"], "err.txt")
    sys.stderr = open(err_file, 'w')
    if write_msgs_to_stdout:
        print("pretty_start: ", pretty_start_time)
        print("outdir: ", my_args["out_dir"])
    return (start_time_secs, pretty_start_time, my_args, addl_logfile)

def end(logfile, start_time_secs, write_msgs_to_stdout = 1):
    (end_time_secs, pretty_end_time) = get_time_and_pretty_time()
    total_elapsed_time = end_time_secs - start_time_secs
    logfile.write("\n\nEndtime: " + pretty_end_time + "\n")
    logfile.write("All done. Total elapsed time: " + str(total_elapsed_time) + " seconds.\n")
    close_log_file(logfile)  
    if write_msgs_to_stdout:
        print("All done. Total elapsed time: " + str(total_elapsed_time) + " seconds.\n")      
        
def build_arg_parser(command_line_def_file):
    with open(command_line_def_file, "r") as cmd_line_f:
        first_line = skip_headers(cmd_line_f)
        parser = argparse.ArgumentParser(description=get_description_from_first_line(first_line),
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        for line in cmd_line_f:
            if line:
                (arg_def_list, arg_def_kwargs_dict) = get_arg_defs_needed_to_add(line)
                if ("default" in arg_def_kwargs_dict.keys()):
                    if (arg_def_kwargs_dict['default'] == "BOOLEANFALSE"):  # magic number. ugh.
                        parser.add_argument(*arg_def_list, action="store_true") #defaults to False
                    elif (arg_def_kwargs_dict['default'] == "BOOLEANTRUE"):  # magic number. ugh.
                        parser.add_argument(*arg_def_list, action="store_false") #defaults to True 
                    else:
                        parser.add_argument(*arg_def_list, **arg_def_kwargs_dict)
                else:
                    parser.add_argument(*arg_def_list, **arg_def_kwargs_dict)      
    return parser

def skip_headers(f, header_flag="#"):
    line = f.readline()
    while line.startswith(header_flag):
        line = f.readline()
    return line

def get_description_from_first_line(line):
    return line.strip()

def get_args_from_line(line, sep="|"):
    # if we want defaults, so line doesnt need to be full,
    # add them now: args_defs = {'key': default_val}
    vals = line.strip().split(sep)
    # Validate the lines from the commandLine.txt file
    NUM_VALS_IN_LINE = 10
    #out_dir|Top level directory that holds all the results|1|1|1|0|0|||
    #infile|file path of file with a file with header in format call(1 or 0)\tX\tValue|0|0|0|1|1|||
    #-print_x_thresh|print every X threshold|0|0|0|0|0|--print_every_x_threshold|1|int
    line_copy = line
    line_copy = line_copy.strip(" ")
    if (len(line_copy) == 0):
        print("Problem in command file for line: \n", line,"\nThis line is just some number of spaces.")
        sys.exit(1)
    if (len(vals) != 10):
        print("Problem in command file for line: \n", line, "\nThere must be 10 values separated by 9 '", 
               sep, "' symbols. You need 9 delimiters, even if some values are null.")
        sys.exit(1)
    
    keys = ("name", "help", "is_out_dir", "is_dir", "check_dir", "is_file", "check_file", "alt_name", "default","type")
    args =  {k: v for (k, v) in zip(keys, line.strip().split(sep))}
    if (args["is_out_dir"] == '1' and args["is_dir"] == '0'):
        print("Must be a directory if it is an out_dir: \n", line, "\n")
        sys.exit(1)
        
    bools = {'0', '1'}
    if not (args["is_out_dir"] in bools and args["is_dir"] in bools and args["check_dir"] in bools
         and args["is_file"] in bools and args["check_file"] in bools ):
        print("One of your boolean values for is_out_dir, is_dir, check_dir, is_file, or check_file is not 0 or 1. See: \n",
            line)
        sys.exit(1)
    if (args["alt_name"]):
        if not args["alt_name"].startswith("--"):
            print("Alternate name must start with '--'. See: \n",
            line)
            sys.exit(1) 
        if args["default"]:
            if not args["type"] in ("float", "int", "bool", "str",""): 
                print("argstype:", args["type"]) 
                print("Valid types for casting are 'float', 'int', 'bool', and 'str'. See: \n",
                    line)
                sys.exit(1)     
    return args
    
def get_arg_defs_needed_to_add(line):
    arg_defs = get_args_from_line(line)
    if is_positional(arg_defs):
        return get_defs_for_positional_arg(arg_defs)
    else:
        return get_defs_for_flagged_arg(arg_defs)
    
def is_positional(arg_defs):
    return not arg_defs["name"].startswith("-")

def get_defs_for_positional_arg(arg_defs):
    assert arg_defs["alt_name"] == ""
    assert arg_defs["default"] == ""
    arg_def_list = []
    arg_def_list.append(arg_defs["name"])
    arg_def_kwargs_dict = {}
    arg_def_kwargs_dict["help"] = arg_defs["help"]
    
    if arg_defs["type"]:
        arg_def_kwargs_dict["type"] = eval(arg_defs["type"])
    return (arg_def_list, arg_def_kwargs_dict)
    
def get_defs_for_flagged_arg(arg_defs):
    assert(arg_defs["alt_name"]) 
    arg_def_list = []
    arg_def_list.append(arg_defs["name"])
    arg_def_list.append(arg_defs["alt_name"])
    arg_def_kwargs_dict = {}
    arg_def_kwargs_dict["help"] = arg_defs["help"]
    if (arg_defs["default"]):
        arg_def_kwargs_dict['default'] = arg_defs["default"]
    typestr = ""
    if (arg_defs["type"]):
        arg_def_kwargs_dict['type'] = eval(arg_defs["type"]) 
        if (arg_defs["default"]):
            arg_def_kwargs_dict['default'] =  arg_def_kwargs_dict['type']( arg_def_kwargs_dict['default'])  
    return (arg_def_list, arg_def_kwargs_dict)
    
def massage_and_validate_args(args, start_time_secs, pretty_start_time, command_line_def_file):
    new_args = {}
    dirs_to_check = []
    file_paths_to_check = []
    the_out_dir = ""
    with open(command_line_def_file, "r") as cmd_line_f:
        first_line = skip_headers(cmd_line_f) #first_line at this point will contain the description line.
        for line in cmd_line_f:
            if line:
                arg_defs = get_args_from_line(line)
                tmp_name = arg_defs["name"]
                if (arg_defs["name"].startswith("-")):
                    tmp_name = arg_defs["alt_name"].lstrip("-")
                new_args[tmp_name] = args.__dict__[tmp_name]  # if it is a directory or file,  new_args[tmp_name] will be overlain below
                if (arg_defs["is_dir"] == "1" or arg_defs["is_file"] == "1"):
                    if (args.__dict__[tmp_name]): #rms. I don't like this.  I think I need a different way to check that the flagged arg is NOT filled in, versus filled in incorrectly
                        new_args[tmp_name] = os.path.abspath(args.__dict__[tmp_name])
                if (arg_defs["is_out_dir"]  == "1"):
                    the_out_dir = new_args[tmp_name]
                if (arg_defs["check_dir"] == "1"):
                    if (args.__dict__[tmp_name]):  
                        #rms. I don't like this.  I think I need a different way to check that the flagged arg is NOT filled in, versus filled in incorrectly
                        dirs_to_check.append(new_args[tmp_name])
                if (arg_defs["check_file"] == "1"):  # same goes for files, see rms comment 2 lines above.
                    if (not args.__dict__[tmp_name].endswith("ZZZ")): #I think this is the correct logic... RMS.  magic number. Ugh.
                        file_paths_to_check.append(new_args[tmp_name])
    for fpath in file_paths_to_check:
        assert os.path.isfile(fpath), fpath + " file does NOT exist!"
    new_args["start_time_secs"] = start_time_secs
    new_args["pretty_start_time"] = pretty_start_time
    assert(the_out_dir != "")
    if ("rerun_out_directory" in new_args and new_args["rerun_out_directory"] != None):
        the_out_dir = new_args["rerun_out_directory"]
        print("rerundir in cmdlogtime:", new_args["rerun_out_directory"])
    else:
        make_dir(the_out_dir)
        the_out_dir = os.path.join(the_out_dir, pretty_start_time)
    make_dir(the_out_dir)
    
    for dir in dirs_to_check:
        assert os.path.isdir(dir), dir + " directory does NOT exist!"
    
    new_args["out_dir"] = the_out_dir
    addl_logfile, parms_logfile, script_logfile, pkgs_logfile = build_log_files(the_out_dir, pretty_start_time)  #requires an out_dir RMS!!!
    new_args["addl_logfile"] = addl_logfile
    new_args["parms_logfile"] = parms_logfile
    new_args["script_logfile"] = script_logfile
    new_args["pkgs_logfile"] = pkgs_logfile
    return new_args
                      
def get_args(start_time_secs, pretty_start_time, command_line_def_file):
    parser = build_arg_parser(command_line_def_file)
    my_args = massage_and_validate_args(parser.parse_args(), start_time_secs, pretty_start_time, command_line_def_file)
    return my_args

def make_dir(dir):
    x = ph(dir).mkdir(exist_ok=True)  

# ----------------------------------  LOGGING FUNCTIONS ----------------------
def build_log_files(out_dir, pretty_start_time):
    addl_logfile = build_log_file(out_dir, pretty_start_time, "addl_log")
    parms_logfile = build_log_file(out_dir, pretty_start_time, "parms_log")
    script_logfile = build_log_file(out_dir, pretty_start_time, "script_log")
    pkgs_logfile = build_log_file(out_dir, pretty_start_time, "pkgs_log")   
    return (addl_logfile, parms_logfile, script_logfile, pkgs_logfile)

def build_log_file(out_dir, pretty_start_time, file_str):
    make_dir(os.path.join(out_dir,file_str))
    logfile = file_str + "_" + str(pretty_start_time) + "_.txt"
    return (os.path.join(out_dir, file_str, logfile))
    
def open_log_file(log_file):
    return (open(log_file, "w+"))

def close_log_file(log_file_fh):
    log_file_fh.close()
        
def write_args (my_args, logfile):
    logfile.write("args:\n")
    for attr, value in my_args.items():
        logfile.write(str(attr) + "^" + str(value) + "\n") 
        
def write_pkgs (logfile):    
    installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}
    logfile.write("Installed Packages:\n")
    for key, value in installed_packages.items():
        logfile.write(key + ":" + value + "\n")
    
def write_files (curr_executing_file, command_line_file, logfile):
    write_file_contents(curr_executing_file, logfile)
    write_file_contents(command_line_file, logfile) 
               
def write_file_contents(a_file, logfile):
    logfile.write("\n\n-------------- START " + a_file + " -----------------\n")
    with open(a_file, "r") as file_to_write_out:
        for line in file_to_write_out:
            logfile.write(str(line))
    logfile.write("\n\n-------------- END " + a_file + " -----------------\n")              

# ----------------------------------   END LOGGING FUNCTIONS ----------------------
def get_time_and_pretty_time():
    time_struct = time.localtime()
    time_secs = time.mktime(time_struct)  #need to use something besides time.mktime if want fractions of sec.
    #pretty_time = time.strftime("%d_%b_%Y_%H_%M_%S", time_struct)  #old format
    pretty_time = time.strftime("%Y_%m_%d_%H_%M_%S", time_struct)  #New format that will sort better
    return(time_secs, pretty_time)         