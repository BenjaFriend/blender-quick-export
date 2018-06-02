# Blender/Python quick export as FBX!

# This is a script that go through all blender files in a certain
# directoy, and export them as .FBX files.

# This is depenedany on the quickExport.py script being in the same directoy as
# this, so make sure that it is there!

import os;
from subprocess import call;
import sys;
import argparse;

# Used to print console colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    # When --help or no args are given, print this help
    usage_text = (
    "Run this script with python:\n"
    " python " + __file__ + " -- [options]"
    );


    parser = argparse.ArgumentParser(description=usage_text);

    parser.add_argument('-o','--output', action='store',
                        type=str, default=os.getcwd(),
                        help='Output directory of the export. (Default is the current direectory)');

    parser.add_argument('-d','--modelsdir', action='store',
                        type=str, default=os.getcwd(),
                        help='Directory of the files to export. (Default is the current directory)');


    args = parser.parse_args();

    print bcolors.WARNING;
    print args;
    print bcolors.ENDC;

    # If args don't exist then stop
    if not args:
        print("\n\nPlease enter the necessary args!");
        parser.print_help();
        #return;

    outputDir = args.output;
    modelsDir = args.modelsdir;

    print bcolors.WARNING + "\n==== Batch Export Info ====\n";
    print "     Model Dir: " + modelsDir;
    print "     Output Dir: " + outputDir;
    print "\n===========================\n\n" + bcolors.ENDC;


    # For all the files in this directory
    for subdir, dirs, files in os.walk(modelsDir):
        for file in files:
            # If the extension on that file is a blender file
            ext = os.path.splitext(file)[-1].lower();
            if ext == '.blend':
                # Export it in blender
                blendFile = os.path.join(subdir, file);
                print ("     Current exporting: " + blendFile);

                call(["blender", blendFile ,"--background", "--python", "quickExport.py", "--", "-o", outputDir]);

    print ( bcolors.OKGREEN + "All done all done" + bcolors.ENDC);

if __name__ == '__main__':
    main();
