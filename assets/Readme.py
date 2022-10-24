#!/usr/bin/env python
#  need to import cmdlogtime
import cmdlogtime

#need to specify a command line definition file.  See example command line definition file in this directory.
COMMAND_LINE_DEF_FILE = "./processLincsCommandLine.txt"

#There is also an example python file that uses all this stuff in this directory.
def main():
    # Call cmdlogtime.begin() at the beginning of main()
    (start_time_secs, pretty_start_time, my_args, logfile) = cmdlogtime.begin(COMMAND_LINE_DEF_FILE, sys.argv[0])
    
    # the command line arguments will be in the my_args dictionary returned, so you can access them like this:
    get_treats_vectors = my_args["get_treats_vectors"]
    
    #  Then you put all of your code here.....
    
    # if you want to add stuff to the logfile:
    logfile.write("Run Skim here for each of the B terms files in B_TERMS_DIR")
       
    #The only functions you probably will ever need in cmdlogtime are begin(), end(), and maybe make_dir. Here's an example:
    cmdlogtime.make_dir(intermediate_out_dir)

    # Call cmdlogtime.end() at the end of main()
    cmdlogtime.end(logfile, start_time_secs)

if __name__ == "__main__":
    main()
