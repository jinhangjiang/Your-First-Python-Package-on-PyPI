# How to use CMD Log time:

## Write a Command file that teaches cmdlogtime how to parse your input args:

```
# first line is the description of what the program does.
# subsequent lines list positional arguments (PA), then key-value (KV)arguments (KVA).
# Positional line:
# PA_name|PA_Description|Is_out_dir|Is_Dir|Check_Directory|Is_file|Check_File|||
# Key/Value Line:
# KVA_name|KVA_Description|Is_out_dir|Is_Dir|Check_Directory|Is_file|Check_File|alternate_KVA_name|default value|type
# -print_x_thresh|print every X threshold|0|0|0|0|0|--print_every_x_threshold|1|int
# For KVAs for booleans, set default value to BOOLEANFALSE or BOOLEANTRUE.
# If default is BOOLEANFALSE, then if you set the flag it will be True. (or vice-versa)
# -get_top_words|get top most probable words|0|0|0|0|0|--get_top_probable_words|BOOLEANFALSE|
#  out_dir must be given.
# 
# Example below. First line describes the program
Compute AUCROC and other stats from infile. Print AUCROC and PR curves.
out_dir|Top level directory that holds all the results|1|1|1|0|0|||
infile|file path of file with a file with header in format call(1 or 0)\tX\tValue|0|0|0|1|1|||
-print_x_thresh|print every X threshold|0|0|0|0|0|--print_every_x_threshold|1|int
```
## Call cmdlinetime from your code as follows:

```python
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

```


Reference Blog: https://towardsdatascience.com/an-end-to-end-guide-to-publish-your-python-package-bdb56639662c
